from django.contrib import admin
from django.urls import path
from .views import PostListView, PostDetailView
from .views import PostCreateView, PostUpdateView, PostDeleteView
from . import views
urlpatterns = [
    # get views.py home() function
    # path('', views.home, name='blog_home'),
    path('', PostListView.as_view(), name='blog_home'),
    # fetch variable pk which means who post
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_form'),
    path('post/edit=<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('post/delete=<int:pk>/', PostDeleteView.as_view(), name='post_unlink'),
    path('about/', views.about, name='blog_about'),
]
# PostListView.as_view() search for a template
# has a html file named as <app>/<model>_<viewtpye>.html