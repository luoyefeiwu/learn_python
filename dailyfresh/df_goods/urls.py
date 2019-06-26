# coding=utf-8
from django.urls import path, re_path, include
from . import views

app_name = 'df_goods'
urlpatterns = [
    re_path('^$', views.index, name='index'),
    re_path(r'^user/', include('df_user.urls')),
    re_path(r'^search/', views.ordinary_search, name="ordinary_search"),  # 全文检索
]
