from django.shortcuts import render,redirect
from django.http import HttpResponse
from app01.My_forms import EmpForm
from app01 import models
from django.core.exceptions import ValidationError

# Create your views here.
#首页
def index(request):
    status=request.session.get("is_login")
    if not status:
        return redirect('login')
    else:
        return render(request,'index.html')
#表格
def table(request):
    status=request.session.get("is_login")
    if not status:
        return redirect('login')
    else:
        return render(request,'tables.html')
#日历
def calendar(request):
    status=request.session.get("is_login")
    if not status:
        return redirect('login')
    else:
        return render(request,'calendar.html')
#表单
def page_form(request):
    status=request.session.get("is_login")
    if not status:
        return redirect('login')
    else:
        return render(request,'form.html')
#图表
def chart(request):
    status=request.session.get("is_login")
    if not status:
        return redirect('login')
    else:
        return render(request,'chart.html')
#文字列表
def table_list(request):
    status=request.session.get("is_login")
    if not status:
        return redirect('login')
    else:
        return render(request,'table-list.html')
#图文列表
def table_list_img(request):
    status=request.session.get("is_login")
    if not status:
        return redirect('login')
    else:
        return render(request,'table-list-img.html')
#注册页面
def sign_up(request):
    status=request.session.get("is_login")
    if not status:
        return redirect('login')
    else:
        return render(request,'sign-up.html')
#登录页面
def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    else:
        name=request.POST.get("user-name")
        pwd=request.POST.get("user-pass")
        if name == "haokuo" and pwd == "haokuo":
            request.session['is_login']=True
            request.session['user_name']=name
            return redirect('index')
        else:
            error_message="用户名或密码错误"
            return render(request, "login.html",{"error_message":error_message})

#404错误页面
def page_404(request):
    return render(request,'404.html')

#注销页面
def logout(request):
    request.session.flush()
    return redirect('login')





















