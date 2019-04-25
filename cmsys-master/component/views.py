
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
#from .models import CustomUser


def home_page(request):
    context = {
        "title" : "CMS ",
        "content" : "Welcome to home page",
    }
    if request.user.is_authenticated:
        context["premium_content"] = request.user.get_username()
    return render(request, "home_page.html", context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form" : form # to link template to #1
    }

    if form.is_valid():
        print(form.cleaned_data)
        username= form.cleaned_data.get("username")
        password= form.cleaned_data.get("password")
        user = authenticate(request,  username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            print("Wrong password")

    return  render(request, "login.html", context)



def logout_page(request):
    logout(request)
    return redirect("/")

User = get_user_model()

def register_page(request):
    form= RegisterForm(request.POST or None)
    context ={
        "form" : form
    }

    if form.is_valid():
        print(form.cleaned_data)
        username                = form.cleaned_data.get("username")
        email                   = form.cleaned_data.get("email")
        password                = form.cleaned_data.get("password")

        new_user= User.objects.create_user(username, email, password) # here new user is added after all datacheck
        return redirect("/login")


    return render(request, "register.html", context)
