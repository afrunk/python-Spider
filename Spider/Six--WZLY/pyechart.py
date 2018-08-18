import pandas as pd
import numpy as np
import sys
import os
from  pyecharts  import Bar
from pyecharts import Pie
from pyecharts import Funnel
from pyecharts import Radar
# 身高范围
height_interval = ['140cm', '150cm', '160cm', '170cm', '180cm']

raw_data = pd.read_excel('我主良缘.xls',header=0,skiprows=0)
# print(raw_data['height'])

def analysis_height(data):
    height_data=data['height']
    height = (height_data.loc[(height_data > 140) & (height_data < 200)]).value_counts().sort_index()
    height_count = [0, 0, 0, 0, 0]
    for h in range(0, len(height)):
        if 140 <= height.index[h] < 150:
            height_count[0] += height.values[h]
        elif 150 <= height.index[h] < 160:
            height_count[1] += height.values[h]
        elif 160 <= height.index[h] < 170:
            height_count[2] += height.values[h]
        elif 170 <= height.index[h] < 180:
            height_count[3] += height.values[h]
        elif 180 <= height.index[h] < 190:
            height_count[4] += height.values[h]
    print(height_count)
    return height_count


def draw_height_bar(data):
    bar = Bar("妹子身高分布柱状图")
    bar.use_theme('dark')
    bar.add("妹子身高", height_interval, data, bar_category_gap=0, is_random=True, )
    bar.render()
    return bar

# 绘制身高分布饼图
def draw_height_pie(data):
    pie = Pie("妹子身高分布饼图-圆环图",title_pos='center')
    pie.add("", height_interval, data, radius=[40, 75], label_text_color=None,
        is_label_show=True, legend_orient='vertical',is_random=True,
        legend_pos='left')
    pie.render()
    return pie

# draw_height_bar(analysis_height(raw_data))
# draw_height_pie(analysis_height(raw_data))

edu_interval = ['本科', '大专', '高中', '中专', '初中', '硕士', '博士', '院士']  # 学历范围

# 分析学历
def analysis_edu(data):
    print(data['education'].value_counts().values)
    return data['education'].value_counts().values


# 学历漏斗图
def draw_edu_funnel(data):
    funnel = Funnel("妹子学历分布漏斗图",title_top='center')
    funnel.add("学历", edu_interval, data, is_label_show=True,label_pos="inside", label_text_color="#fff",is_random=True )
    funnel.render()
    return funnel

# draw_edu_funnel(analysis_edu(raw_data))




# 学历范围
age_interval = [
    ('18-25', 8000), ('26-30', 8000), ('31-40', 8000),
    ('41-50', 8000), ('50以上', 8000),
]

# 分析年龄
def analysis_age(data):
    age_data = data['birthdayyear']
    age = (age_data.loc[(age_data >= 1956) & (age_data <= 2000)]).value_counts().sort_index()
    age_count = [0, 0, 0, 0, 0]
    for h in range(0, len(age)):
        if 1993 <= age.index[h] <= 2000:
            age_count[0] += age.values[h]
        elif 1988 <= age.index[h] <= 1992:
            age_count[1] += age.values[h]
        elif 1978 <= age.index[h] <= 1987:
            age_count[2] += age.values[h]
        elif 1968 <= age.index[h] <= 1977:
            age_count[3] += age.values[h]
        elif age.index[h] < 1968:
            age_count[4] += age.values[h]
    print(age_count)
    return age_count

# 年龄雷达图
def draw_age_radar(data):
    radar = Radar("妹子年龄分布雷达图")
    radar.config(age_interval)
    radar.add("年龄段", data, is_area_show=False,legend_selectedmode='single')
    radar.render()
    # return radar

# draw_age_radar([analysis_age(raw_data)])

from pyecharts import Geo


# 分析城市分布
def analysis_city(data):
    city_data = data['city'].value_counts()
    city_list = []
    for city in range(0, len(city_data)):
        if city_data.values[city] > 10:
            city_list.append((city_data.index[city], city_data.values[city]))
    return city_list

# 城市分布地图
def draw_city_geo(data):
    geo = Geo("全国妹子所在地分布", "制作人：afrunk", title_color="#fff",
              title_pos="left", width=1200,
              height=600, background_color='#404a59')
    attr, value = geo.cast(data)
    geo.add("", attr, value, visual_range=[10, 2500],  visual_text_color="#fff",
            symbol_size=15, is_visualmap=True)
    return geo

# draw_city_geo(analysis_city(raw_data))

from pyecharts import WordCloud
import re
import jieba as jb
from collections import Counter


# 过滤标点符号正则
word_pattern = re.compile('[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？“”、~@#￥%……&*（）(\d+)]+')
# 过滤无用词
exclude_words = [
            '一辈子', '不相离', '另一半', '业余时间', '性格特点', '茫茫人海', '男朋友', '找对象',
            '谈恋爱', '有时候', '女孩子', '哈哈哈', '加微信', '兴趣爱好',
            '是因为', '不良嗜好', '男孩子', '为什么', '没关系', '不介意',
            '没什么', '交朋友', '大大咧咧', '大富大贵', '联系方式', '打招呼',
            '有意者', '晚一点', '哈哈哈', '以上学历', '是不是', '给我发',
            '不怎么', '第一次', '越来越', '遇一人', '择一人', '无数次',
            '符合条件', '什么样', '全世界', '比较简单', '浪费时间', '不知不觉',
            '有没有', '寻寻觅觅', '自我介绍', '请勿打扰', '差不多', '不在乎', '看起来',
            '一点点', '陪你到', '这么久', '看清楚', '身高体重', '比较慢', '比较忙',
            '多一点', '小女生', '土生土长', '发消息', '最合适'
        ]

# 词频分布
def analysis_word(data):
    word_data = data['monolog'].value_counts()
    word_list = []
    for word in range(0, len(word_data)):
        if word_data.values[word] == 1:
            word_list.append(word_data.index[word])
    return word_list

# 交友宣言词云
def draw_word_wc(name, count):
    wc = WordCloud(width=900, height=720)
    wc.add("", name, count, word_size_range=[20, 100], shape='diamond')
    # wc.render()
    return wc

word_result = word_pattern.sub("", ''.join(analysis_word(raw_data)))
# Jieba分词
words = [word for word in jb.cut(word_result, cut_all=False) if len(word) >= 3]
# 遍历过滤无用词
for i in range(0, len(words)):
    if words[i] in exclude_words:
        words[i] = None
filter_list = list(filter(lambda t: t is not None, words))
data = r' '.join(filter_list)
# 词频统计
c = Counter(filter_list)
word_name = []  # 词
word_count = []  # 词频
for word_freq in c.most_common(100):
    word, freq = word_freq
    word_name.append(word)
    word_count.append(freq)

print(word_name)

draw_word_wc(word_name, word_count)