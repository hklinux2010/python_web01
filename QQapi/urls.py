from django.contrib import admin
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('add_num', views.add_number, name="add_num"),
    path('test', views.test, name="test"),
]
