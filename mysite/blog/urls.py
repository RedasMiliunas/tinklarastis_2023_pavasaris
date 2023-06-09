from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.PostListView.as_view(), name='posts'),
    path('posts/<int:pk>', views.PostDetailView.as_view(), name='post'),
]