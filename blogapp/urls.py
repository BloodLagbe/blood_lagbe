from django.urls import path

from blogapp.views import (
    blogView,
)

app_name = 'blogapp'

urlpatterns = [
    path('', blogView, name='blog-view'),
]
