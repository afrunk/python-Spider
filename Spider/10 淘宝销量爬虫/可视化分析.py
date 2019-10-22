"""
date:2019-10-7
author:afrunk
作用：读取数据库的某家店铺的数据进行销售额的计算

"""

# 链接数据库的部分
import pymysql
db = pymysql.connect(host='127.0.0.1',
                     port=3306,
                     user='root', #用户名
                     password='password', #密码
                     db='world', # 数据库名
                     charset='utf8')
cursor = db.cursor()

import matplotlib.pyplot as plt
import numpy as np
# 从数据库读取每家店铺的价格并进行查询单价和销量进行求和
def calculationPrice():
    shopNames=[] #店铺列表
    shuju_dapu_onlt=[]
    sales =[
        0,0,0,0,0,0,0,0,0,0,
    ] #销售额列表 需要初始化 否则即便在下面进行定义也没用
    # try:
    # 获取数据库中店铺名的列表 进行遍历
    sql='select distinct shopname from taobao' # 去掉重复的店铺名
    cursor.execute(sql) # 执行sql语句 获取数据库数据
    for i in cursor.fetchall(): # 遍历店铺列表 注意需要使用fetchall()方法
        shopName=i[0] # 获取到的是一个列表 取出店铺名为第一个元素
        # print(shopName)
        shopNames.append(shopName) # 将店铺名添加到列表中方便后续我们查询每个店铺的数据进行遍历店铺名
    # for i in range(0,len(shopNames)): # 遍历店铺名 方便查询该店铺下所有宝贝的销售数据
    # print(sales[i]) # 输出当前店铺的销售额是否为0
    # print(shopNames[i])
    shopNames='hm'
    sql_2="select * from taobao where shopname='%s'" %(shopNames ) # 查询所有该店铺下的所有数据
    cursor.execute(sql_2) # 执行sql语句
    shuju_dianpu = cursor.fetchall()
    for j in shuju_dianpu: # 遍历查询到的嵌套列表
        # print(j)
        shuju_dapu_onlt.append(j)
    # 销量最高的十个选项
    shuju_dapu_onlt.sort(key=lambda x: x[2], reverse=True) # 以价格来排序
    shujudeal_gao = shuju_dapu_onlt[:10]
    # print(shujudeal_gao)
    # print(shuju_dapu_onlt[0:10])
    jiagelist = []  # 价格列表
    xiaolList = []  # 销量列表
    for i in range(10):
        jiagelist.append(shujudeal_gao[i][0]) # 将价格添加进去
        xiaolList.append(shujudeal_gao[i][2]) # 将销量添加进去
    print(jiagelist)
    print(xiaolList)

    # 画柱状图
    # 创建一个点数为 8 x 6 的窗口, 并设置分辨率为 80像素/每英寸
    plt.figure(figsize=(8, 6), dpi=80)
    # 再创建一个规格为 1 x 1 的子图
    plt.subplot(1, 1, 1)
    # 柱子总数
    N = 10
    # 包含每个柱子对应值的序列
    values = xiaolList
    # 包含每个柱子下标的序列
    index = [1,2,3,4,5,6,7,8,9,10]
    # 柱子的宽度
    width = 0.35
    # 绘制柱状图, 每根柱子的颜色为紫罗兰色
    p2 = plt.bar(index, values, width, color="#87CEFA")
    # 设置横轴标签
    plt.xlabel('price ')
    # 设置纵轴标签
    plt.ylabel('num')
    # 添加标题
    plt.title('HM Sale')
    # 添加纵横轴的刻度
    plt.xticks(index, ('0593829', '0685816', '0561445', '0690950', '0554479', '0476315','0687635','0570004__3','0545396','0636586'))
    # plt.yticks(np.arange(0, 81, 10))
    # 添加图例
    plt.legend(loc="upper right")
    plt.show()

    # 销量最低的十个选项
    shujudeal_di = shuju_dapu_onlt[-10:]
    jiagelist_1 = []  # 价格列表
    xiaolList_1 = []  # 销量列表
    for i in range(10):
        jiagelist_1.append(shujudeal_di[i][1])  # 将价格添加进去
        xiaolList_1.append(shujudeal_di[i][0])  # 将销量添加进去
    print(jiagelist_1)
    print(xiaolList_1)



if __name__=='__main__':
    # 计算销售额部分
    calculationPrice()