from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserRegistrationForm(forms.ModelForm):
  password = forms.CharField(label='Password', 
                                            widget=forms.PasswordInput())
  password2 = forms.CharField(label='Repeat Password', 
                                            widget=forms.PasswordInput())

  class Meta:
    model = User
    fields = ('username', 'first_name', 'email')

  def clean_password2(self):
    cd = self.cleaned_data
    if cd['password'] != cd['password2']:
      raise forms.ValidationError('Password didn\'t match.')
    return cd['password'] 

  def clean_email(self):
    cd = self.cleaned_data
    qs = User.objects.filter(email=cd['email'])
    if qs.exists():
      raise forms.ValidationError('User with this Email already exists!') 
    return cd['email']                                              

class LoginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput)


class UserEditForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'email') 


class ProfileEditForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ('date_of_birth', 'photo')