
from django.contrib import messages
from django.shortcuts import render, redirect
from accounts.forms import LoginForm
from django.contrib.auth import login, authenticate, logout
from accounts.forms import SearchDoner
from accounts.models import User, Profile
from core.models import Blood
from address.models import Division, District, Upazila
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    donors = Profile.objects.filter(is_active=True).order_by('-total_donate')[0:6]
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

    context = {"login_form": form, "donor": donors}
    return render(request, "pages/home.html", context)


def donor(request):
    donor_list = User.objects.filter(is_active=True).order_by('-id')
    context = {
        "donor": donor_list,
        "filter": SearchDoner,
    }
    print("----step 3-----")
    return render(request, 'pages/donor.html', context)


def contact(request):
    return render(request, 'pages/contact.html')
