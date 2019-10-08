#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Github 上clone下来的代码
来源：https://github.com/DropsDevopsOrg/ECommerceCrawlers/tree/master/DianpingCrawler
2019-10-8 可跑 直接运行没有问题 但是不知该如何修改达到我们的目的

"""
import datetime
import random
import re
import time

import requests
from lxml import etree


class DianpingComment:
    font_size = 14
    start_y = 23

    def __init__(self, shop_id, cookies, delay=7):
        self.shop_id = shop_id
        self._delay = delay
        self.font_dict = {}
        self._cookies = self._format_cookies(cookies)
        self._css_headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        }
        self._default_headers = {
            'Connection': 'keep-alive',
            'Host': 'www.dianping.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        }
        self._cur_request_url = 'http://www.dianping.com/shop/{}/review_all/p1'.format(shop_id)
        self._cur_request_css_url = 'http://www.dianping.com/shop/{}/'.format(shop_id)

    def _delay_func(self):
        delay_time = random.randint((self._delay - 2) * 10, (self._delay + 2) * 10) * 0.1
        print('睡一会', delay_time)
        time.sleep(delay_time)

    def _format_cookies(self, cookies):
        cookies = {cookie.split('=')[0]: cookie.split('=')[1]
                   for cookie in cookies.replace(' ', '').split(';')}
        return cookies

    def _get_css_link(self, url):
        """
            请求评论首页，获取css样式文件
        """
        res = requests.get(self._cur_request_css_url, headers=self._default_headers, cookies=self._cookies)
        html = res.text
        print('首页源码',html)
        # css_link = re.search(r'<link re.*?css.*?href="(.*?svgtextcss.*?)">', html)
        css_link = re.findall(r'<link rel="stylesheet" type="text/css" href="//s3plus.meituan.net/v1/(.*?)">', html)
        assert css_link
        css_link = 'http://s3plus.meituan.net/v1/' + css_link[0]
        print('css链接',css_link)
        return css_link



    def _get_font_dict_by_offset(self, url):
        """
            获取坐标偏移的文字字典, 会有最少两种形式的svg文件（目前只遇到两种）
        """
        res = requests.get(url,timeout=60)
        html = res.text
        font_dict = {}
        y_list = re.findall(r'd="M0 (\d+?) ', html)
        if y_list:
            font_list = re.findall(r'<textPath .*?>(.*?)<', html)
            for i, string in enumerate(font_list):
                y_offset = self.start_y - int(y_list[i])

                sub_font_dict = {}
                for j, font in enumerate(string):
                    x_offset = -j * self.font_size
                    sub_font_dict[x_offset] = font

                font_dict[y_offset] = sub_font_dict

        else:
            font_list = re.findall(r'<text.*?y="(.*?)">(.*?)<', html)

            for y, string in font_list:
                y_offset = self.start_y - int(y)
                sub_font_dict = {}
                for j, font in enumerate(string):
                    x_offset = -j * self.font_size
                    sub_font_dict[x_offset] = font

                font_dict[y_offset] = sub_font_dict
        print('字体字典',font_dict)
        return font_dict

    def _get_font_dict(self, url):
        """
            获取css样式对应文字的字典
        """
        print('解析svg成字典的css', url)
        res = requests.get(url, headers=self._css_headers,cookies=self._cookies,timeout=60)
        html = res.text

        background_image_link = re.findall(r'background-image: url\((.*?)\);', html)
        print('带有svg的链接', background_image_link)
        assert background_image_link
        background_image_link = 'http:' + background_image_link[0]
        html = re.sub(r'span.*?\}', '', html)
        group_offset_list = re.findall(r'\.([a-zA-Z0-9]{5,6}).*?round:(.*?)px (.*?)px;', html)  # css中的类
        print('css中class对应坐标', group_offset_list)
        font_dict_by_offset = self._get_font_dict_by_offset(background_image_link)  # svg得到这里面对应成字典
        print('解析svg成字典', font_dict_by_offset)


        for class_name, x_offset, y_offset in group_offset_list:
            y_offset = y_offset.replace('.0', '')
            x_offset = x_offset.replace('.0', '')
            # print(y_offset,x_offset)
            if font_dict_by_offset.get(int(y_offset)):
                self.font_dict[class_name] = font_dict_by_offset[int(y_offset)][int(x_offset)]

        return self.font_dict

    def _data_pipeline(self, data):
        """
            处理数据
        """
        print('最终数据:',data)

    def _parse_comment_page(self, doc):
        """
            解析评论页并提取数据
        """
        for li in doc.xpath('//*[@class="reviews-items"]/ul/li'):

            name = li.xpath('.//a[@class="name"]/text()')[0].strip('\n\r \t')
            try:
                star = li.xpath('.//span[contains(./@class, "sml-str")]/@class')[0]
                star = re.findall(r'sml-rank-stars sml-str(.*?) star', star)[0]
            except IndexError:
                star = 0
            time = li.xpath('.//span[@class="time"]/text()')[0].strip('\n\r \t')
            pics = []

            if li.xpath('.//*[@class="review-pictures"]/ul/li'):
                for pic in li.xpath('.//*[@class="review-pictures"]/ul/li'):
                    print(pic.xpath('.//a/@href'))
                    pics.append(pic.xpath('.//a/img/@data-big')[0])
            comment = ''.join(li.xpath('.//div[@class="review-words Hide"]/text()')).strip('\n\r \t')
            if not comment:
                comment = ''.join(li.xpath('.//div[@class="review-words"]/text()')).strip('\n\r \t')

            data = {
                'name': name,
                'comment': comment,
                'star': star,
                'pic': pics,
                'time': time,
            }
            self._data_pipeline(data)

    def _get_conment_page(self):  # 获得评论内容
        """
            请求评论页，并将<span></span>样式替换成文字
        """
        while self._cur_request_url:
            self._delay_func()
            print('[{now_time}] {msg}'.format(now_time=datetime.datetime.now(), msg=self._cur_request_url))
            res = requests.get(self._cur_request_url, headers=self._default_headers, cookies=self._cookies)
            html = res.text
            class_set = set()
            for span in re.findall(r'<span class="([a-zA-Z0-9]{5,6})"></span>', html):
                class_set.add(span)
            for class_name in class_set:
                html = re.sub('<span class="%s"></span>' % class_name, self._font_dict[class_name], html)
            doc = etree.HTML(html)
            self._parse_comment_page(doc)
            try:
                self._default_headers['Referer'] = self._cur_request_url
                next_page_url = 'http://www.dianping.com' + doc.xpath('.//a[@class="NextPage"]/@href')[0]
            except IndexError:
                next_page_url = None
            self._cur_request_url = next_page_url

    def run(self):
        self._css_link = self._get_css_link(self._cur_request_url)
        print('css 的连接', self._css_link)
        self._font_dict = self._get_font_dict(self._css_link)
        self._get_conment_page()


if __name__ == "__main__":
    COOKIES = '_lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=16dab7f8457c8-0c95c3c1c0c36a-67e1b3f-1fa400-16dab7f8458c8; _lxsdk=16dab7f8457c8-0c95c3c1c0c36a-67e1b3f-1fa400-16dab7f8458c8; _hc.v=d5a555f4-4153-1228-db57-eea5e1eb0d23.1570540325; cy=4; cye=guangzhou; s_ViewType=10; dper=cd1fb2c13ad994f5957f9ece4bc6c794a34295cc1f9cdaebd363116e5c9fa163038090ebefff860c8f6874ef62a76666cfc54aec557e8e37d8d62b4ec117b413861d7d81bb0739277b70e9b91d20d19dca272a889e02f0896cc360cb482757b7; ll=7fd06e815b796be3df069dec7836c3df; ua=aff; ctu=d18a6eea80cd3f693fa1b6bfc3d2611e1d93d0fd99be9db6fb2533f6a85af21d; _lxsdk_s=16dabc059d6-19e-058-8f8%7C%7C345'
    dp = DianpingComment('412xx21', cookies=COOKIES)
    dp.run()