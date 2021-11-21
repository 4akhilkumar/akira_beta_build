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

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('akira_apps.authentication.urls')),
    path('super_admin/', include('akira_apps.super_admin.urls')),
    path('staff/', include('akira_apps.staff.urls')),
    path('student/', include('akira_apps.student.urls')),
    path('academic_registration/', include('akira_apps.academic_registration.urls')),
    path('accounts/', include('akira_apps.accounts.urls')),

    # path('ckeditor/', include('ckeditor_uploader.urls')),
    path('ckeditor/upload/', login_required(ckeditor_views.upload), name='ckeditor_upload'),
    path('ckeditor/browse/', never_cache(login_required(ckeditor_views.browse)), name='ckeditor_browse'),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
]

handler400 = "akira_apps.authentication.views.handler400"
handler403 = "akira_apps.authentication.views.handler403"
handler404 = "akira_apps.authentication.views.handler404"
handler500 = "akira_apps.authentication.views.handler500"