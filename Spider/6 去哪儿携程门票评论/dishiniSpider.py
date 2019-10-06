'''
#参考链接：https://blog.csdn.net/qq_34774456/article/details/89885296

难点：
- 将json转换成字典形式
- 将数据存入数据库

所有的评论都是post 一个链接 不同的景点修改data里的cid值
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


def get_all_info(i):

    headers ={
        'access-control-allow-credentials':'true',
        'access-control-allow-origin':'https://piao.ctrip.com',
        'access-control-expose-headers':'RootMessageId, x-service-call',
        'clogging_trace_id':'3727138847182768202',
        'content-encoding':'gzip',
        'content-type':'application/json;charset=UTF-8',
        'date':'Thu, 03 Oct 2019 10:44:07 GMT',
        'rootmessageid':'921812-0a1c5384-436138-2702716',
        'server':'nginx/1.14.1',
        'soa20-service-latency':'100',
        'status':'200',
        'vary':'accept-encoding',
        'x-ctrip-soa2-route':'default-route-rule',
        'x-ctrip-soa2-route-group':'default-group-key',
        'x-ctrip-soa2-route-operation':'viewcommentlist',
        'x-ctrip-soa2-route-url':'http://10.28.105.123:8080/ttd-mobile-restfulapi/api/',
        'x-gate':'ctrip-gate',
        'x-gate-instance':'unknown',
        'x-gate-root-id':'921812-0a1c5384-436138-2702716',
        'x-originating-url':'http://sec-m.ctrip.com/restapi/soa2/12530/json/viewCommentList?_fxpcqlniredt=09031077211458006673',
        'x-service-call':'0.106'
    }

    data ={
        "pageid":'10650000804',
        "viewid":'1412255',
        "tagid":'0',
        "pagenum":'', # 极限就是61
        "pagesize":'10',
        "contentType":"json",
        "head":{"appid":"100013776","cid":"09031077211458006673","ctok":"","cver":"1.0","lang":"01","sid":"8888","syscode":"09","auth":"",
        "extension":[{"name":"protocal","value":"https"}]
                }
        ,"ver":"7.10.3.0319180000"}
    # 传进来得值进行传入data
    data['pagenum']=i
    data = json.dumps(data).encode(encoding='gb18030') # 未添加改部分即报错 不可获取到数据

    # 欢乐谷 https://sec-m.ctrip.com/restapi/soa2/12530/json/viewCommentList?_fxpcqlniredt=09031077211458006673
    con = requests.post("https://sec-m.ctrip.com/restapi/soa2/12530/json/viewCommentList?_fxpcqlniredt=09031077211458006673",headers=headers,data=data)


    # print(con.encoding)

    # 将字符串转换成字典形式
    # global false, null, true
    # false = null = true = ''

    # 直接使用 json方法转换成json格式
    '''
    # 这里存在一个问题 编码的问题  解决该问题的方法是修改pymysql下的编码 D:\anaconda\Lib\site-packages\pymysql\connections.py
    # 参考链接为：https://blog.csdn.net/weixin_34314962/article/details/92490539
    if data is not None:
    if encoding is not None:
        data = data.decode(encoding,'ignore') # 添加,'ignore'
    if DEBUG: print("DEBUG: DATA = ", data)
    if converter is not None:
        data = converter(data)
    '''
    content = json.loads(con.content.decode("utf8","ignore"))

    OnePageInfos =content['data']['comments']

    name_1 ='' # 用户名
    score = ''  # 评分
    content_1 = ''  # 具体评价内容
    date_1 = ''  # 具体评价时间
    commentOrderInfo = ''  # 购票类型


    for onePageInfo in OnePageInfos:
        # print(onePageInfo)
        name_1 = onePageInfo['uid']# 用户名
        score = onePageInfo['score'] # 评分
        content_1 = onePageInfo['content'] # 具体评价内容
        date_1 = onePageInfo['date'] # 具体评价时间
        commentOrderInfo = onePageInfo['commentOrderInfo'] # 购票类型

        print(score)
        print(name_1)
        print(content_1)
        print(date_1)
        print(commentOrderInfo)

        # try:
        # 表名不能有 - 否则会报错 1064
        sql_2 = """
                INSERT IGNORE INTO dishinixiec (score,name_1,content_1,date_1,commentOrderInfo)VALUES('{}','{}','{}','{}','{}')
                """ \
            .format(
                    pymysql.escape_string(score),
                    pymysql.escape_string(name_1),
                    pymysql.escape_string(content_1),
                    pymysql.escape_string(date_1),
                    pymysql.escape_string(commentOrderInfo))#pymysql.escape_string(commentOrderInfo)
        print(sql_2)
        cursor.execute(sql_2)
        # # 执行命令
        db.commit()  # 提交事务

        # except:
        #     print("当前sql语句出错")


if __name__=='__main__':
    for i in range(1,300):
        get_all_info(i)