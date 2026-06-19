from django.urls import path
from . import views

urlpatters = [
    path('', views.checkout, name='checkout'),
]