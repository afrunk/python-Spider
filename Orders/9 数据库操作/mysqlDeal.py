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

def updateData():
    try:
        update_sql = """UPDATE data set uptime ='2019-11-19' where studentname ='许婉雪' union UPDATE data set uptime ='2019-11-19' where studentname ='王智尧' """
        cursor.execute(update_sql)
        db.commit()
    except:
        print("出错了")

def deleteData():
    try:
        delete_sql = """delete from data where studentname = 'test' """
        cursor.execute(delete_sql)
        db.commit()
    except:
        print("出错了")

if __name__ == '__main__':
    # 插入数据
    inputData()
    # # 查询数据
    selectData()
    # 修改数据
    # updateData()
    # 删除数据
    # deleteData()