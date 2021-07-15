from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .models import *
from address.models import Division, District, Upazila
from .forms.forms import RegistrationForm, LoginForm, ProfileForm, UserUpdateForm, ProfileUpdateForm
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
                profile.last_donate = request.POST.get("birthday")
                profile.gender = request.POST.get("gender")
                blood = request.POST.get("blood_group")
                blood = Blood.objects.get(id=blood)
                profile.blood = blood
                profile.division = request.POST.get("division")
                profile.district = request.POST.get("district")
                profile.thana = request.POST.get("upazilla")
                image = request.POST.get('profile_photo')
                print("image---", image)
                profile.image
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


def donor_profile_view(request, profile):
    donor = User.objects.get(id=profile)
    blood = donor.profile.blood
    related_donor = Profile.objects.filter(is_active=True, blood=blood)[0:6]
    context = {
        "donor": donor, "related_donor": related_donor
    }
    return render(request, 'accounts/profile.html', context)


def user_profile_view(request):
    donor = request.user
    blood = donor.profile.blood
    related_donor = Profile.objects.filter(is_active=True, blood=blood)[0:6]
    context = {
        "donor": donor, "related_donor": related_donor
    }
    return render(request, 'accounts/user_profile.html', context)

@login_required
def profile_update_view(request):
    donor = request.user
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('user-profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        "donor": donor
    }
    return render(request, 'accounts/profile_update.html', context)



