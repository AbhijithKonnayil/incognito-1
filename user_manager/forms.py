from django import forms
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):

    def password_check(self):
        if(len(self)<=4):
            raise ValidationError('Password lenth should be more than 4')
    def username_check(self):
        if(self[0]!='a'):
            raise ValidationError('username should start with a')

    username=forms.CharField(validators=[username_check])
    password = forms.CharField(validators=[password_check])