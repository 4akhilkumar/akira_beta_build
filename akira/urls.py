"""akira URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve

from django.contrib.auth.decorators import login_required
from django.urls.conf import re_path
from django.views.decorators.cache import never_cache
from ckeditor_uploader import views as ckeditor_views
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('akira_apps.authentication.urls')),
    path('super_admin/', include('akira_apps.super_admin.urls')),
    path('staff/', include('akira_apps.staff.urls')),
    path('student/', include('akira_apps.student.urls')),
    path('academic_registration/', include('akira_apps.academic_registration.urls')),
    path('academic/', include('akira_apps.academic.urls')),
    path('accounts/', include('akira_apps.accounts.urls')),
    path('course/', include('akira_apps.course.urls')),
    path('specialization/', include('akira_apps.specialization.urls')),
    path('shigen/', include('akira_apps.shigen.urls')),

    # path('ckeditor/', include('ckeditor_uploader.urls')),
    path('ckeditor/upload/', login_required(ckeditor_views.upload), name='ckeditor_upload'),
    path('ckeditor/browse/', never_cache(login_required(ckeditor_views.browse)), name='ckeditor_browse'),

    path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('sitemap.xml',TemplateView.as_view(template_name="sitemap.xml", content_type="application/xml")),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
]