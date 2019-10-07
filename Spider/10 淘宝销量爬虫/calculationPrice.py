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

# 从数据库读取每家店铺的价格并进行查询单价和销量进行求和
def calculationPrice():
    shopNames=[] #店铺列表
    sales =[
        0,0,0,0,0,0,0,0,0,0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    ] #销售额列表 需要初始化 否则即便在下面进行定义也没用
    # try:
    # 获取数据库中店铺名的列表 进行遍历
    sql='select distinct shopname from taobao' # 去掉重复的店铺名
    cursor.execute(sql) # 执行sql语句 获取数据库数据
    for i in cursor.fetchall(): # 遍历店铺列表 注意需要使用fetchall()方法
        shopName=i[0] # 获取到的是一个列表 取出店铺名为第一个元素
        # print(shopName)
        shopNames.append(shopName) # 将店铺名添加到列表中方便后续我们查询每个店铺的数据进行遍历店铺名
    for i in range(0,len(shopNames)): # 遍历店铺名 方便查询该店铺下所有宝贝的销售数据
        print(sales[i]) # 输出当前店铺的销售额是否为0
        print(shopNames[i])
        sql_2="select * from taobao where shopname='%s'" %(shopNames[i]) # 查询所有该店铺下的所有数据
        cursor.execute(sql_2) # 执行sql语句
        for j in cursor.fetchall(): # 遍历查询到的嵌套列表
            price =j[1]  # 第二个元素是价格
            num=j[2] # 第三个元素是销售量
            print(price,num)
            sales[i] += price * num
    # except:
    #     print("Mysql语法错误！")

    print(shopNames,sales)
    # for i in range(len(shopNames)):
    #     print(shopNames[i],sales[i])
if __name__=='__main__':

    # 存入数据库 方便后续计算每月销售额
    # 换一家店铺需要修改的地方0（链接）
    # shopName = 'HM'
    # floge=getPages(shopName)
    # if floge==False:
    #     print("该店铺没有抓取完成！")
    #
    # 计算销售额部分
    calculationPrice()