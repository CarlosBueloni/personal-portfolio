from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
]