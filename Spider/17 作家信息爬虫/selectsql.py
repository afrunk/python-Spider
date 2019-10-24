import pymysql
db = pymysql.connect(host='127.0.0.1',
                     port=3306,
                     user='root',
                     password='password',
                     db='world',
                     charset='utf8')
cursor = db.cursor()
import csv
sql_1 = "select  * from author"
# print(sql_1)
cursor.execute(sql_1)  # 执行命令
message = cursor.fetchall()


csv_file=csv.reader(open('NewData.csv','r'))
print(csv_file) #可以先输出看一下该文件是什么样的类型
content=[] #用来存储整个文件的数据，存成一个列表，列表的每一个元素又是一个列表，表示的是文件的某一行
for line in csv_file:
    # print(line) #打印文件每一行的信息
    content.append(line)
print("该文件中保存的数据为:\n",content)
for i in content:
    for j in message:
        if i[0] == j[0]:
            print("yes")
            i.append(j[1])
            i.append(j[2])
print(content)



with open("Data.csv",'a+',newline='') as f: # 写入到本地csv中 a+会自动创建文件 newline解决中间有空行的问题
    for data in content:
         write=csv.writer(f)
         write.writerow(data)