
from django.contrib import messages
from django.shortcuts import render, redirect
from accounts.forms import  LoginForm
from django.contrib.auth import login, authenticate, logout
# Create your views here.
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
    blood = Blood.objects.all()
    division = Division.objects.all().order_by('-div_name')
    district = District.objects.all().order_by('-dist_name')
    upazila = Upazila.objects.all().order_by('-upazila_name')
    if request.POST:
        blood = request.POST.get("blood_group")
        divisions = request.POST.get('division')
        districts = request.POST.get('district')
        upazilas = request.POST.get('upazila')
        print("---------",blood, divisions,)
        # if blood:
        #     donor_list = Profile.objects.filter(blood__name=blood, is_active=True).order_by('-id')
        if divisions:
            donor_list = Profile.objects.filter(division__exact=divisions, is_active=True).order_by('-id')
        if donor_list:
            # pagination
            page = request.GET.get('page', 1)
            paginator = Paginator(donor_list, 6)

            try:
                donor_list = paginator.page(page)
            except PageNotAnInteger:
                donor_list = paginator.page(1)
            except EmptyPage:
                donor_list = paginator.page(paginator.num_pages)
            context = {
                "donor": donor_list, "district": district,
                "blood": blood, "upazila": upazila,
                "division": division,
            }
            print("----step 1-----")
            return render(request, 'pages/donor.html', context)
        else:
            print("----step 2-----")
            context = {
                "donor": donor_list, "district": district,
                "blood": blood, "upazila": upazila,
                "division": division,
            }
            return render(request, 'pages/donor.html', context)

    context = {
        "donor": donor_list, "district": district,
        "blood": blood, "upazila": upazila,
        "division": division,
    }
    print("----step 3-----")
    return render(request, 'pages/donor.html', context)


def contact(request):
    return render(request, 'pages/contact.html')
