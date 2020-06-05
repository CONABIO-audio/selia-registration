from django.urls import path
from django.urls import re_path
from django.contrib.auth import views as auth_views
from .views import InviteUserView
from .views import InviteUserDoneView
from .views import PasswordChangeView


urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='selia_registration/login.html'),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(
            template_name='selia_registration/password_reset_form.html',
            email_template_name='selia_registration/password_reset_email.html',
            subject_template_name='selia_registration/password_reset_subject.txt'),
        name='password_reset'
    ),
    path(
        'password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='selia_registration/password_reset_done.html'),
        name='password_reset_done'
    ),
    re_path(
        r'reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='selia_registration/password_reset_confirm.html'),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='selia_registration/password_reset_complete.html'),
        name='password_reset_complete'
    ),
    path(
        'password_change/',
        PasswordChangeView.as_view(),
        name='password_change'
    ),
    path(
        'password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='selia_registration/password_change_done.html'
        ),
        name='password_change_done'
    ),
    path(
        'invite/',
        InviteUserView.as_view(),
        name='invite'),
    path(
        'invite/done/',
        InviteUserDoneView.as_view(),
        name='invite_user_done'),
]
