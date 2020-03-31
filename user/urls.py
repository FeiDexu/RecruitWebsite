# -*- coding: UTF-8 -*-
# @date: 2020/3/18 0018 17:04 
# @name: urls
# @author：Fei Dexu

from django.contrib import admin
from django.urls import path
from user.views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', login),
    path('captcha/', get_captcha),
    path('register/', register),
    path('register/mobile/', send_code_by_sms),
    # path('hot/', get_hot_distinct),

]
