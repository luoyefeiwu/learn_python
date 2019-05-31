from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from .models import *
from hashlib import sha1


# Create your views here.
def register(request):
    """
    注册页面
    :param request:
    :return:
    """
    return render(request, 'df_user/register.html')


def register_handle(request):
    """
    用户注册操作
    :param request:
    :return:
    """
    # 接收用户输入
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')
    # 判断两次密码
    if upwd != upwd2:
        return redirect('/user/register/')
    # 密码加密
    s1 = sha1()
    s1.update(upwd.encode('utf-8'))
    upwd3 = s1.hexdigest()
    # 创建对象
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()
    # 注册成功,跳转到登录页
    return redirect('/user/login/')


def register_exist(request):
    """
    用户名是否存在
    :param request:
    :return:
    """
    get = request.GET
    uname = get.get('uanme')
    return JsonResponse(UserInfo().objects.filter(uname=uname).count())


def login(request):
    return render(request, 'df_user/login.html')


def login_handle(request):
    """
    登录操作
    :param request:
    :return:
    """
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    userinfo = UserInfo().objects.filter(uname=uname);
    return redirect('/user/user_center_info')


def user_center_info(request):
    """
    用户中心页面
    :param request:
    :return:
    """
    # 接收用户输入
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    s1 = sha1()
    s1.update(upwd.encode('utf-8'))
    upwd3 = s1.hexdigest()

    # 登录成功跳转到用户中心
    return redirect('/user/user_center_info/')
