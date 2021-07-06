from django.shortcuts import render

from address.models import District, Upazila


def load_district(request):
    div_code = request.GET.get('division')
    district = District.objects.filter(
        division__div_code=div_code
    ).order_by('dist_name')
    context = {
        'district': district
    }
    return render(request, 'address/dropdown_list.html', context)


def load_upazila(request):
    dist_code = request.GET.get('district')
    upazila = Upazila.objects.filter(
        district__dist_code=dist_code
    ).order_by('upazila_name')
    context = {
        'upazila': upazila
    }
    return render(request, 'address/dropdown_list.html', context)
