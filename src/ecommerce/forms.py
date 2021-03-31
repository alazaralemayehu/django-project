from django import forms
from django.contrib.auth import get_user_model
class ContactForm(forms.Form):
  attributes = {
    "class": "form-control"
  }
  fullname = forms.CharField(widget=forms.TextInput(attrs=attributes))
  email = forms.EmailField(widget=forms.EmailInput(attrs=attributes))
  content = forms.CharField(widget=forms.Textarea(attrs=attributes))

  def clean_email(self):
    email = self.cleaned_data.get("email")
    if not "gmail.com" in email:
      raise forms.ValidationError("Email has to be gmail")
    return email
  

class LoginForm(forms.Form):
  attributes = {
    "class":"form-control"
  }

  username = forms.CharField(widget=forms.TextInput(attrs=attributes))
  password  = forms.CharField(widget = forms.PasswordInput(attrs=attributes))


class RegisterForm(forms.Form):
  attributes = {
    "class": "form-control"
  }
  username = forms.CharField(widget=forms.TextInput(attrs=attributes))
  email = forms.EmailField(widget=forms.EmailInput(attrs=attributes))
  password = forms.CharField(widget=forms.PasswordInput(attrs=attributes))
  password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput(attrs=attributes))

  def clean_username(self):
    user = get_user_model()

    username = self.cleaned_data.get('username')
    qs = user.objects.filter(username=username)

    if qs.exists():
      raise forms.ValidationError("Username is taken")
    return username

  def clean_email(self):
    user = get_user_model()
    email = self.cleaned_data.get('email')
    qs = user.objects.filter(email=email)

    if qs.exists():
      raise forms.ValidationError("Email is taken")

    return email

  def clean_password(self):
    password = self.cleaned_data.get('password')
    password2 = self.cleaned_data.get('password2')
    if password != password2:
      raise forms.ValidationError("Password Must match")
    return password