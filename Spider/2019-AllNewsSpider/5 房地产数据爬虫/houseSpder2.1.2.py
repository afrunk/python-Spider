"""
2.1.1 现售 数据入库看看速度会不会快一些
快很多 尝试着用这个直接跑一下
表名：houseSpider2 第三页开始
思路：
1. 获取公示楼盘的信息列表 post
2. 提取信息列表中的id和cid https://cucc.tazzfdc.com/reisPub/pub/projectInfo?id=7227&cid=1601486 get请求
3. 进去具体的楼盘 获取房间url列表 https://cucc.tazzfdc.com/reisPub/pub/loupan?buildingId=107492 get请求
4. 使用房间url列表进入具体的房间信息：https://cucc.tazzfdc.com/reisPub/pub/houseInfo?houseId=370911:4118962 get请求

"""
# 引入地库
import requests
from bs4 import BeautifulSoup
import re
import xlrd
import xlwt
from xlutils.copy import copy # 修改excle表格库
from multiprocessing import Pool # 多线程库
import time
import pymysql
db = pymysql.connect(host='127.0.0.1',
                     port=3306,
                     user='root',
                     password='password',
                     db='world',
                     charset='utf8')
cursor = db.cursor()
# 获取预售项目id和cid
def GetpreSaleBuildingStatist(ss):
    id=[] # 存放10个id
    cid=[] # 存放10个cid
    # url='https://cucc.tazzfdc.com/reisPub/pub/preSaleBuildingStatist' # 预售
    url ='https://cucc.tazzfdc.com/reisPub/pub/saleBuildingStatist' # 现售
    headers ={
        'Accept'
    }
    data = {
        'name':'',
        'no':'',
        'developer':'',
        'pageNo':'', # 页码
        'status':''
    }
    data['pageNo'] = ss
    print(data)
    # con = requests.post(url=url,data=data)
    con = requests.post(url=url,data=data).text
    # print(con)
    content_bs = BeautifulSoup(con,'lxml')
    tbody_tr= content_bs.find_all('a')# 匹配所有a标签
    # print(tbody_tr)
    tbody_tr_real=tbody_tr[2:12]# 切片每页只有10个属于项目的链接 一般都是固定
    # print(tbody_tr_real)
    for tr_a in tbody_tr_real:
        # print(tr_a)
    #     onclick = tr_a.text # 项目名
    #     # print(onclick)
        t=re.findall(r'\d+',str(tr_a))[:2]# id 和 cid 有的时候项目名中有数字 所以切片 只要前2个数字
        # print(t)
        id.append(t[0]) # 将id添加到列表中传给获取房屋状态的函数
        cid.append(t[1]) # 将cid添加到列表中传给获取房屋状态的函数
    # print(id,cid)
    return id,cid



# 进入项目获取房屋状态链接
def getHouseUrl(ss):
    urlRealList=[]
    id,cid = GetpreSaleBuildingStatist(ss)
    # print(id)
    for i in range(10):
        print("这是第 {} 个项目".format(i))
        url='https://cucc.tazzfdc.com/reisPub/pub/projectInfo?id={}&cid={}'.format(id[i],cid[i]) # 使用id和cid拼接请求url
        print("起始项目链接: "+url)
        con = requests.get(url).text
        # print(con)
        keyword=BeautifulSoup(con,'lxml')
        # # print(keyword)
        # # 使用find_all 参数来匹配标签 ，而find_all 返回的是一个列表 所以提取第一个 然后再获取 onclick 参数
        a_s = keyword.find_all(href=re.compile("javascript")) # 有的页面不止一个 房屋具体信息页
        # print(a_s)
        # # 获取都onclick参数之后替换掉我们所不需要的字符部分 然后拼接成我们想要的链接
        for a in a_s:
            url_rael='https://cucc.tazzfdc.com'+a.get('onclick').replace("$.openNewContent(this,'","").replace("');","")
            print(url_rael)
            urlRealList.append(url_rael)
        # #返回具体项目的所有具体户型的信息列表页面
        # print("该项目下有几个楼："+str(len(urlRealList)))
    return urlRealList

# 获取具体户型的信息列表页面中的链接列表
def getRealHouseUrlList(ss):
    # 定义一个该项目的所有具体户型的url列表 存入之后方便抓取然后存入excle
    houseInfoUrlList =[]
    try:
        urlRealList = getHouseUrl(ss)
        # urlRealList =['https://cucc.tazzfdc.com/reisPub/pub/loupan?buildingId=107493']
        # print(urlRealList)
        for url_real in urlRealList:
            print("某栋楼的具体信息链接: "+url_real)
            con = requests.get(url_real).text
            # print(con)
            content = BeautifulSoup(con, 'lxml')
            # # print(content)
            # # 获取层数 tr
            tbody_real = content.find_all('tbody',class_='houses')[0]
            # print(tbody_real)
            trs=tbody_real.find_all('tr',align='center')# 获取trs
            # print(trs)
            # print(len(trs))
            for tr in trs: # 获取tr
                tds = tr.find_all('td') # 获取td标签
                # print(tds)
                del tds[0]
                for td in tds:
            #         # 有些td 没有a 但是仍然存在 所以加一个try避免报错停止
                    try:
                        test=td.find('a')
            #             # 拼接成具体的
                        houseUrl='https://cucc.tazzfdc.com/'+test.get('href')
                        # print(houseUrl)
                        houseInfoUrlList.append(houseUrl)
                    except(Exception, BaseException) as e:
                        print(e)
    except(Exception,BaseException) as e:
        print(e)
    return houseInfoUrlList

# 获取具体的信息 然后追加写入excle
def getHouseInfo(ss):
    # 获取项目下得具体户型得信息链接

    houseInfoUrlList = getRealHouseUrlList(ss)
    # houseInfoUrlList = 'https://cucc.tazzfdc.com/reisPub/pub/houseInfo?houseId=370911:4119018'
    print("该十个项目地具体户型链接有:"+str(len(houseInfoUrlList)))

    # 遍历整个列表取出来
    for houseInfoUrl in houseInfoUrlList:
        contentInfo = []
        con = requests.get(houseInfoUrl).text
        # print(con)
        content = BeautifulSoup(con, 'lxml')
        # print(content)
        trs = content.find_all('tr')
        # print(trs)
        for tr in trs:
            # print(tr)
            tds = tr.find_all('td')
            # print(tds)
            for i in range(1,4,2):
            # for i in range():
            #     print(tds[i].text)
                contentInfo.append(tds[i].text)
        print(contentInfo)
        sql_2 = """
                        INSERT IGNORE INTO houseSpider2 (xiangmuming,fangwuzuoluo,fanghao,zhuanghao,jianzhumianji,jiegou,fentanmianji,taoneimianji,suozaiceng,yongtu,zhuangxiu,huxing)VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}' )
                            """ \
            .format(
            pymysql.escape_string(contentInfo[0]),
            pymysql.escape_string(contentInfo[1]),
            pymysql.escape_string(contentInfo[2]),
            pymysql.escape_string(contentInfo[3]),
            pymysql.escape_string(contentInfo[4]),
            pymysql.escape_string(contentInfo[5]),
            pymysql.escape_string(contentInfo[6]),
            pymysql.escape_string(contentInfo[7]),
            pymysql.escape_string(contentInfo[8]),
            pymysql.escape_string(contentInfo[9]),
            pymysql.escape_string(contentInfo[10]),
            pymysql.escape_string(contentInfo[11])
        )
        # print(sql_2)
        cursor.execute(sql_2)  # 执行命令
        db.commit()  # 提交事务

# 测试插入excle是否有问题
def test():
    contentInfo=['硕园经典', '岱岳区泮河大街以南、泮河以东硕园经典4号楼2单元2404室', '2404', '4号楼', '109.84', '钢筋混凝土结构', '26.27', '83.57', '24', '住宅', '', '']
    workbook = xlrd.open_workbook('data.xlsx')  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows + 1  # 获取表格中已存在的数据的行数
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)
    for i in range(0, len(contentInfo)):
        new_worksheet.write(rows_old, i, label=contentInfo[i])
    new_workbook.save('data.xlsx')

if __name__=='__main__':

    # 单线程
    start_ = time.time()
    for i in range(3,10): # 70页
        #ok 1-2024 2-3400 表格没跑完 4700
        # mysql 3-1591 4-1898 5-2647
        # try:
        getHouseInfo(i)
        # except:
        #     with open('log.txt', 'a', encoding='utf-8') as f:
        #         content = "现售没有完成:%s" % (str(i))
        #         print(content)
        #         f.write(str(content) + '\n')
        #         f.close()
    end_ = time.time()
    print('1进程爬虫耗时:', end_ - start_)

    # getRealHouseUrlList(1)