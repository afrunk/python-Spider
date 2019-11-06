# IO
- [x] 文件夹
- [x] txt
- [x] json
- [x] csv
- [x] image
- [x] excle的批处理

## 文件夹的处理
```python
import os
os.getcwd()# 获取当前目录的文件夹
os.chcwd('D:/work') # 修改当前的文件夹的位置
os.makedirs('work2') # 新建目录
os.rmdir('work2') # 删除目录 目录必须为空
os.rename('fff.txt','fool.txt') # 重命名
os.remove('h.txt') # 删除文件


```

## txt
- 从txt中读取文件
```python
with open('exp.txt')as file_object:
    contents=file_object.read()
    print(contents)
    print(contents.rstrip)
```
- 访问不再绝对路径的文件
```python
 with open('file\\exp.txt')as file_object:
    contents=file_object.read()
    print(contents)
```
- 逐行读取txt文件
```python
filename='file\\exp.txt'
with open(filename)as file_object:
    for content in file_object:
        print(content.rstrip())#使用rstrip()方法实现空白行的删除
```
- 写入空txt文件:不覆盖写入
```python
with open('2016国家工作报告.txt','a',encoding='utf-8')as f:
    f.write(title+'\n')
    f.write(page)
    f.close()
```
## json
- 将数据存储到json文件中
```python
import json
numbers=[2,3,5,7,11,13]
file='numbers.json'
with open(file,'w')as f:
    json.dump(numbers,f)
```
上述的方法即可将数据写入到文件名为'numbers.json'文件中。
- 读取网页上json数据的方法
```python
data = {
            'gender': '2',
            'marry':'1',
            'page':'1'
        }
data['page']=i
url='http://www.lovewzly.com/api/user/pc/list/search?'
resp=requests.get(url,headers=headers,params=data)
if resp.status_code==200:
    data_json=resp.json()['data']['list']
    if len(data_json)>0:
        data_list=[]
        for data in data_json:
            data_list.append((
                data['username'], data['userid'], data['avatar'],
                data['height'], data['education'], data['province'],
                data['city'], data['birthdayyear'], data['gender'], data['monolog']
            ))
```
**data_json=resp.json()['data']['list']** 这个是最关键的语句。另外就是200的提示是成功400-500的提示是失败.
## csv
- 写入
```python
import requests
import xlwt
url_='http://www.htoption.cn/weixin/app/index.php?i=4&c=entry&do=getatmvol&m=ht_otc&mounth=2018-08-27'
url=input("请输入:")
# url_='http://www.htoption.cn/weixin/app/index.php?i=4&c=entry&do=getatmvol&m=ht_otc&mounth='+str(url)
response=requests.get(url_).json()
style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')
wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')#当前表的名字
for i in range(0,27):
    ws.write(i,2,response['AskVol'][i])
    ws.write(i,1,response['BidVol'][i])
    ws.write(i,0,response['ContractCode'][i])
    print(response['AskVol'][i])
    print(response['BidVol'][i])
    print(response['ContractCode'][i]+'\n')
wb.save(str(url)+'.xls')
```
- 读取
```python
import xlrd
from datetime import date,datetime
def read_excel():
    #打开文件
    workbook=xlrd.open_workbook(r'郭源潮.xls')
    #获取所有的sheet
    print(workbook.sheet_names())#['A Test Sheet']
    #根据sheet索引或者名称获取sheet内容
    sheet=workbook.sheet_by_index(0)#sheet索引从0开始
    # sheet=workbook.sheet_names('A Test Sheet')
    #sheet的名称，行数，列数
    print(sheet.name,sheet.nrows,sheet.ncols)
    #获取整行和整列的值（数组）
    rows=sheet.row_values(1)#获取第一行的内容
    cols=sheet.col_values(3)#获取第三列的内容
    print(rows[3])#获取第一行的第4个单元格的内容
    print(cols)
if __name__=='__main__':
    read_excel()
```
## image
- 批量保存图片
```python
def get_img(url,username):
    folder_path='./Photo'
    #这个也是可以赋值随时更改的
    if os.path.exists(folder_path)==False:
        os.makedirs(folder_path)
    res=requests.get(url,headerh=headers)
    # print(res)
    # if url[0:5]=='http:':
    #     img_url=url
    # filename=url.split('/')[-1]
    try:
        if 'png' in url:
            # print(url)
            fp = open('photo\\' +username+'.png', 'wb')
        else:
            fp = open('photo\\' + username + '.JPG', 'wb')
            # print(url)
        fp.write(res.content)
        print("Sucessful"+username)
        fp.close()
    except:
        print("Failed"+username)
        pass
```

## excle的批处理
```python
__author__ = 'afrunk'
__date__ = '2018/12/4 12:03'
import xlrd
import csv
import xlwt
style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')
wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet', cell_overwrite_ok=True)  # 当前表的名字 后面加上True才可避免被重复写入时的报错

import os
filelists=[]
filelists2=[]
def test():
    workbook2 = xlrd.open_workbook(r'888735_20181001-20181031_全部渠道_商品明细.xls')
    sheet2 = workbook2.sheet_by_index(0)
    pcols2 = sheet2.col_values(0)
    print(pcols2)

def test1():
    numh = 0.0
    for f in os.listdir('F:\Various competitions\Python_C接单群\MakeMoneyByMyself\Excle批处理\新建文件夹'):
        if "全部渠道" in f.split("_"):
            print("file:,",f)
            wb = xlrd.open_workbook(os.path.abspath(f))
            table = wb.sheet_by_index(0)
            for r in range(1,table.nrows):
                numh = r+ numh
            print('numh:',numh)

#生成总表
def filelist():
    # 获取到商品编码
    i = 0
    csv_reader = csv.reader(open('导出SPU.csv'))
    one = 0
    for row in csv_reader:
        # print(row[0])
        ws.write(i, 0, row[0])
        ws.write(i, 1, one)
        ws.write(i, 2, one)
        ws.write(i, 3, one)
        i += 1
    ws.write(0, 1, "历史下单总和")
    ws.write(0, 2, "历史访客总和")
    ws.write(0, 3, "7天访客数")
    wb.save("总表.xls")
    #批量处理excle文件
    for root,dirs,files in os.walk(".",topdown=False):
        for name in files:
            str=os.path.join(root,name)
            # if str.split(".")[-1]=='xls':
            if "全部渠道" in str.split("_"):
                # print(str)
                filelists.append(str)
            if "七天访客" in str.split("_"):
                filelists2.append(str)
    print(filelists)

    for m in range(0,len(filelists)):
        print(filelists[m])
        workbook=xlrd.open_workbook(filelists[m])
        workbook2 = xlrd.open_workbook(r'总表.xls')
        sheet = workbook.sheet_by_index(0)
        sheet2 = workbook2.sheet_by_index(0)

        cols2 = sheet2.col_values(0)#总表的第一列
        cols = sheet.col_values(0)#取值表的第一列

        xiadanzonghe =sheet2.col_values(1)
        lshifangke =sheet2.col_values(2)
        # qitianfangkeshu=sheet2.col_values(3)

        len1=sheet.nrows
        len2=sheet2.nrows
        for i in range(1,len1):
            for j in range(1,len2):
                if (cols[i] == cols2[j]):#编号相同则输出编号之后将总表的第二列相加
                    print(cols2[j])
                    xiadanzonghe[j] +=sheet.col_values(8)[i]

                    # print(xiadanzonghe[j])

                    print(sheet.col_values(8)[i])

                    lshifangke[j]+=sheet.col_values(3)[i]

                    print(lshifangke[j])

                    ws.write(j,2,lshifangke[j])

                    ws.write(j,1,xiadanzonghe[j])

                    # qitianfangkeshu = sheet2.col_values()
                    # ws.write(j, 3, qitianfangkeshu[j])
        wb.save('总表.xls')

    workbook1 = xlrd.open_workbook(filelists2[0])
    workbook22 = xlrd.open_workbook(r'总表.xls')
    sheet1 = workbook1.sheet_by_index(0)
    sheet22 = workbook22.sheet_by_index(0)
    print("开始七天的测试")
    print(filelists2[0])
    cols2 = sheet22.col_values(0)  # 总表的第一列
    cols = sheet1.col_values(0)  # 取值表的第一列
    qitianfangkeshu = sheet22.col_values(3)
    len11 = sheet1.nrows
    len22 = sheet22.nrows
    for k in range(1, len11):
        for y in range(1, len22):
            if (cols[k] == cols2[y]):  # 编号相同则输出编号之后将总表的第二列相加
                print(cols2[y])
                qitianfangkeshu[y] += sheet1.col_values(3)[k]
                ws.write(y, 3, qitianfangkeshu[y])
    wb.save('总表.xls')

def dierbufen():
    workbook22 = xlrd.open_workbook(r'总表.xls')
    sheet22 = workbook22.sheet_by_index(0)
    ws.write(0,0,"商品编码")
    ws.write(0,1,"上下架(上架/下架)")
    len=sheet22.nrows
    print(sheet22.col_values(1))
    for sm in range(1,len):
        ws.write(sm, 0, sheet22.col_values(0)[sm])
        if sheet22.col_values(1)[sm]==0 and sheet22.col_values(3)[sm]==0:
            ws.write(sm, 1, "下架")
            print(sheet22.col_values(0)[sm],"下架")
        else:
            ws.write(sm, 1, "上架")
            print(sheet22.col_values(0)[sm],"上架")
    wb.save("上下架表.xls")
if __name__=='__main__':

    # filelist()
    # test1()
    dierbufen()
```
