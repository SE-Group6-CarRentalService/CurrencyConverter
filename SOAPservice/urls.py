from django.urls import path
from . import views

urlpatterns = [
    path('soap_service/', views.my_soap_application)
]