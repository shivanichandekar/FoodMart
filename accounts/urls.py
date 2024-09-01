from django.urls import path
from . import views

urlpatterns = [
    path('registerUuser/', views.registerUser, name='registerUser'),
    path('registerVendor/', views.registerVendor, name='registerVendor'),
]
