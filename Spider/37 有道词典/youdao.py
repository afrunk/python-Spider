#!/usr/bin/env python
# -*- coding   : utf-8 -*-
# @Time        : 2019-11-10 13:58
# @Author      : yuelimin
# @Site        :
# @File        : you_dao_translation.py
# @Email       : yueliminvc@outlook.com
# @Software    : PyCharm
# @Description : Spider Programmer


import js2py
import requests
import random
import hashlib
import json
import jsonpath


class Translation(object):

    def __init__(self, query):
        self.query = query
        self.ua, self.split_ua = self.get_request_headers()
        self.split_ua = self.split_ua[1].encode("utf-8")
        self.api_url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    def get_response_data(self):
        """
        获取响应数据
        :return:
        """
        ua, data = self.joined_field()
        response = requests.post(self.api_url, data=data, headers=ua)
        response = response.content.decode("utf-8")
        response = json.loads(response)
        print("这个是请求到的数据")
        print(response)
        query = jsonpath.jsonpath(response, "$..src")
        translation = jsonpath.jsonpath(response, "$..tgt")
        print(query)
        print(translation)

    def get_decode_js_code(self):
        """
        处理js加密
        :return:
        """
        md5 = hashlib.md5(self.split_ua)
        # 获取加密之后的字符串
        bv = md5.hexdigest()
        # 获取现在的时间
        ts = js2py.eval_js('"" + (new Date).getTime();')
        # 随机数
        random_number = js2py.eval_js('parseInt(10 * Math.random(), 10);')
        salt = int(ts) + int(random_number)
        s = "fanyideskweb" + self.query + str(salt) + "n%A-rKaT5fb[Gy?;N5@Tj"
        md5 = hashlib.md5(s.encode("utf-8"))
        sign = md5.hexdigest()
        print(sign)
        return bv, ts, salt, sign

    def joined_field(self):
        """
        拼接
        :return: post数据, 请求头参数
        """
        bv, ts, salt, sign = self.get_decode_js_code()
        post_data = {
            "i": self.query,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "ts": ts,
            "bv": bv,
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME"
        }
        headers = {
            "User-Agent": self.ua,
            "Accept": "text/html,application/xhtml+xml,application/xml;"
                      "q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "Connect": "keep-alive",
            "Accept-Encoding": "gzip, deflate, br",
            "Host": "fanyi.youdao.com",
            "Origin": "http://fanyi.youdao.com",
            "Referer": "http://fanyi.youdao.com/",
            "Cookie": '_ga=GA1.2.910468718.1563467388; '
                      'OUTFOX_SEARCH_USER_ID_NCOO=591924106.9992104; '
                      'OUTFOX_SEARCH_USER_ID="{}"; '
                      '_gid=GA1.2.937494763.1573302486; '
                      'JSESSIONID=aaaC6A-p3ZK0T9qt62t5w; '
                      '___rl__test__cookies=1573364976940'.format("624654023@10.168.11.144")
        }
        return headers, post_data

    def get_request_headers(self):
        """
        获取ua
        :return: 初步的ua, 处理后的ua
        """
        # 这个也是一种提供随机ua的方式
        first_num = random.randint(55, 62)
        third_num = random.randint(0, 3200)
        fourth_num = random.randint(0, 140)
        os_type = [
            '(Windows NT 6.1; WOW64)',
            '(Windows NT 10.0; WOW64)', '(X11; Linux x86_64)',
            '(Macintosh; Intel Mac OS X 10_12_6)'
        ]
        chrome_version = 'Chrome/{}.0.{}.{}'.format(first_num, third_num, fourth_num)

        ua = ' '.join(['Mozilla/5.0',
                       random.choice(os_type),
                       'AppleWebKit/537.36',
                       '(KHTML, like Gecko)',
                       chrome_version, 'Safari/537.36'
                       ])
        return ua, ua.split("/", 1)


def main():
    while True:
        query = str(input("enter query string -> "))
        tran = Translation(query=query)
        tran.get_response_data()


if __name__ == '__main__':
    main()

"""
i: 伪娘
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
salt: 15733704113901
sign: a2517b1e5028484361aff0072f26e314
ts: 1573370411390
bv: 4b93d5124b22240a44d26f6e025092f0
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_CLICKBUTTION
i: 圆角少年
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
salt: 15733705020850
sign: ad6f1f99e5835b597669e0817fbb76de
ts: 1573370502085
bv: 4b93d5124b22240a44d26f6e025092f0
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_REALTlME
"""