from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from django.views.generic.edit import FormView
from django.template.loader import get_template
from .forms import InviteUserForm


class InviteUserView(FormView):
    template_name = 'selia_registration/invite_user.html'
    form_class = InviteUserForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        self.invite_user(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        # find your next url here
        back_url = self.request.GET.get('back',None) # here method should be GET or POST.
        if back_url:
            if self.error:
                return self.request.get_full_path()
            else:
                return "%s?new_user_id=%s" % (back_url, self.new_user_id) # you can include some query strings as well
        else :
            return '/' # what url you wish to return

    def invite_user(self, valid_data):
        try:
            sender = self.request.user
            username = valid_data['username']
            password = get_random_string(length=10)
                
            user = get_user_model().objects.create_user(username, username, password)
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
            print(e)
        pass
