from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.contrib.auth import views
from django.urls import reverse

from .forms import InviteUserForm
from .utils import invite_user


class InviteUserView(FormView):
    template_name = 'selia_registration/invite_user.html'
    form_class = InviteUserForm
    success_url = 'invite_user_done'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        sender = self.request.user.username

        new_user = invite_user(email, sender, message=message)
        self.new_user_id = new_user.id
        return super().form_valid(form)

    def get_success_url(self):
        baseurl = reverse(self.success_url)
        query = self.request.GET.copy()
        query['user'] = self.new_user_id
        querystr = query.urlencode(safe='/')
        return f'{baseurl}?{querystr}'


class InviteUserDoneView(TemplateView):
    template_name = 'selia_registration/invite_user_done.html'


class PasswordChangeView(views.PasswordChangeView):
    template_name = 'selia_registration/password_change_form.html'
    success_url = 'done'

    def get_success_url(self):
        url = super().get_success_url()
        query = self.request.GET.urlencode(safe='/')
        return f'{url}?{query}'
