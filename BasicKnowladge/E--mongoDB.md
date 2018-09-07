# mongoDB
## 如何安装和使用可视化界面管理mongoDB数据库
mongoDB官网：https://www.mongodb.com/download-center?jmp=nav#community<br>
Robomongo可视化工具：https://robomongo.org/download
- 第一步：<br>
首先在c盘mongodb的serverserver\4.0\data\db下进入命令行输入：`mongod --dbpath C:\MongoDB\Server\4.0\data\db`,这样就会启动mongodb，并输出一些日志。我们可以在浏览器输入：`http://localhost:27017/`，它会显示一行文字，意思是告诉你，你已经启动了mongodb.
  >  It looks like you are trying to access MongoDB over HTTP on the native driver port.
- 第二步：<br>
返回之前的bin目录，在此文件夹下打开命令行输入：mongo,会直接进入mongo的命令行的一个交互页面。在这个页面下进入一个命令的输入就可以实现数据库的操作。
    ```
    > db
    test
    > db.test.insert(('a':'b'))
    2018-08-22T11:46:44.029+0800 E QUERY    [js] SyntaxError: missing ) in parenthetical @(shell):1:19
    > ^C
    bye
    ```
- 第三步:如何设置自动连接的配置
    ```
    C:\Windows\system32>mongod --bind_ip 0.0.0.0 --logpath C:\MongoDB\Server\4.0\data\db\logs\mongo.log --logappend --dbpath C:\MongoDB\Server\4.0\data\db
     --port 27017 --serviceName "MongoDB"  --serviceDisplayName "MongoDB" --install
    ```
## 如何启动mongodb数据库
1.进入mongodb的安装路径的bin目录下打开dos窗口，输入启动命令`mongod --dbpath C:\MongoDB\Server\4.0\data\db`，回车之后dos界面出现12701的字样说明服务启动成功了。<br>
2.之前的窗口不要关闭，我们在回到之前的bin目录下输入mongo此时我们会发现会告诉你mongodb数据库正在运行。<br>
3.我们在上面打开的窗口输入`show dbs`，我们可以查看到所有的数据库的情况。（这个操作需要确保我们之前运行mongodb的命令窗口是未关闭的，否则就会出现无法连接的情况。）如果我们觉得使用命令行操作太过麻烦，还可以通过直接打开可视化软件Robo 3T来查看数据库的情况，一样的需要确保数据库处理打开状态。<br>

## 如何将数据存取在mongodb数据库
以下是读取txt文本的每一行内容，然后对每一行的内容进行一个mongodb的数据库的写入操作。<br>
```
import pymongo
client=pymongo.MongoClient('localhost',27017)#连接数据库
walden=client['walden']#给数据库起名
sheet_tab=walden['sheet_tab']
path='walden.txt'
with open(path,'r') as f:
    lines=f.readlines()#读取txt的每行句子
    for index,line in enumerate(lines):
        data={
            'index':index,#第多少行
            'line':line,#每行的内容
            'words':len(line.split())#有多少个单词
        }
        # print(data)
        sheet_tab.insert(data)
```
我们还可以将数据进行一个筛选后再输出的操作。
```
import pymongo
client=pymongo.MongoClient('localhost',27017)#连接数据库
walden=client['walden']#给数据库起名
sheet_tab=walden['sheet_tab']
for item in sheet_tab.find():
    print(item)
```
