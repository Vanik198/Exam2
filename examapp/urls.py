from django.urls import path
from . import views

app_name='examapp'

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    path('', views.home, name='home')
]
