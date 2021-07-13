from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm, ProfileForm
from django.contrib.auth import login, authenticate, logout
from .models import *
from address.models import Division, District, Upazila

# Create your views here.


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('/')

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
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    context = {}
    blood = Blood.objects.all()
    division = Division.objects.all()
    district = District.objects.all()
    upazilla = Upazila.objects.all()
    if request.POST:
        form = RegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            phone = form.cleaned_data.get('phone')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            form.save(commit=True)
            account = authenticate(
                name=name, phone=phone, email=email, password=raw_password)
            login(request, account)
            if profile_form.is_valid():
                profile = request.user.profile
                profile.image = request.POST.get("profile_photo")
                profile.birthday = request.POST.get("birthday")
                profile.gender = request.POST.get("gender")
                blood = request.POST.get("blood_group")
                blood = Blood.objects.get(id=blood)
                profile.blood = blood
                profile.division = request.POST.get("division")
                profile.district = request.POST.get("district")
                profile.thana = request.POST.get("upazilla")
                profile.save()
                return render(request, 'pages/home.html')
            return render(request, 'pages/home.html')
        else:
            context = {
                "registration_form": form, "blood": blood, "division": division,
                "district": district, "upazilla": upazilla,
                }
    else:  # GET request
        form = RegistrationForm()
        context = {
            "registration_form": form, "blood": blood, "division": division,
                "district": district, "upazilla": upazilla,
        }
    return render(request, 'accounts/registration.html', context)

