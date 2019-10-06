'''
去哪儿评价
get

https://piao.qunar.com/ticket/detailLight/sightCommentList.json?sightId=457472&index=1&page=1&pageSize=10&tagType=0
Request Method: GET
比起携程的更简单 request get 修改链接即可 在代码中有注释 相对较简单


'''

import requests
import json
import pymysql
db = pymysql.connect(host='127.0.0.1',
                     port=3306,
                     user='root',
                     password='password',
                     db='world',
                     charset='utf8')
cursor = db.cursor()
def get_info():
    for i in range(1,500): #500*10
        # url='https://piao.qunar.com/ticket/detailLight/sightCommentList.json?sightId=457472&index={}&page={}&pageSize=10&tagType=0'.format(i,i) # 迪士尼
        url='https://piao.qunar.com/ticket/detailLight/sightCommentList.json?sightId=4287&index={}&page={}&pageSize=10&tagType=0'.format(i,i) #欢乐谷
        print(url)
        con = requests.get(url).text
        # 读取 json格式数据
        # 参考链接：https://www.runoob.com/python/python-json.html
        con = json.loads(con)
        # 读取我们地data数据部分
        commentLists=con['data']['commentList'] # 评论列表
        for comment in commentLists:
            print(comment['author']) # 用户名
            print(comment['content']) # 内容
            print(comment['date']) # # 时间
            print(comment['score']) # 评分
            print('\n')

            name_1 = comment['author']  # 用户名
            score = comment['score']  # 评分
            content_1 =comment['content'] # 具体评价内容
            date_1 = comment['date'] # 具体评价时间
            # 表分别是 huanleguqunaer  dishiniqunaer 表结构一致
            sql_2 = """
                            INSERT IGNORE INTO huanleguqunaer (score,name_1,content_1,date_1)VALUES('{}','{}','{}','{}') 
                            """ \
                .format(
                score,
                pymysql.escape_string(name_1),
                pymysql.escape_string(content_1),
                pymysql.escape_string(date_1),
            )  # pymysql.escape_string(commentOrderInfo)
            print(sql_2)
            cursor.execute(sql_2)
            # # 执行命令
            db.commit()  # 提交事务

if __name__=='__main__':
    get_info()