"""blood_lagbe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve as mediaserve
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path, include
from blog.views import postView


urlpatterns = [
    path('admin/', admin.site.urls),

    # pages url ----
    path('', include("pages.urls"), name='index'),
    path('core/', include("core.urls")),
    path('accounts/', include("accounts.urls"), name='accounts'),

    path('', include("pages.urls")),
    path('blog/', include("blog.urls")),
    path('blog/<id>/', postView, name='blog-view'),
    # auth urls -----
    path('accounts/', include('django.contrib.auth.urls')),
]

# just development environment
urlpatterns.append(url(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$',
                       mediaserve, {'document_root': settings.MEDIA_ROOT}))

urlpatterns += staticfiles_urlpatterns()


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

# admin site title change
admin.sites.AdminSite.site_header = "Blood Lagbe"
admin.sites.AdminSite.site_title = "Blood Lagbe"
admin.sites.AdminSite.index_title = "Blood Lagbe"
