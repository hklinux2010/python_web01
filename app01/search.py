from django.http import HttpResponse
from django.shortcuts import render,redirect

def search_from(request):
    return render(request,"search_from.html")

def search(request):
    request.encoding = 'utf-8'
    method=request.method
    if method == "GET":
        request.encoding = 'utf-8'
        if 'q' in request.GET and request.GET['q']:
            message = '你的搜索内容为：' + request.GET['q']
        else:
            message = '你提交了空的表单'

        return redirect('/page2/')
    elif method == "POST":
        ctx = {}
        ctx['rlt'] = request.POST['q']
        return render(request, "search_from.html", ctx)





