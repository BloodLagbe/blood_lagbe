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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from blog.views import postView
from core import utilities
#from django.conf.urls.i18n import i18n_patterns
#from django.conf.urls import url



urlpatterns = [
    path('admin/', admin.site.urls),

    # pages url ----
    path('', include("pages.urls"), name='index'),
    path('core/', include("core.urls")),
    path('accounts/', include("accounts.urls"), name='accounts'),

    path('', include("pages.urls")),
    path('blog/', include("blog.urls")),
    path('blog/<id>/', postView, name='blog-view'),

    # data import urls ----------

    path('division_import/', utilities.division_import,
         name='division_import'),

    path('district_import/', utilities.district_import,
         name='district_import'),

    path('upazila_import/', utilities.upazila_import,
         name='upazila_import'),

    path('union_import/', utilities.union_import,
         name='union_import'),

    path('village_import/', utilities.village_import,
         name='village_import'),

    # auth urls -----
    path('accounts/', include('django.contrib.auth.urls')),
]

# just development environment
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )


#urlpatterns += [url(r'^i18n/', include('django.conf.urls.i18n')),]
#urlpatterns += i18n_patterns(url(r'^admin/', admin.site.urls))
# admin site title change
admin.sites.AdminSite.site_header = "Blood Lagbe"
admin.sites.AdminSite.site_title = "Blood Lagbe"
admin.sites.AdminSite.index_title = "Blood Lagbe"
