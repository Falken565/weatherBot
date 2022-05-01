from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/<int:user_id>/', views.register, name='register'),
    path('weather/<int:user_id>/', views.weather, name='weather'),
]
