from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('exam/', include('examapp.urls')), 
    path('accounts/', include('django.contrib.auth.urls')),  
    path('', include('examapp.urls')),
]