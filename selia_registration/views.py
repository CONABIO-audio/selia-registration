from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.template.loader import get_template
from django.contrib.auth import views
from django.urls import reverse

from .forms import InviteUserForm


class InviteUserView(FormView):
    template_name = 'selia_registration/invite_user.html'
    form_class = InviteUserForm
    success_url = 'invite_user_done'

    def form_valid(self, form):
        self.invite_user(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        baseurl = reverse(self.success_url)
        query = self.request.GET.copy()
        query['user'] = self.new_user_id
        querystr = query.urlencode(safe='/')
        return f'{baseurl}?{querystr}'

    def invite_user(self, valid_data):
        try:
            sender = self.request.user

            username = valid_data['username']
            password = get_random_string(length=10)
            user = get_user_model().objects.create_user(
                username,
                username,
                password)

            user.save()
            self.new_user_id = user.pk

            template = get_template('selia_registration/invitation_email.html')
            email_body = template.render({
                'sender': sender,
                'message': valid_data['message'],
                'username': username,
                'password': password
            })

            email_success = send_mail(
                'Invitación para unirte a la plataforma Selia',
                None,
                'clubpumasmas@gmail.com',
                [username],
                fail_silently=False,
                html_message=email_body
            )

            self.error = not email_success
        except Exception as e:
            self.error = True


class InviteUserDoneView(TemplateView):
    template_name = 'selia_registration/invite_user_done.html'


class PasswordChangeView(views.PasswordChangeView):
    template_name = 'selia_registration/password_change_form.html'
    success_url = 'done'

    def get_success_url(self):
        url = super().get_success_url()
        query = self.request.GET.urlencode(safe='/')
        return f'{url}?{query}'
