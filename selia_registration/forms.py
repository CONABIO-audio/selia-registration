from django import forms

class InviteUserForm(forms.Form):
    username = forms.EmailField(label='Correo electrónico', max_length=100)
    message = forms.CharField(label='Escribe tu mensaje', max_length=500, widget=forms.Textarea)