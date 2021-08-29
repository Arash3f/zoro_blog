from django.contrib import admin
from django.urls import path , include
from Zoro_Blog import views
from django.conf.urls.static import static
from Zoro_Blog import settings
urlpatterns = [

    path('admin/', admin.site.urls),
    path('portfolio/' , include("Portfolio.urls")),
    path('account/', include("Dashboard.urls")),
    path('', include("Blog.urls")),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)