# Capture tutorial
## Fiddler抓包工具
首先去[官网](http://fiddler2.com/)下载软件，然后是配置环境。<br>
下载证书，在浏览器输入：http://localhost:8888/，然后将证书下载下来之后发给手机，在手机的安全-设置管理与凭证导入本地证书，之后在wifi处设置代理。<br>
使用fiddler抓包，需要使得电脑和手机在同一个内网，我们将手机和电脑处于一个wifi环境，然后使用电脑的ip代理访问。在cmd输入：`ipconfig`，找到WLAN的IPv4地址。IPv4地址：192.168.1.106记下这个地址写入到手机的代理，端口号为8888.<br>
