# coding=utf-8
from django.urls import path, re_path, include
from . import views

app_name = 'df_goods'
urlpatterns = [
    re_path('^$', views.index, name='index'),
    re_path(r'^user/', include('df_user.urls'))
]
