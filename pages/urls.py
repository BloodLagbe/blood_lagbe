from django.urls import path
from .views import index
from pages import views as pages_views


urlpatterns = [
    path('', index, name="home"),
    path('donor/', pages_views.donor, name='donor'),
    path('contact/', pages_views.contact, name='contact'),
]
