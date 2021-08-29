from django.urls import path ,include
from Portfolio import views

app_name='portfolio'

urlpatterns = [
    
    path('', views.Portfolio_page , name='Portfolio_page'),
    path('about/', views.about_page , name='about_page'),
    path('project/', include("Project.urls")),
    path('contact/', include("Contact_me.urls")),
    
]