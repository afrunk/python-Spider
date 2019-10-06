
import requests
import xlwt
import time
import xlrd
from xlutils.copy import copy
from bs4 import BeautifulSoup


headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-HK,zh;q=0.9,zh-CN;q=0.8,en;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Host':'www.whalebj.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
# style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')
# style1 = xlwt.easyxf(num_format_str='D-MMM-YY')
# wb = xlwt.Workbook('data.xls')
# ws = wb.add_sheet('data')  # 当前表的名字
# ws.write(0, 0 ,label="时间")
# ws.write(0, 1, label="场内待运车辆数")
# ws.write(0, 2, label="前半小时进程车辆数")
# ws.write(0, 3, label="前半小时离场车辆数")

# wb.save('data.xls')
for i in range(1,10000):
    try:
        style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')
        style1 = xlwt.easyxf(num_format_str='D-MMM-YY')
        workbook = xlrd.open_workbook('data.xls')  # 打开工作簿
        sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
        worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
        rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
        new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
        new_worksheet = new_workbook.get_sheet(0)
        url='http://www.whalebj.com/xzjc/default.aspx'
        html = requests.get(url,headers=headers).text
        soup = BeautifulSoup(html,'lxml')
        # print(soup)
        sp = soup.find('span').text.replace('郑州机场出租车秩序管理站 截止目前为止','').replace('前半小时进场车辆数为','').replace('场内待运车辆数为','').replace('辆(场内待运较多)； 前半小时进场车辆数为','').replace('辆； 前半小时离场车辆数为','').replace('辆；','').replace('\xa0','')
        print(sp)
        list = sp.split('：')
        print(list)
        new_worksheet.write(i, 0,label=list[0])
        new_worksheet.write(i, 1,label=list[1])
        new_worksheet.write(i, 2,label=list[2])
        new_worksheet.write(i, 3,label=list[3])
        new_workbook.save('data.xls')
        time.sleep(15)
    except:
        pass