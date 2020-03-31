# -*- coding: UTF-8 -*-
# @date: 2020/3/19 0019 0:35 
# @name: forms
# @author：Fei Dexu
import re

from django.core.exceptions import ValidationError
from django import forms


USERNAME_PATTERN = re.compile(r'\w{6,20}')


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True, min_length=6,
        max_length=20,
        error_messages={
            'required': '请输入用户名',
        })
    # required=True表示必填字段
    password = forms.CharField(
        strip=False,
        required=True, min_length=8,
        max_length=16,
        error_messages={
            'required': '请输入密码',
            'min_length': '密码最少8个字符'
        })

    captcha = forms.CharField(
        required=True,
        min_length=4,
        max_length=4,
        error_messages={
            'required': '请提供验证码信息',
            'min_length': '请输入正确的验证码',
            'max_length': '请输入正确的验证码',
        })

    def clean_username(self):
        username = self.cleaned_data['username']
        if not USERNAME_PATTERN.fullmatch(username):
            # 校验错误信息
            raise ValidationError('用户名由字母数字下划线组成，且长度为6-20个字符')
        return username



