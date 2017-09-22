from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import AccountInfo

# Create your views here.


def home_list_page(request):
    """首页商品"""
    return render(request, 'home/index.html')


def login(request):
    '''显示登录页面'''
    return render(request, 'df_user/login.html')


def login_check(request):
    """用户登录验证"""
    username = request.POST.get('username')
    password = request.POST.get('pwd')
    if AccountInfo.objects.filter(username=username, password=password).exists():
        res = 1
    else:
        res = 0  # 密码或用户名错误
    return JsonResponse({'res': res})


def check_user_exist(request):
    """验证用户名是否存在"""
    username = request.POST.get('username')
    if AccountInfo.objects.filter(username=username).exists():  # 判断查询集中是否有数据
        res = 1
    else:
        res = 0
    return JsonResponse({'res': res})


def register(request):
    '''显示注册页面'''
    return render(request, 'df_user/register.html')


def register_handle(request):
    '''处理用户注册信息'''
    username = request.POST.get('user_name')  # 获取用户名
    password = request.POST.get('pwd')  # 获取密码
    email = request.POST.get('email')  # 获取邮箱
    accountInfo = AccountInfo()
    # accountInfo.username = username
    # accountInfo.password = password
    # accountInfo.email = email
    # accountInfo.save()  # 保存进数据库
    AccountInfo.objects.add_one_passport(username, password, email)

    return redirect('/user/login/')  # 跳转至登录页面

