# mongoDB
## 如何安装和使用可视化界面管理mongoDB数据库
mongoDB官网：https://www.mongodb.com/download-center?jmp=nav#community<br>
Robomongo可视化工具：https://robomongo.org/download
- 第一步：首先在c盘mongodb的serverserver\4.0\data\db下进入命令行输入：`mongod --dbpath C:\MongoDB\Server\4.0\data\db`,这样就会启动mongodb，并输出一些日志。我们可以在浏览器输入：`http://localhost:27017/`，它会显示一行文字，意思是告诉你，你已经启动了mongodb.
  It looks like you are trying to access MongoDB over HTTP on the native driver port.
