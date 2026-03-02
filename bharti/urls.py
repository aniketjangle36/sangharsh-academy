from django.urls import path
from . import views

urlpatterns = [
    path('', views.bharti_list, name='bharti_list'),
]
