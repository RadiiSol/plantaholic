from django.urls import path
from . import views

urlpatterns = [
    path('', views.settings, name='settings'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('log_out', views.log_out, name='log_out'),
    path('login', views.login, name='login'),
   # path('settings', views.settings, name='settings'),
]
