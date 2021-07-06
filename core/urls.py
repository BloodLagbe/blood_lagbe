from django.urls import path
from . import data_load
from . import views

urlpatterns = [

    # ajax urls ------

    path('ajax/load_districts/', data_load.load_districts,
         name='ajax_load_districts'),

    path('ajax/load_upazila/', data_load.load_upazila,
         name='ajax_load_upazila'),

    path('ajax/load_union/', data_load.load_union,
         name='ajax_load_union'),
    path('ajax/load_village/', data_load.load_village,
         name='ajax_load_village'),
]
