from django.urls import path

from blog.views import (
    blogView,
)

app_name = 'blog'

urlpatterns = [
    path('', blogView, name='blog-view'),
]
