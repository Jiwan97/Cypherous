from django.shortcuts import render, redirect
from .auth import *
from django.contrib.auth import update_session_auth_hash
from validate_email import validate_email  # pip install validate email
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User, Profile
from .forms import ProfileForm, ProfileForm2
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, force_text, DjangoUnicodeDecodeError
from .utils import generate_token
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.conf import settings
import threading


# Create your views here.
class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'Activate your account'
    email_body = render_to_string('accounts/activate.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)
    })

    # email = EmailMessage(subject=email_subject, body=email_body,
    #                      from_email=settings.EMAIL_FROM_USER,
    #                      to=[user.email]
    #                      )
    email = EmailMultiAlternatives(subject=email_subject,
                                   from_email=settings.EMAIL_FROM_USER,
                                   to=[user.email])
    email.attach_alternative(email_body, "text/html")

    if not settings.TESTING:
        EmailThread(email).start()


def send_notification_email(user, request):
    email_subject = 'Secure Your Account'
    email_body = render_to_string('accounts/notify.html', {'user': user, })

    email = EmailMultiAlternatives(subject=email_subject, body=email_body,
                                   from_email=settings.EMAIL_FROM_USER,
                                   to=[user.email])
    email.attach_alternative(email_body, "text/html")

    if not settings.TESTING:
        EmailThread(email).start()


def send_response_email(resp, content, request):
    email_subject = 'Response from Learn To Earn'
    email = EmailMultiAlternatives(subject=email_subject,
                                   from_email=settings.EMAIL_FROM_USER,
                                   to=[resp.email])
    email.attach_alternative(content, "text/html")

    if not settings.TESTING:
        EmailThread(email).start()


def send_reset_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'Reset your account'
    email_body = render_to_string('accounts/resetting_pass.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user)
    })

    email = EmailMultiAlternatives(subject=email_subject, body=email_body,
                                   from_email=settings.EMAIL_FROM_USER,
                                   to=[user.email])
    email.attach_alternative(email_body, "text/html")

    if not settings.TESTING:
        EmailThread(email).start()


@unauthenticated_user
def register(request):
    if request.method == "POST":
        context = {'has_error': False, 'data': request.POST}
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if len(password) < 6:
            messages.add_message(request, messages.ERROR,
                                 'Password should be at least 6 characters')
            context['has_error'] = True

        elif password != password2:
            messages.add_message(request, messages.ERROR,
                                 'Password mismatch')
            context['has_error'] = True

        elif not validate_email(email):
            messages.add_message(request, messages.ERROR,
                                 'Enter a valid email address')
            context['has_error'] = True

        elif not username:
            messages.add_message(request, messages.ERROR,
                                 'Username is required')
            context['has_error'] = True

        elif User.objects.filter(username=username).exists():
            messages.add_message(request, messages.ERROR,
                                 'Username is taken, choose another one')
            context['has_error'] = True

        elif User.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR,
                                 'Email is taken, choose another one')
            context['has_error'] = True

        # if context['has_error']:
        #     return HttpResponse('')
        if not context['has_error']:
            user = User.objects.create_user(username=username, email=email)
            user.set_password(password)
            user.save()
            send_activation_email(user, request)

            messages.add_message(request, messages.SUCCESS,
                                 'We sent you an email to verify your account')
    return render(request, 'accounts/register.html')


@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        context = {'data': request.POST}
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if not user:
            messages.add_message(request, messages.ERROR,
                                 'Invalid Username or Password')

        else:
            if not user.is_staff:
                if user and not user.is_email_verified:
                    messages.add_message(request, messages.ERROR,
                                         'Email is not verified, please check your email inbox')
                else:
                    if user.profile.sendNotification:
                        if user.is_active:
                            send_notification_email(user, request)

                    login(request, user)
                    messages.add_message(request, messages.SUCCESS,
                                         f'Welcome {user.username}')
                    if 'next' in request.POST:
                        return redirect(request.POST.get('next'))
                    else:
                        return redirect('/home')
            elif user.is_staff:
                login(request, user)
                messages.add_message(request, messages.SUCCESS,
                                     f'Welcome Admin, {user.username}')
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('/admins-dashboard')

    return render(request, 'accounts/login.html')


def logoutUser(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def activate_user(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))

        user = User.objects.get(pk=uid)

    except Exception:
        user = None
    if user and generate_token.check_token(user, token):
        user.is_email_verified = True
        user.save()

        messages.add_message(request, messages.SUCCESS,
                             'Email verified, you can now login')
        return redirect('/login')

    return render(request, 'accounts/activate-failed.html', {"user": user})


def forget(request):
    if request.method == "POST":
        context = {'data': request.POST}
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
        except Exception:
            user = None

        if not user:
            messages.add_message(request, messages.ERROR,
                                 'User does not exists for this Email Address  ')
            render(request, 'accounts/forgot-password.html', context)
        else:
            send_reset_email(user, request)
            messages.add_message(request, messages.SUCCESS,
                                 'We sent you an email to reset your password')
            return redirect('/login')
    return render(request, 'accounts/forgot-password.html')


@login_required()
def show_profile(request):
    profile = request.user
    if not profile.is_email_verified:
        profile.is_email_verified = True
        profile.save()
        return render(request, 'accounts/showProfile.html')
    else:
        return render(request, 'accounts/showProfile.html')


def view_profile(request, name):
    if Profile.objects.filter(username=name).exists():
        profile = Profile.objects.get(username=name)

        return render(request, 'accounts/viewProfile.html', {'users': profile})
    else:
        return render(request, 'accounts/errorView.html')


def error_profile(request):
    return render(request, 'accounts/errorView.html')


@login_required()
def edit_profile(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    form1 = ProfileForm2(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        form1 = ProfileForm2(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/showprofile')
        elif form1.is_valid():
            form1.save()
            return redirect('/showprofile')

    context = {'form': form,
               'form1': form1}

    return render(request, 'accounts/editProfile.html', context)


@login_required()
@nopassyet
def set_password(request):
    if request.method == "POST":
        context = {'has_error': False}
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if len(password) < 6:
            messages.add_message(request, messages.ERROR,
                                 'Password should be at least 6 characters')
            context['has_error'] = True

        elif password != password2:
            messages.add_message(request, messages.ERROR,
                                 'Password mismatch')
            context['has_error'] = True

        user1 = request.user
        user1.set_password(password)
        user1.save()
        update_session_auth_hash(request, user1)
        if not context['has_error']:
            return redirect('/password_set_done')

    return render(request, 'accounts/passwordSet.html')


def set_password_done(request):
    return render(request, 'accounts/passwordSetDone.html')
