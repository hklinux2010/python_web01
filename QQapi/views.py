import requests
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import json
from . import apps
from . import models
import threading
import urllib.request
import re

# Create your views here.
'''
简单body请求报文
{
    'x': int,
    'y': int,
}
'''

# 简单定义返回报文
res = {
    "status": '',
    "date": datetime.now(),
    "msg": ""
}


@csrf_exempt
def add_number(request):
    if request.method == "POST":
        if request.body.decode() == "":
            res["status"] = "Error"
            res["msg"] = "body is null!!"
            return JsonResponse(res)
        else:
            body = eval(request.body)
        if body['x'] == '' or body['y'] == '':
            res["status"] = "Error"
            res["msg"] = "please check body"
            return JsonResponse(res)
        elif type(body['x']) != int or type(body['y']) != int:
            res["status"] = "Error"
            res["msg"] = "please check body must be int"
            return JsonResponse(res)
        else:
            res["status"] = "Success"
            res["msg"] = apps.add(body['x'], body['y'])
            return JsonResponse(res)
    else:
        res["status"] = "Error"
        res["msg"] = "Method is not POST!!!"
        return JsonResponse(res)


@csrf_exempt
def test(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if 'message' in data:
            message = data['message']
            message_type = data['message_type']
            user_id = data['user_id']
            # 思知机器人
            result = requests.get('https://api.ownthink.com/bot?spoken={0}？'.format(message))
            re_data = json.loads(result.text)["data"]["info"]["text"]

            # 青云客机器人
            #     resp = requests.get("http://api.qingyunke.com/api.php", {'key': 'free', 'appid': 0, 'msg': message})
            #     resp.encoding = 'utf8'
            #     resp = resp.json()
            #     re_data = resp['content']
            data = {
                'message_type': message_type,
                'user_id': user_id,
                'message': re_data
            }
            ret = requests.post("http://192.168.100.195:5700/send_msg", json=data)
            return HttpResponse("测试")
    return HttpResponse(request.method)
