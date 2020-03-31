# -*- coding: UTF-8 -*-
# @date: 2020/3/19 0019 23:07 
# @name: test
# @author：Fei Dexu

import requests
import json
import random

code = random.choices('0123456789', k=6)
def send_messag_example():
    resp = requests.post("http://sms-api.luosimao.com/v1/send.json",
                         auth=("api", "key-231d57135b48a07b35efc6005a4e51c9"),
                         data={
                             "mobile": "18008373685",
                             "message": f"【左右网】 欢迎注册【左右网】，你本次的验证码是{code}，请保存好不要随便给他人，有效期为3分钟。【name二见】"
                         }, timeout=3, verify=False)
    result = json.loads(resp.content)
    print(result)


def main():
    send_messag_example()


if __name__ == '__main__':
    main()
