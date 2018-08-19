# Python
Python reptile code<br>
晴空一鹤排云上，便引诗情到碧霄。<br>
[技术性思考](https://github.com/afrunk/Summer-for-Learing/blob/master/TechnicalThinking.md)<br>
[md语法教程](https://www.jianshu.com/p/86e7fa33de8e)
## 技术点
- 网页知识：
   * CSS\HTML:分析DOM提取网页内容
   * JS:网页的加密解密、json加载等等
- HTTP:
   * GTE\POST方法获取服务器请求获取网页
   * Cookie的作用、模拟登录如何才能够让人分别不出来
- 第三方库：
   * [x] [requests：让HTTP为人类服务](https://github.com/afrunk/Summer-for-Learing/blob/master/BasicKnowladge/Requests.md)。
   * [x] BeautifulSoup4：更简单的分析页面
   * [x] xlwt：将数据存入到csv
   * [ ] xpath:分析页面内容
   * [ ] [pyechart：数据可视化](https://github.com/afrunk/Summer-for-Learing/blob/master/BasicKnowladge/DataVisualization.md)
   * [ ] pandas：数据可视化
- 存储：
   * [x] [本地保存](https://github.com/afrunk/Summer-for-Learing/blob/master/BasicKnowladge/%E6%9C%AC%E5%9C%B0%E4%BF%9D%E5%AD%98.md)：txt、excle、csv
   * [ ] 数据库存储：mongodb、mysql
- 爬虫框架：
   * [ ] Scrapy
   * [ ] PySpider
- 反爬虫：
   * 动态加载
   * js加密
   * 限制时间和提交请求次数
   * 多重加密
   * 登陆获取
- 分布式爬虫
## Spider--Requests
##### Zero--ZhihuBAsic:
  * 基础知识解析<br>
  * 爬取淘宝指定商品和价格:requetst||re<br>
  * 爬取股票数据：requests||bs4<br>
  * 人民日报时评：requests||bs4<br>
  * 所有大学基本信息与物联网专业开设大学：selenium||bs4||pjs<br>
  * 爬取拉勾网python职位信息：requests||bs4||json<br>
  * 爬取极客学院所有课程信息：requests||re<br>
##### One--MaoyanMovies:
  爬取猫眼短评——《我不是药神》,通过猫眼电影的api获取到json文件，通过对json文件的解析得到文本。<br>
##### Two--jianshuImg：
  爬取简书交友页面的最近200页的内容和url链接存入到excle表格中，并下载所有的图片，借助百度的api打分并根据分值存入到不同的文件夹中。<br>
##### Three--LianjiaHouse:
  爬取链家网的二手房、租房、小区等三个方面的信息存入到本地excle中。<br>
##### Four--Yiduxiaoshuo:
  爬取易读小说网的真本小说——《极道天魔》<br>
##### [Six--WZLY](https://github.com/afrunk/Summer-for-Learing/blob/master/Spider/Six--WZLY/%E6%88%91%E6%9C%AC%E5%8F%AF%E4%BB%A5%E5%BF%8D%E5%8F%97%E9%BB%91%E6%9A%97.md):
  爬取我主良缘网的信息和图片并进行可视化分析 `pyechart` `可视化`
##### [Senev--govcn](https://github.com/afrunk/Summer-for-Learing/blob/master/Spider/Sever-Govcn/%E6%A2%A6%E6%83%B3%E8%BF%99%E4%B8%AA%E4%B8%9C%E8%A5%BF.md)
  爬取政府工作报告文本进行分词和词云  `jieba`  `wordcloud` `可视化`
##### [Eight--DemographicVisualization](https://github.com/afrunk/Summer-for-Learing/blob/master/Spider/Eight--DemographicVisualization/%E6%88%91%E6%89%80%E6%9C%89%E7%9A%84%E8%87%AA%E8%B4%9F%E9%83%BD%E6%9D%A5%E8%87%AA%E6%88%91%E7%9A%84%E8%87%AA%E5%8D%91.md)
  爬取政府人口的数据进行本地同步可视化（第一个自己实现的动态可视化界面）`pyecharts`   `可视化`
#####  [鞋图]( http://qcr0122.x.yupoo.com/albums?from=singlemessage&isappinstalled=0&page=2)
  批量盗图
## Spider--Selenium
##### A--SilumatedLoginZhihu:
  模拟登录知乎<br>
##### B--Qzone
  模拟登录qq空间，爬取某好友的所有说说内容保存在txt并制作词云。<br>
##### C--Weibo
  模拟登录微博，爬取某指定好友的所有微博内容存在txt并制作词云。<br>
##### [D--JD](https://github.com/afrunk/Summer-for-Learing/blob/master/Spider--Selenium/D--JD/%E6%88%91%E4%BA%A6%E9%A3%98%E9%9B%B6%E4%B9%85.md)
  爬取京东图书评论，动态难破解直接使用此方法。<br>

## Scrapy
Python Scrapy project group！Daily work and project set。<br>

## 其他
- [Splinter文档](https://splinter-docs-zh-cn.readthedocs.io/zh/latest/#drivers)：python开发的开源web自动化测试的工具集
- [python绿色通道](https://mp.weixin.qq.com/s/BUZhmh-3qIe2HCpZrY4Zig)：爬虫系列文章
- [pyecharts可视化模块文档](http://pyecharts.org/#/)
   * [作者简书教程](https://www.jianshu.com/p/b718c307a61c)：都是静态的可视化。
- 有趣的网站
   * [聚投诉](http://ts.21cn.com/merchant/ranking)
   * 关注某人微博如果有更新的话就将更新内容爬取下来并发送邮件
- [廖雪峰python学习笔记](https://blog.csdn.net/u012084802/article/category/7370766)：python基础知识排查
- [编程派](http://codingpy.com/category/tutorials/)：python各种实现
