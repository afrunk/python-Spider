import requests
from bs4 import BeautifulSoup
import time
import random
import xlwt

def get_page():
    style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')
    style1 = xlwt.easyxf(num_format_str='D-MMM-YY')
    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')  # 当前表的名字
    ws.write(0, 0, '小区')
    ws.write(0, 1, '价格')
    ws.write(0, 2, '区')
    ws.write(0, 3, '路')
    ws.write(0, 4, '建成时间')
    ws.write(0, 5, '在售套数')
    # city=['jn','cs','sh','bj','cd','sz','cq','lf','nj','sy','xa','zz','zh','dl','fs','hf','xm','hk']#济南 长沙 上海 北京 成都  深圳 重庆 廊坊 南京 沈阳 西安 郑州  珠海 大连 佛山  合肥 厦门 海口
    # for i in range(3,18):
    #     print('这是%s'%city[i])
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }
    j=1
    for c in range(1,2):
        # url_page='https://m.lianjia.com/'+str(city[c])+'/zufang/pg'
        try:
            for k in range(1,30):
                url='https://cs.lianjia.com/xiaoqu/pg'+str(k)+'/?_t=1'#第一页23户后面每一页30户 13468 585
                print(url)
                res=requests.get(url,headers=headers,timeout=5).text
                # print(res)
                html=BeautifulSoup(res,'lxml')
                try:
                    titles=html.find_all('div','title')#小区名字
                    totalPrice=html.find_all('div','totalPrice')#价格
                    positions=html.find_all('div','positionInfo')#地点
                    zaishous=html.find_all('a','totalSellCount')#在售套数
                    for i in range(1,31):#我们从提取的div的class为title的标签中提取到了从第二个标签到31个标签都是小区名字
                        a=titles[i].text.split()#通过split将空格去掉 存入列表
                        total=totalPrice[i-1].text.split()
                        position=positions[i-1].text.split(maxsplit=3)#通过split和maxspit函数将字符串分割成四个部分，取出来我们需要的三个部分
                        zaishou=zaishous[i-1].text.split()
                        print(a[0])#小区名字
                        print(total[0])#价格
                        print(position[0]+position[1]+position[3])#分别是区 路 建成时间
                        print(zaishou[0])#在售套数

                        ws.write(j, 0, a[0])
                        ws.write(j, 1, total[0])
                        ws.write(j, 2, position[0])
                        ws.write(j, 3, position[1])
                        ws.write(j, 4, position[3])
                        ws.write(j, 5, zaishou[0])
                        j=j+1
                    wb.save('链家网小区-长沙.xls')
                    rtime=float(random.randint(1,100)/20)
                    print("请让我休息%d秒钟"%rtime)
                    print("接下来将要爬取长沙第%d页"%(k+1))
                    time.sleep(rtime)
                except:
                    pass
        except:
            pass



    # print(j)

if __name__=='__main__':
    get_page()