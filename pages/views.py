
from django.contrib import messages
from django.shortcuts import render, redirect
from accounts.forms import  LoginForm
from django.contrib.auth import login, authenticate, logout
# Create your views here.


def index(request):
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            phone = request.POST['phone']
            password = request.POST['password']
            user = authenticate(phone=phone, password=password)
            if user:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Try again")
        else:
            messages.error(request, "Phone number & Password doesn't match!")
    else:
        form = LoginForm()

    context = {"login_form": form}
    return render(request, "pages/home.html", context)
