from django.urls import path

from . import views

urlpatterns = [
    path('', views.indexBot, name='indexBot'),
]