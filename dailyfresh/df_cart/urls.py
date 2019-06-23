# coding=utf-8
from django.conf.urls import re_path, include
from . import views

app_name = 'df_cart'

urlpatterns = [
    re_path(r'^$', views.user_cart, name="cart"),
    re_path(r'^add(\d+)_(\d+)/$', views.add, name="add"),
    re_path(r'^edit(\d+)_(\d+)/$', views.edit, name="edit"),
    re_path(r'^delete(\d+)/$', views.delete, name="delete"),
]
