from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class SignInForm(forms.Form):
    username = forms.CharField(max_length=20, label='Nom d’utilisateur')
    password = forms.CharField(max_length=60, widget=forms.PasswordInput, label='Mot de passe')
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')
    #captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)