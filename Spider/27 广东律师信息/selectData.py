
"""
查询数据库中表得page列 然后统计某一数字出现得次数
计算列表中数字出现得频率 https://blog.csdn.net/ZhiAi_ZhengLiLi/article/details/99083398
"""
import pymysql
from collections import Counter
db = pymysql.connect(host='127.0.0.1',
                     port=3306,
                     user='root',
                     password='password',
                     db='world',
                     charset='utf8')
cursor = db.cursor()
sql = 'select page from guangzhou'
cursor.execute(sql)
dataList = cursor.fetchall()
dataList = Counter(dataList)
print(dataList)