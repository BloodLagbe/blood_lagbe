from django.urls import path
from .views import index
from pages import views as pages_views
from .ajax_request_view import ajax_request_filter


urlpatterns = [
    path('', index, name="home"),
    path('donor/', pages_views.donor, name='donor'),
    path('contact/', pages_views.contact, name='contact'),
    path('filter/donor', ajax_request_filter, name='filter_donor'),
]
