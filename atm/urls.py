from django.urls import path
from . import views

urlpatterns = [
    path('', views.atm_interface, name='atm_interface'),
]
