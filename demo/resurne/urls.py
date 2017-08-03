# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create_page/$', views.create_page),
    url(r'^create_info/$', views.create_info),
    url(r'^list_page_(\d+)/$', views.list_page),
    url(r'^show_information_(\d+)/$', views.show_information),
    url(r'^edit_(\d+)/$', views.edit_info),
    url(r'^save_(\d+)/$', views.save_info),
]
