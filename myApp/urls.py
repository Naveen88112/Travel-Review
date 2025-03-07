from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='home'),
    path('contact/', views.contact, name='home'),
    path('destinations/', views.destinations, name='home'),
    path('reviews/', views.reviews, name='home'),
]
