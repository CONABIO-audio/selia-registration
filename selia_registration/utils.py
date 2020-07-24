from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.template.loader import get_template
from django.utils.translation import gettext as _


def create_user_random_password(email):
    password = get_random_string(length=10)

    new_user = get_user_model().objects.create_user(
        username=email,
        email=email,
        password=password)

    new_user.save()
    return new_user, password


def send_invitation_email(email, sender, password, message=''):
    template = get_template('selia_registration/invitation_email.html')

    email_body = template.render({
        'sender': sender,
        'message': message,
        'username': email,
        'password': password
    })

    success_code = send_mail(
        _('Invitation to join selia'),
        None,
        'Selia <selia@conabio.gob.com>',
        [email],
        fail_silently=False,
        html_message=email_body
    )

    return success_code


def invite_user(email, sender, message=''):
    new_user, password = create_user_random_password(email)
    send_invitation_email(email, sender, password, message=message)
    return new_user
