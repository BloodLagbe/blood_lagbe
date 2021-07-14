from django.shortcuts import render
from accounts.models import User


def ajax_request_filter(request):
    template = "pages/donor_filter.html"
    divisionID = request.GET.get('division')
    districtID = request.GET.get('district')
    upazilaID = request.GET.get('upazila')
    bloodID = request.GET.get('blood')

    print("divisionID--------", divisionID)
    print("districtID--------", districtID)
    print("upazilaID--------", upazilaID)
    print("bloodID--------", bloodID)
    objects_list = User.objects.filter(is_active=True).order_by('-id')
    
    if divisionID:
        if divisionID == 0:
            objects_list = objects_list
        else:
            objects_list = objects_list.filter(
                profile__division__pk=divisionID
            )

    context = {
        'objects_list': objects_list
    }
    print('----objects_list', objects_list)
    return render(request, template, context)
