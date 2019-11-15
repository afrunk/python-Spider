import pymysql
db = pymysql.connect(host='127.0.0.1',
                     port=3306,
                     user='root',
                     password='password',
                     db='world',
                     charset='utf8')
cursor = db.cursor()

def inputData():
    # 插入数据准备
    studentname = '许婉雪'
    major = '交互设计'
    uptime = '2019/11/6'
    subject = '文件系统'
    try:
        sql_2 = """
                INSERT IGNORE INTO data (studentname,major,uptime,subject)VALUES('{}','{}','{}','{}'  )
                    """ \
            .format(
            pymysql.escape_string(studentname),
            pymysql.escape_string(major),
            pymysql.escape_string(uptime),
            pymysql.escape_string(subject),
        )
        # print(sql_2)
        cursor.execute(sql_2)  # 执行命令
        db.commit()  # 提交事务
    except:
        pass

def selectData():
    try:
        sql ='select * from data'
        cursor.execute(sql)  # 执行命令
        content = cursor.fetchall()
        for i in  content:
            print(i)
    except:
        pass

if __name__ == '__main__':
    # 插入数据
    inputData()
    # 查询数据
    selectData()