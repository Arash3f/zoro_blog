from django.urls import path
from Paper import views

app_name="paper"

urlpatterns = [
    path('<int:year>/<int:month>/<int:day>/<slug:post>/' , views.paper_detail , name='paper_detail'),  
]