from django.contrib import admin
from django.urls import path , include
from Dashboard import views

urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('register/', views.register.as_view() , name='register'),
    path('dashboard/', views.dashboard.as_view() , name='dashboard'),
    path('comments/', views.comments .as_view(), name='comments'),
    
]