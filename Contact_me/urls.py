from django.urls import path
from Contact_me import views

urlpatterns = [
    path('', views.contact_me_view.as_view() , name='contact_me_view'),
    ]