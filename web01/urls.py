"""web01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include

from app02 import views02
from app01 import views
from QQapi import urls

urlpatterns = [
    url('^admin/', admin.site.urls),
    path('index', views.index, name="index"),
    path('table', views.table, name='table'),
    path('calendar', views.calendar, name='calendar'),
    path('page_form', views.page_form, name='page_form'),
    path('chart', views.chart, name='chart'),
    path('table_list', views.table_list, name='table_list'),
    path('table_list_img', views.table_list_img, name='table_list_img'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('page_404', views.page_404, name='page_404'),

    path('insert_data', views.insert_data, name='insert_data'),
    path('test01', views.test01, name="test01"),
    path('add_book', views02.add_book, name="add_book"),

    path('testapi/', include(urls))

]
