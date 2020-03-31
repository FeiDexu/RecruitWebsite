# -*- coding: UTF-8 -*-
# @date: 2020/3/20 0020 0:53 
# @name: alissm
# @author：Fei Dexu

import random

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

ACCESSKEYID = 'LTAI4FhXqvVErCQvGrdZEpeg'
ACCESSSECRET = 'z3oivIZmW3gNQ177V3TG4lKcPgZDE7'

client = AcsClient(ACCESSKEYID, ACCESSSECRET, 'default')
code = random.choices('0123456789', k=6)
request = CommonRequest()
request.set_accept_format('json')
request.set_domain('dysmsapi.aliyuncs.com')
request.set_method('POST')
request.set_protocol_type('https')
request.set_version('2017-05-25')
request.set_action_name('QuerySendDetails')

request.add_query_param('RegionId', "cn-hangzhou")
request.add_query_param('PhoneNumber', "18286241390")
request.add_query_param('SignName', '【左右网】')
request.add_query_param('TemplateCode', 'SMS_155355731')
request.add_query_param('TemplateParam', f'您正在申请手机注册，验证码为：${code}，5分钟内有效！为短信模板。')
request.add_query_param('SendDate', "2019-06-04")
request.add_query_param('PageSize', "1")
request.add_query_param('CurrentPage', "1")

response = client.do_action(request)
# python2:  print(response)
# print(response)
print(str(response, encoding='utf-8'))














