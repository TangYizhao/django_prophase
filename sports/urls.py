import os

from django.urls import path

from sports import views

urlpatterns = [
    path('index', views.index_view),
]

