# coding=utf-8
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    re_path('^$', views.index, name='index'),
    re_path(r'^user/', include('df_user.urls'))
]
