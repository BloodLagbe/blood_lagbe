from django.urls import path

from address import views

app_name = 'address'


urlpatterns = [
    path('load-district/', views.load_district, name='load_district'),
    path('load-upazila/', views.load_upazila, name='load_upazila'),
]
