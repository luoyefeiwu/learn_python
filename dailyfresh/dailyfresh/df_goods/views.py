from django.shortcuts import render
from .models import *


def index(request):
    # 查询各个分类的最新4条，最热4条数据
    typelist = TypeInfo.objects.all()
