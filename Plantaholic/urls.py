"""Plantaholic URL Configuration

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
from . import views
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('indoor_plants', views.indoor_plants, name='indoor_plants'),
    path('outdoor_plants', views.outdoor_plants, name='outdoor_plants'),
    path('gallery', views.gallery, name='gallery'),
    path('plant_growth', views.plant_growth, name='plant_growth'),
    path('plant_protection', views.plant_protection, name='plant_protection'),
    path('garden_tools', views.garden_tools, name='garden_tools'),
    path('suggestion', views.suggestion, name='suggestion'),
    path('user/', include("account.urls")),
]
