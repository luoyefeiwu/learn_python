# coding=utf-8
from django.urls import re_path

from . import views

app_name = 'df_user'
urlpatterns = [
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^register_handle/$', views.register_handle),
    re_path(r'^register_exist/$', views.register_exist),
    re_path(r'^login/$', views.login, name='login'),
    re_path(r'^login_handle/$', views.login_handle),
    re_path(r'^user_center_info/$', views.user_center_info,name='info'),
    re_path(r'^user_center_order/$', views.user_center_order),
    re_path(r'^user_center_site/$', views.user_center_site),
]
