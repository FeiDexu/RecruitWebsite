# -*- coding: UTF-8 -*-
# @date: 2020/3/16 0016 21:38 
# @name: urls
# @author：Fei Dexu

from django.urls import path

from web.views import *

urlpatterns = [
    path('hot/', get_hot_distinct),
    path('', index)
]

