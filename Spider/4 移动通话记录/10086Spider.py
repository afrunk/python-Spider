"""
移动爬虫
爬取通话记录存入mysqlsh数据库
电话：15151531962
密保：476053

"""
# 链接数据库 切换时候修改db即可
import pymysql
db = pymysql.connect(host='127.0.0.1',
                     port=3306,
                     user='root',
                     password='password',
                     db='world',
                     charset='utf8')
cursor = db.cursor()
import requests
headers ={
    'Accept':'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-HK,zh;q=0.9,zh-CN;q=0.8,en;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
    'Connection':'keep-alive',
    'Content-Type':'*',
    'Cookie':'inx=myorders; inx2=returnorderqry; ssologinprovince=250; CmLocation=250|512; collect_id=kr85l05klhe9fps34v0e4rp6kp4cdtso; CmProvid=bj; defaultloginuser_p=izr73fwOUuimT7R+YElqbvQdIEKrmWCpu49KY4pe7cglQnOlbxDN0nqcpR0yt5wiIU6Mjw2cFGiqccIsrNqK/CMTsRVyT13VInOal6sQlEadt/KkBQHpnISURF30i3h1NIChi3gihwmhVzzoGOae/T4++cBy6mWhB3ovCk/XxgaNwSyqpJkEqg/LuT1QHsyO; verifyCode=50374e3a8b3594cc606cae9ba4424f3a86d0f8bf; is_login=true; jsessionid-echd-cpt-cmcc-jt=0B9A1A8D18A95793A95860698873B204; lgToken=d8d0a3168c984c8bbba589e60e27ac69; CaptchaCode=HtTtFN; rdmdmd5=A52C537D27C9AD87DE277F5194BF0463; captchatype=z; sendflag=20190914131201136382; cmccssotoken=2995cb9746c44f0bb2d2ed61d7e181aa@.10086.cn; c=2995cb9746c44f0bb2d2ed61d7e181aa; WT_FPC=id=274f7dca70dc500a0eb1568370207719:lv=1568438125933:ss=1568437846215',
    'Host':'shop.10086.cn',
    'Referer':'https://shop.10086.cn/i/?f=billdetailqry&welcome=1568372155773',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-origin',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'
}
def get_html():
    try:
        sql = 'select id from user_tellw order by id DESC limit 1'
        print(sql)
        result = int(cursor.execute(sql))
        # print(cursor.fetchall())
        print(result)
    except:
        pass
    id = result
    url = 'https://shop.10086.cn/i/v1/fee/detailbillinfojsonp/15151531962?callback=jQuery01484335341501053_1568371059523&curCuror=1&step=100&qryMonth=201903&billType=02&_=1568371719071'
    html = requests.get(url,headers=headers).text.replace('})','}').replace('jQuery01484335341501053_1568371059523(','') # 将不符合dict格式的部分替换掉 方便后续进行dict的转换
    print(html)
    # print(type(html)) #str类型
    # 避免转换成dict时报错为空
    global null
    null=''
    # 转换成
    content = eval(html)
    # print(type(content)) # dict类型
    # print(type(content['data'])) # list类型
    list_ocntent = content['data']
    print("起始时间——通信地点——通信方式——对方号码——通信时长——通信类型——套餐优惠——实收通信费（元）")
    for i in list_ocntent: # 遍历存储通话记录的信息 得到每一条数据的dict
        id = id +1
        remark = i['remark']
        startTime = i['startTime']
        commPlac = i['commPlac']
        commMode = i['commMode']
        anotherNm = i['anotherNm']
        commTime = i['commTime']
        commType= i ['commType']
        mealFavorable =i['mealFavorable']
        commFee =i['commFee']
        print(id,remark,startTime,commPlac,commMode,anotherNm,commTime,commType,mealFavorable,commFee)
        insert_data_sql(id,remark,startTime,commPlac,commMode,anotherNm,commTime,commType,mealFavorable,commFee)


def insert_data_sql(id,remark,startTime,commPlac,commMode,anotherNm,commTime,commType,mealFavorable,commFee):
    try:
        print(id)
        sql_2 = """
                    INSERT IGNORE INTO user_tellw (id,anotherNm,commFee,commMode,commPlac,commTime,commType,mealFavorable,remark,startTime)VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}' )
                    """ \
            .format(id,
                    pymysql.escape_string(anotherNm),
                    pymysql.escape_string(commFee),
                    pymysql.escape_string(commMode),
                    pymysql.escape_string(commPlac),
                    pymysql.escape_string(commTime),
                    pymysql.escape_string(commType),
                    pymysql.escape_string(mealFavorable),
                    pymysql.escape_string(remark),
                    pymysql.escape_string(startTime))
        # print(sql_2)
        cursor.execute(sql_2)  # 执行命令
        db.commit()  # 提交事务

    except:
        print("当前sql语句出错")




if __name__=='__main__':
    # remark = '11'
    # startTime = '22'
    # commPlac = '33'
    # commMode = '44'
    # anotherNm = '55'
    # commTime = '66'
    # commType = '77'
    # mealFavorable = '88'
    # commFee = '99'
    # decimal = '1010'
    # insert_data_sql(remark,startTime,commPlac,commMode,anotherNm,commTime,commType,mealFavorable,commFee)
    get_html()