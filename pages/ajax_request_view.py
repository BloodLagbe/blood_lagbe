from django.shortcuts import render
from accounts.models import User


def ajax_request_filter(request):
    template = "pages/donor_filter.html"
    division_id = request.GET.get('division')
    district_id = request.GET.get('district')
    upazila_id = request.GET.get('upazila')
    blood_id = request.GET.get('blood')
    objects_list = User.objects.filter(is_active=True).order_by('-id')
    if division_id:
        if division_id == 0:
            objects_list = objects_list
        else:
            objects_list = objects_list.filter(
                profile__division__pk=division_id
            )
    if district_id:
        if district_id == 0:
            objects_list = objects_list
        else:
            objects_list = objects_list.filter(
                profile__district__pk=district_id
            )
    if upazila_id:
        if upazila_id == 0:
            objects_list = objects_list
        else:
            objects_list = objects_list.filter(
                profile__upazila__pk=upazila_id
            )
    if blood_id:
        if blood_id == 0:
            objects_list = objects_list
        else:
            objects_list = objects_list.filter(
                profile__blood__pk=blood_id
            )

    context = {
        'objects_list': objects_list
    }
    print('----objects_list', objects_list)
    return render(request, template, context)
