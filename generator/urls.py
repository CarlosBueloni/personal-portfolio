from django.urls import path
from django.urls import include
from . import views

app_name = 'generator'

urlpatterns = [
    path('', views.generator, name='generator'),
    path('password/', views.password, name='password')
]