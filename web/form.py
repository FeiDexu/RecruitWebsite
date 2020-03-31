# -*- coding: UTF-8 -*-
# @date: 2020/3/17 0017 19:12 
# @name: form
# @author：Fei Dexu
#
# from django import forms
# from web.models import *
# #
# # class RegisterForm(forms.Form):
# #     email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class": "form-control"}))
# #     # forms.类型() 定义对应字段的表单类型
# #     username = forms.CharField(min_length=4, max_length=12, widget=forms.TextInput(
# #         attrs={"class": "form-control"}))
# #
# #     password = forms.CharField(min_length=6, widget=forms.PasswordInput(
# #         attrs={"class": "form-control"}))
# #
# #     password2 = forms.CharField(min_length=6, widget=forms.PasswordInput(
# #         attrs={"class": "form-control"}))
# #
# #     valid_code = forms.CharField(widget=forms.TextInput(
# #         attrs={"class": "form-control"}))
#
# from wtforms import StringField, PasswordField, SubmitField, BooleanField
# from wtforms.validators import DataRequired, Length, ValidationError
#
#
# # 注册表单
# class RegisterForm(forms.Form):
#     username = StringField('用户名', validators=[DataRequired(message='用户名不能为空'), Length(max=32, message='用户名不能超过32个字符')])
#     mobile = StringField('手机号', validators=[DataRequired(message='手机号不能为空'), Length(max=16, message='请输入有效手机号')])
#     password = PasswordField('密码', validators=[DataRequired(), Length(min=8, max=16, message='密码不能小于8位')])
#     submit = SubmitField('提交')
#
#     # 验证用户名是否存在
#     def validate_username(self, field):
#         username = field.data
#         if User.query.filter_by(username=username).first():
#             raise ValidationError('该用户名已存在')
#
#     # 验证手机号是否存在
#     def validate_mobile(self, field):
#         mobile = field.data
#         if User.query.filter_by(mobile=mobile).first():
#             raise ValidationError('该手机号已存在')
#
#     # 验证邮箱是否存在
#     def validate_mobile(self, field):
#         email = field.data
#         if User.query.filter_by(email=email).first():
#             raise ValidationError('该邮箱已被注册')
#
#
# # 登录表单
# class LoginForm(forms.Form):
#     username = StringField('用户名/手机号', validators=[DataRequired(message='用户名不能为空')])
#     password = PasswordField('密码', validators=[DataRequired(message='密码不能为空')])
#     remember_me = BooleanField('记住我')
#     submit = SubmitField('登录')
#
#
#
#
