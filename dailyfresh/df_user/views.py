from hashlib import sha1

from django.http.response import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse

from .models import *


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
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count': count})


def login(request):
    uname = request.COOKIES.get('uname', '')
    context = {'title': '用户登录', 'error_name': 0, 'err_pwd': 0, 'uname': uname}
    return render(request, 'df_user/login.html', context=context)


def login_handle(request):
    """
    登录操作
    :param request:
    :return:
    """
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    remember = post.get('remember', 0)
    # 根据用户名查询对象
    users = UserInfo.objects.filter(uname=uname);
    print(uname)
    if len(users) == 1:
        s1 = sha1()
        s1.update(upwd.encode('utf-8'))
        if s1.hexdigest() == users[0].upwd:
            red = HttpResponseRedirect('/user/user_center_info/')
            # 记住用户名
            if remember != 0:
                red.set_cookie('uname', uname)
            else:
                red.set_cookie('uname', '', max_age=-1)
            request.session['user_id'] = users[0].id
            request.session['user_name'] = uname
            return red
        else:
            context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 1, 'uname': uname, 'pwd': upwd}
            return render(request, 'df_user/login.html', context)
    else:
        context = {'title': '用户登录', 'error_name': 1, 'error_pwd': 0, 'uname': uname, 'pwd': upwd}
        return render(request, 'df_user/login.html', context)


def user_center_info(request):
    """
    用户中心页面
    :param request:
    :return:
    """
    user_email = UserInfo.objects.get(id=request.session['user_id']).uemail
    context = {
        'title': '用户中心',
        'user_email': user_email,
        'user_name': request.session['user_name']
    }
    return render(request, 'df_user/user_center_info.html', context)


def user_center_order(request):
    context = {'title': '用户中心'}
    return render(request, 'df_user/user_center_order.html', context)


def user_center_site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        post = request.POST
        user.ushou = post.get('ushou')
        user.uaddress = post.get('uaddress')
        user.uyoubian = post.get('uyoubian')
        user.uphone = post.get('uphone')
        user.save()
    context = {'title': '用户中心', 'user': user}
    return render(request, 'df_user/user_center_site.html', context)


def logout(request):
    request.session.flush()  # 清空当前用户所有session
    return redirect(reverse("df_goods:index"))
