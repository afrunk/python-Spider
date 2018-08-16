import requests
from lxml import etree
import time
from bs4 import BeautifulSoup
import xlwt
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}
import random


def get_url(url,j):
    res=requests.get(url,headers=headers)
    print(res)
    html = etree.HTML(res.text)
    infos = html.xpath('//ul[@class="note-list"]/li')#文章列表模块
    for info in infos:
        root = 'https://www.jianshu.com'
        url_path = root + info.xpath('div/a/@href')[0]
        print(url_path)#获取到每一个页面的详情页
        j += 1
        get_content(url_path,j)
    wb.save('简书交友之路-2.xls')

    rtime=float(random.randint(1,100))/20
    print("请让我休息%f秒..." % rtime)
    # time.sleep(rtime)


def get_content(url_path,j):
    res=requests.get(url_path,headers=headers).text
    html=BeautifulSoup(res,'lxml')
    # print(html)
    title=html.find_all("h1","title")[0].text#标题
    name=html.find("span","name").string#姓名
    content=html.find("div","show-content-free").text#内容
    zishu=html.find("span","publish-time").text#字数
    time=html.find('span','wordage').text#时间
    # print(title)
    # print(name)
    # print(content)
    # print(zishu)
    # print(time)
    ws.write(j, 0,title)
    ws.write(j, 1, name)
    ws.write(j, 2,zishu)
    ws.write(j, 3, time)
    ws.write(j, 4, content)
    print("正在保存第%d篇..."%j)



if __name__ == '__main__':
    style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')
    style1 = xlwt.easyxf(num_format_str='D-MMM-YY')
    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')  # 当前表的名字
    ws.write(0, 0, '标题')
    ws.write(0, 1, '作者')
    ws.write(0, 2, '字数')
    ws.write(0, 3, '时间')
    ws.write(0, 4, '内容')
    j=0
    urls = ['https://www.jianshu.com/c/bd38bd199ec6?order_by=added_at&page={}'.format(str(i)) for i in range(1,201)]#201
    for url in urls:
        # print(j)
        get_url(url,j)
        j+=10
        #这个地方是程序流程的问题，很多细节还是需要多练啊。如果不加这个的话for循环的j的值一直都是不变的。
