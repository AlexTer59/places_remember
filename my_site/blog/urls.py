from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='blog-about'),
    path('home/', views.home, name='blog-home'),
]
