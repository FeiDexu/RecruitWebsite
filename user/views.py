import base64
import json
import random
import re

import requests
from django.shortcuts import render, HttpResponse, redirect
# from rest_framework.decorators import api_view

from common.captcha import Captcha

from datetime import datetime, timedelta

from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
#
from user.forms import LoginForm
from web.models import *


# 获取验证码
# @api_view(('POST', 'GET'))
def get_captcha(request):
    captcha_text = ''.join(random.choices('123456789abcdefghigklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ', k=4))
    request.session['captcha'] = captcha_text
    # captcha类做了单例（一个类只能创建出唯一的实例）设计
    captcha_data = Captcha.instance().generate(captcha_text)
    return HttpResponse(captcha_data, content_type='image/png')


def register(request):
    """用户注册"""
    if request.method == 'GET':
        return render(request, 'user/signup.html')
    else:
        form_code = request.POST.get('tel_code', '0')
        sess_code = request.session.get('code', '1')
        if form_code == sess_code:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            tel = request.POST.get('tel')
            try:
                user = User(username=username, password=make_password(password), email=email, tel=tel)
                user.save()
                # User.objects.create(username=username, password=make_password(password),
                #                     email=email, tel=tel)
                return redirect('/login/')
            except Exception:
                hint = '注册失败，请尝试更换用户名'
        else:
            hint = '请输入正确的短信验证码'

        return render(request, 'user/signup.html', {
            'hint': hint
        })


# 处理表单验证错误信息
def handle_errors(errors):
    return {key: ';'.join(value) for key, value in errors.items()}
    # results = {}
    # for key, value, in errors.items():
    #     results[key] = ';'.join(value)
    #     return


# 用户登录
def login(request):
    if request.method == 'GET':
        backurl = request.GET.get('backurl', '/')
        if backurl != '/':
            backurl = base64.b64decode(backurl).decode()
        return render(request, 'user/signin.html', {'backurl': backurl})
    backurl = request.POST.get('backurl', '/')
    form = LoginForm(request.POST)
    if not form.is_valid():
        return render(request, 'user/signin.html', {
            'errors': handle_errors(form.errors)
        })
    if request.session.get('captcha').lower() != form.cleaned_data['captcha'].lower():
        return render(request, 'user/signin.html', {
            'errors': {'captcha': '请输入正确的验证码'}
        })
    # 登录成功
    user = User.objects.filter(username=form.cleaned_data['username']).first()
    if user and check_password(form.cleaned_data['password'], user.password):
        request.session['userid'] = user.userid
        request.session['username'] = user.username
        return redirect('/')
    return render(request, 'user/signin.html', {
        'hint': '用户名或密码错误'
    })


# 退出登录
def logout(request):
    request.session.flush()
    return redirect('/')


TEL_PATTERN = re.compile(r'1[3-9]\d{9}')


def send_code_by_sms(request):
    """通过短消息服务器发送验证码"""
    tel = request.GET.get('tel')
    # tel = '18008373685'
    if TEL_PATTERN.fullmatch(tel):
        code = ''.join(random.choices('0123456789', k=6))
        resp = requests.post(
            url='http://sms-api.luosimao.com/v1/send.json',
            auth=('api', 'key-231d57135b48a07b35efc6005a4e51c9'),
            data={
                'mobile': tel,
                'message': f'【左右网】 欢迎注册【左右网】，你本次的验证码是{code}，请保存好不要随便给他人，有效期为3分钟。【name二见】'
            },
            timeout=10,
            verify=False
        )
        data = json.loads(resp.text)
        if data['error'] == 0:
            request.session['code'] = code  # 将短信验证码保存在用户自己的会话对象（字典，每个用户都有属于自己的会话)中
            result = {'code': 20000, 'message': '短信验证码发送成功'}
        else:
            result = {'code': 20002, 'message': '短信验证码发送失败'}
    else:
        result = {'code': 20001, 'message': '请输入有效的手机号码'}
    return JsonResponse(result)


