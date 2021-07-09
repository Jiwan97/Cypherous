from django.shortcuts import render, redirect
from .auth import unauthenticated_user
from validate_email import validate_email  # pip install validate email
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, force_text, DjangoUnicodeDecodeError
from .utils import generate_token
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.conf import settings
import threading


def home(request):
    context = {
        'activate_h': 'active'}
    return render(request, 'LearnToEarn/home.html',context)


def about(request):
    context = {
        'activate_a': 'active'}

    return render(request, 'LearnToEarn/about.html', context)


def courses(request):
    context = {
        'activate_cou': 'active'}
    return render(request, 'LearnToEarn/courses.html')


def contact(request):
    context = {
        'activate_c': 'active'}
    return render(request, 'LearnToEarn/contact.html',context)


class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'Activate your account'
    email_body = render_to_string('LearnToEarn/activate.html', {
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


def send_reset_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'Reset your account'
    email_body = render_to_string('LearnToEarn/resetting_pass.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user)
    })

    # email = EmailMessage(subject=email_subject, body=email_body,
    #                      from_email=settings.EMAIL_FROM_USER,
    #                      to=[user.email]
    #                      )
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

            return render(request, 'LearnToEarn/register.html', context, status=409)

        elif User.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR,
                                 'Email is taken, choose another one')
            context['has_error'] = True

            return render(request, 'LearnToEarn/register.html', context, status=409)

        if context['has_error']:
            return render(request, 'LearnToEarn/register.html', context)

        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()
        if not context['has_error']:
            send_activation_email(user, request)

            messages.add_message(request, messages.SUCCESS,
                                 'We sent you an email to verify your account')
            return redirect('/login')

    return render(request, 'LearnToEarn/register.html')


def login_user(request):
    if request.method == 'POST':
        context = {'data': request.POST}
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user and not user.is_email_verified:
            messages.add_message(request, messages.ERROR,
                                 'Email is not verified, please check your email inbox')
            return render(request, 'LearnToEarn/login.html', context, status=401)

        if not user:
            messages.add_message(request, messages.ERROR,
                                 'Invalid Username or Password')
            return render(request, 'LearnToEarn/login.html', context, status=401)

        login(request, user)

        return redirect('/home')

    return render(request, 'LearnToEarn/login.html')


# def forget(request):
#     return render(request, 'LearnToEarn/forgot-password.html')


def logoutUser(request):
    logout(request)
    return redirect('/home')


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

    return render(request, 'LearnToEarn/activate-failed.html', {"user": user})


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
            render(request, 'LearnToEarn/forgot-password.html', context)
        else:
            send_reset_email(user, request)
            messages.add_message(request, messages.SUCCESS,
                                 'We sent you an email to reset your password')
            return redirect('/login')
    return render(request, 'LearnToEarn/forgot-password.html')
