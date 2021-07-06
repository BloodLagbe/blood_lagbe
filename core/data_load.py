from .models import District, Union, Upazila, Village
from django.shortcuts import render


def load_districts(request):
    """ 
    filter districts by division_id 
    """
    division_id = request.GET.get('division_id')
    district = District.objects.filter(
        division_id=division_id).order_by('name')

    return render(request,
                  'dataload/dropdown_list_options.html',
                  {'district': district})


def load_upazila(request):
    """ 
    filter upazila by district_id 
    """

    district_id = request.GET.get('district_id')
    upazila = Upazila.objects.filter(district_id=district_id).order_by('name')

    return render(request,
                  'dataload/upazila_list_options.html', {'upazila': upazila})


def load_union(request):
    """ 
    filter union by upazila_id 
    """

    upazila_id = request.GET.get('upazila_id')
    union = Union.objects.filter(upazila_id=upazila_id).order_by('name')

    return render(request,
                  'dataload/union_list_options.html', {'union': union})


def load_village(request):
    """ 
    filter village by union_id 
    """

    union_id = request.GET.get('union_id')
    village = Village.objects.filter(union_id=union_id).order_by('name')

    return render(request,
                  'dataload/village_list_options.html', {'village': village})
