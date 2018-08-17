'''
@author=afrunk
time=2018-8-17
'''
import requests
import xlwt
import json
import time
import random
import os
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'cookie':'Hm_lvt_ad61b7e39c2050f6b2b13390d4decf4f=1534475898; Hm_lpvt_ad61b7e39c2050f6b2b13390d4decf4f=1534500204',
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-HK,zh;q=0.9,zh-CN;q=0.8,en;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
    'Connection':'keep-alive',
    'Host':'www.lovewzly.com',
    'Referer':'http://www.lovewzly.com/jiaoyou.html',
    'X-Requested-With':'XMLHttpRequest'
}

def get_json():
    style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')
    style1 = xlwt.easyxf(num_format_str='D-MMM-YY')
    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')  # 当前表的名字
    ws.write(0, 0, 'username')
    ws.write(0, 1, 'userid')
    ws.write(0, 2, 'avatar')
    ws.write(0, 3, 'height')
    ws.write(0, 4, 'education')
    ws.write(0, 5, 'province')
    ws.write(0, 6, 'city')
    ws.write(0, 7, 'birthdayyear')
    ws.write(0,8,'gender')
    ws.write(0,9,'monolog')
    j=1
    for i in range(363,730):#730
        try:
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
                        ws.write(j, 0,data['username'])
                        ws.write(j, 1,data['userid'])
                        ws.write(j, 2, data['avatar'])
                        ws.write(j, 3,data['height'])
                        ws.write(j, 4,data['education'])
                        ws.write(j, 5, data['province'])
                        ws.write(j, 6, data['city'])
                        ws.write(j, 7,data['birthdayyear'])
                        ws.write(j,8, data['gender'])
                        ws.write(j,9, data['monolog'])
                        urls=data['avatar']
                        username=data['username']
                        get_img(urls,username)
                        j+=1
            # print(data_list)
        except:
            pass
        wb.save('我主良缘-3.xls')
        rtime = float(5+random.randint(1, 50) / 20)
        print("请让我休息%d秒钟" % rtime)
        print("接下来将要爬取API第%d页" % (i + 1))
        time.sleep(rtime)

def get_img(url,username):
    folder_path='./Photo'
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



if __name__=='__main__':
    get_json()