from django.urls import path
from django.urls import include
from . import views

app_name = 'generator'

urlpatterns = [
    path('', views.home, name='home'),
    path('password/', views.password, name='password')
]