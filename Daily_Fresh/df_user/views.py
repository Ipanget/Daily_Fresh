from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import AccountInfo
from .task import send_register_success_mail  # 导入发送邮件任务函数
# from django.conf import settings
from django.views.decorators.http import require_http_methods, require_POST, require_GET
# from django.core.mail import send_mail
# Create your views here.


def home_list_page(request):
    """首页商品"""
    return render(request, 'home/index.html')


@require_http_methods(['GET', 'POST'])
def register(request):
    if request.method == 'GET':
        """显示注册页面"""
        return render(request, 'df_user/register.html')
    else:
        """处理用户注册信息"""
        username = request.POST.get('user_name')   # 获取用户名
        password = request.POST.get('pwd')         # 获取密码
        email = request.POST.get('email')          # 获取邮箱
        AccountInfo.objects.add_one_passport(username, password, email)                # 将注册信息保存进数据库
        send_register_success_mail(username=username, password=password, email=email)  # 发送注册成功邮件
        return redirect('/user/login/')            # 跳转至登录页面


def login(request):
    """显示登录页面"""
    if 'username' in request.COOKIES:
        username = request.COOKIES['username']
    else:
        username = ''
    return render(request, 'df_user/login.html', {'username':username})


@require_POST
def login_check(request):
    """用户登录验证"""
    username = request.POST.get('username')
    password = request.POST.get('pwd')
    remember = request.POST.get('remember')
    if AccountInfo.objects.get_one_passport(username=username, password=password):
        # 当密码和用户名正确时会返回True
        jres = JsonResponse({'res':1})
        if remember:
            # 当记住用户名被选中
            jres.set_cookie('username', username, max_age=14*24*3600)
        return jres
    else:
        return JsonResponse({'res': 0})  # 密码或用户名错误


@require_POST
def check_user_exist(request):
    """验证用户名是否存在"""
    username = request.POST.get('username')
    if AccountInfo.objects.get_one_passport(username=username):
        res = 1
    else:
        res = 0
    return JsonResponse({'res': res})


# @require_http_methods({'post', 'get'})
# def register_handle(request):
#     """处理用户注册信息"""
#     username = request.POST.get('user_name')  # 获取用户名
#     password = request.POST.get('pwd')  # 获取密码
#     email = request.POST.get('email')  # 获取邮箱
#     # accountInfo = AccountInfo()
#     # accountInfo.username = username
#     # accountInfo.password = password
#     # accountInfo.email = email
#     # accountInfo.save()  # 保存进数据库
#     AccountInfo.objects.add_one_passport(username, password, email)
#     # send_mail('欢迎信息', '', settings.EMAIL_FROM, [email], html_message=message)
#     # send_mail('Hello,Python', '你好', settings.EMAIL_FROM, [email])  # 发送邮件给用户send_mail(subject, message, from_email, recipient_list,, html_message=None)
#     send_register_success_mail(username=username, password=password, email=email)
#     return redirect('/user/login/')  # 跳转至登录页面

