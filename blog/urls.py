from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    # get views.py home() function
    path('', views.home, name='blog_home'),
    path('about/', views.about, name='blog_about'),
]
