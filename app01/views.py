from django.shortcuts import render, redirect
from django.http import HttpResponse
from app01.My_forms import EmpForm
from django import forms
from app01 import models
from django.core.exceptions import ValidationError






def test01(request):
    return render(request, 'test01.html')


def auth(request):
    status = request.session.get("is_login")
    if not status:
        return redirect('login')


# Create your views here.
# 首页
def index(request):
    status = request.session.get("is_login")
    if not status:
        return redirect('login')
    else:
        return render(request, 'index.html')


# 表格
def table(request):
    status = request.session.get("is_login")
    if not status:
        return redirect('login')
    else:
        return render(request, 'tables.html')


# 日历
def calendar(request):
    status = request.session.get("is_login")
    if not status:
        return redirect('login')
    else:
        return render(request, 'calendar.html')


# 表单
def page_form(request):
    status = request.session.get("is_login")
    if not status:
        return redirect('login')
    else:
        return render(request, 'form.html')


# 图表
def chart(request):
    status = request.session.get("is_login")
    if not status:
        return redirect('login')
    else:
        return render(request, 'chart.html')


# 文字列表
def table_list(request):
    status = request.session.get("is_login")
    if not status:
        return redirect('login')
    else:
        return render(request, 'table-list.html')


# 图文列表
def table_list_img(request):
    status = request.session.get("is_login")
    if not status:
        return redirect('login')
    else:
        return render(request, 'table-list-img.html')


# 注册页面
def sign_up(request):
    status = request.session.get("is_login")
    if not status:
        return redirect('login')
    else:
        return render(request, 'sign-up.html')


# 登录页面
def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        name = request.POST.get("user-name")
        pwd = request.POST.get("user-pass")
        if models.add.objects.filter(name=name).exists():
            pwd2 = models.add.objects.filter(name=name)[0].password
            if pwd == pwd2:
                request.session['is_login'] = True
                request.session['user_name'] = name
                return redirect('index')
            else:
                message = "用户名或密码错误"
                return render(request, "login.html", {"message": message})
        else:
            message = "用户名或密码错误"
            return render(request, "login.html", {"message": message})


# 404错误页面
def page_404(request):
    return render(request, '404.html')


# 注销页面
def logout(request):
    request.session.flush()
    return redirect('login')


# 写入数据库
def insert_data(request):
    status = request.session.get("is_login")
    if not status:
        return redirect('login')
    else:
        if request.method == "GET":
            return redirect('sign_up')
        else:
            name = request.POST.get("user-name")
            pwd1 = request.POST.get("password")
            pwd2 = request.POST.get("re-password")
            email = request.POST.get("email")
            print(email, name, pwd1, pwd2)
            if pwd1 == pwd2:
                add = models.add(name=name, email=email, password=pwd1)
                add.save()
                message = "注册成功"
                return render(request, "login.html", {"message": message})
            else:
                message = "两次密码不一致"
                return render(request, "sign-up.html", {"message": message})
