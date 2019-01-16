from django.shortcuts import render, redirect
from .models import *
from hashlib import sha1


def register(request):
    return render(request, 'df_user/register.html')


def register_handle(request):
    # 接收用户输入
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')
    # 判断密码是否一致
    if upwd != upwd2:
        return redirect('/user/register')
    # 密码加密

    s1 = sha1()
    # 对s1进行更新
    s1.update(upwd.encode())
    # 加密处理
    upwd3 = s1.hexdigest()

    # 创建对象
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()
    # 注册成功，并跳转到登录页面
    return redirect('/user/login')
