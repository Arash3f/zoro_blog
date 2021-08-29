from django.urls import path
from Project import views

app_name="Project"

urlpatterns = [
    path('detail/<slug:slug>/' , views.project_detail,name='project_detail'),
    path('list/' , views.project_list.as_view(),name='project_list'),
]