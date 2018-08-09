from django.http import HttpResponse
from django.shortcuts import render_to_response


# 表单
def search_form(request):
    return render_to_response('search_form.html')


# 接收请求数据

def search(requset):
    requset.encoding = 'utf-8'
    if 'q' in requset.GET:
        message = '你搜索的内容为:' + requset.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)
