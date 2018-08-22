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
    ```C:\Windows\system32>mongod --bind_ip 0.0.0.0 --logpath C:\MongoDB\Server\4.0\data\db\logs\mongo.log --logappend --dbpath C:\MongoDB\Server\4.0\data\db
     --port 27017 --serviceName "MongoDB"  --serviceDisplayName "MongoDB" --install
    ```
