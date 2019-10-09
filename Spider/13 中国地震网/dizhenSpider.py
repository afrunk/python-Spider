"""
抓取地震的信息写入text
目标网站链接：http://www.ceic.ac.cn/speedsearch?time=1
json数据抓取链接：
    - http://www.ceic.ac.cn/ajax/speedsearch?num=1&&page=1&&callback=jQuery1800006901831796154223_1570542282133&_=1570545914834  24小时内地震数据
    - http://www.ceic.ac.cn/ajax/speedsearch?num=2&&page=1&&callback=jQuery1800006901831796154223_1570542282133&_=1570545944509  48小时内地震数据
    - http://www.ceic.ac.cn/ajax/speedsearch?num=3&&page=1&&callback=jQuery1800006901831796154223_1570542282133&_=1570545961203  七天内地震数据
    - http://www.ceic.ac.cn/ajax/speedsearch?num=4&&page=1&&callback=jQuery1800006901831796154223_1570542282133&_=1570545980766  最近30天内地震数据
    - http://www.ceic.ac.cn/ajax/speedsearch?num=6&&page=1&&callback=jQuery1800006901831796154223_1570542282133&_=1570546000818  最近一年内地震数据

需要字段:经纬度 位置 utc时间 震级
写入到txt,按照时间顺序来写 重复的不要

技术点：
    - 参考10086爬虫将json字符串转换成字典
    - 读写txt
    - 定时爬取

"""

import requests
import time
import random

def GetContent():
    data_list =[]
    url='http://www.ceic.ac.cn/ajax/speedsearch?num=1&&page=1&&callback=jQuery1800006901831796154223_1570542282133&_=1570545914834'
    html = requests.get(url).text.replace('})','}').replace('jQuery1800006901831796154223_1570542282133(','') # 获取目标文件
    # print(html)#仍然是字符串形式 需要进行强制类型转换
    global null
    null = ''
    # 转换成dict
    content = eval(html)
    shujus =content['shuju'] # 转换成字典形式之后直接读取即可

    # for循环遍历列表读取我们所需要的数据 拼接成列表写入txt
    for shuju in shujus:
        # print(shuju)
        EPI_LAT = shuju['EPI_LAT'] #纬度
        EPI_LON = shuju['EPI_LON'] #经度
        LOCATION_C = shuju['LOCATION_C'] #位置
        O_TIME = shuju['O_TIME'] # UTC时间
        M =shuju['M'] # 震级
        data_list.append((EPI_LAT,EPI_LON,LOCATION_C,O_TIME,M)) # 以嵌套列表的形式写入txt
    # print(data_list) # 输出当前抓取的列表的数据

    # r 读  w 写 a 追加
    # r+ 可读可写 w+ 可读可写 a+ 可追加可读 这三者 文件不存在自动创建 如果对应的是二进制文件  加b即可
    text_new=[] # 存放当前txt已经存在的数据
    with open('data.txt', 'r+', encoding='UTF-8') as f:  # 打开文本
        text_new = f.readlines()  # 读取文本数据存放到列表中
        # print(text_new)

    with open('data.txt', 'a+', encoding='utf-8') as f: # a+才可追加 不知为何
        for data in data_list :
            biaozhi = 1 # 标识符
            # for 循环判断是否存在
            for data in text_new : # for循环当前txt数据中是否已经存在该数据
                print("该地震数据已存在")
                biaozhi = 0 # 如果存在则将标识符修改为0
            if biaozhi == 1:#只有当标识符为1时才写入到txt
                print(data)
                f.write(str(data) + '\n') # 写入txt必须是str类型
    f.close()#全部写入之后关闭



if __name__=='__main__':
    while(1): # 一直运行
        GetContent()
        date_test=random.randint(1,5) # 随机暂停多少秒后抓取 也可以直接修改成一个固定的值
        print("{}秒后将再次抓取数据请稍等：".format(date_test))
        time.sleep(date_test)

