from django import forms
from django.contrib.auth.models import User
from first_app.models import UserInfo

class FormName(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields  = ('username','email','password')


class UserProfile(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields = ['pic']
    # name  = forms.ModelForm()
    # name = forms.CharField()
    # last_name = forms.CharField()
    # email = forms.CharField()


