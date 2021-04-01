from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model, logout
from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
  context= {
    "title": "Home",
    "premium_content": "this is premium content"
  }
  return render(request, "home_page.html", context)

def about_page (request):
  context= {
    "title": "about"
  }
  return render(request, "home_page.html", context)
  
def contact_page(request):
  contact_form = ContactForm(request.POST or None)
  context= {
    "title": "contact",
    "form" : contact_form
  }
  if contact_form.is_valid():
    print(contact_form.cleaned_data)
  
  return render(request, "contact/view.html", context) 

def logout_form(request):
  logout(request)
  return redirect("home")

def login_page(request):
  login_form = LoginForm(request.POST or None)
  context = {
    "form": login_form
  }
  if login_form.is_valid():
    username = login_form.cleaned_data.get('username')
    password = login_form.cleaned_data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      print(request.user.is_authenticated())
    return render (request,'home_page.html',context)

  return render (request,'auth/login.html',context)

def register_page(request):
  user = get_user_model()

  register_form = RegisterForm(request.POST or None)
  context = {
    "form": register_form
  }

  if register_form.is_valid():
    cleaned_data = register_form.cleaned_data
    username = cleaned_data.get('username')
    email = cleaned_data.get('email')
    password = cleaned_data.get('password')
    # password2 = cleaned_data.get('password2')

    new_user = user.objects.create_user(username, email, password)

    return render (request,'home_page.html',context)
    print(new_user)

  return render (request,'auth/register.html',context)