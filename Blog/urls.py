from django.urls import path , include
from Blog import views

urlpatterns = [
    path('paper/' , include("Paper.urls")),
    path('', views.blog , name='blog'),
    path('tag/<slug:tag_slug>/' , views.blog , name='main_site_tag'),
    
]
