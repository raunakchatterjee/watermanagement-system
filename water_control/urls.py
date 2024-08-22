from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('control_pump/', views.control_pump, name='control_pump'),
]
