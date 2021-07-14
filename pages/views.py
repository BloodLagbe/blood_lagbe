
from django.contrib import messages
from django.shortcuts import render, redirect
from accounts.forms import  LoginForm
from django.contrib.auth import login, authenticate, logout
# Create your views here.
from accounts.models import User, Profile


def index(request):
    # donor = User.objects.filter(is_active=True).order_by('user__total_donate')[0:6]
    donor = Profile.objects.filter(is_active=True).order_by('-total_donate')[0:6]
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

    context = {"login_form": form, "donor": donor}
    return render(request, "pages/home.html", context)


def donor(request):
    donor_list = User.objects.filter(is_active=True).order_by('-id')
    context = {
        "donor": donor_list
    }
    return render(request, 'pages/donor.html', context)


def contact(request):
    return render(request, 'pages/contact.html')
