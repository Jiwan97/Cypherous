from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, ),
    path('login/', views.login_user, ),
    path('forgot-p/', views.forget),
    path('logout/', views.logoutUser),
    path('showprofile/', views.show_profile),
    path('editprofile/', views.edit_profile),
    path('viewprofile/<str:name>', views.view_profile),
    path('viewprofile/', views.error_profile),
    path('password_set/', views.set_password),
    path('password_set_done/', views.set_password_done),
    path('activate-user/<uidb64>/<token>',
         views.activate_user, name='activate'),
    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset.html",),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),
         name="password_reset_complete"),
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='accounts/passwordChange.html')),
    path('password_change_done/', auth_views.PasswordChangeView.as_view(
        template_name='accounts/passwordChangeDone.html'), name='password_change_done'),

]
