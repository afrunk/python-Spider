# Python
Python reptile code<br>
晴空一鹤排云上，便引诗情到碧霄。<br>
[自我进化](https://github.com/afrunk/Summer-for-Learing/blob/master/TechnicalThinking.md)<br>
[他我进化](https://github.com/afrunk/Summer-for-Learing/blob/master/SkillThinking.md)<br>
[md语法教程](https://www.jianshu.com/p/86e7fa33de8e)
>  本库是本人自己学习的过程中学习所总结的一些东西，APP\Spider--Selenium\Spider\Scrapy等都是各种项目的具体的文件夹，其中大部分都具有解释性的实现md文档，而BasicKnowladeg文件夹内是在学习的过程中所需要掌握和使用的一些第三方库或数据库等等技术记录文章，不仅仅是为自己的未来的实践做一个记录查询，更多的是希望后来人可以更快速和系统的学习爬虫
## 技术点
- 网页知识：
   * CSS\HTML:分析DOM提取网页内容
   * JS:网页的加密解密、json加载等等
- HTTP:
   * GTE\POST方法获取服务器请求获取网页
   * Cookie的作用、模拟登录如何才能够让人分别不出来
- 第三方库：
   * [x] [requests：让HTTP为人类服务](https://github.com/afrunk/Summer-for-Learing/blob/master/BasicKnowladge/B--Requests.md)。
   * [x] [Urllib](https://github.com/afrunk/Summer-for-Learing/tree/master/BasicKnowladge):最基本的请求库
   * [x] BeautifulSoup4：更简单的分析页面
   * [ ] xpath:分析页面内容
   * [ ] [pyechart：数据可视化](https://github.com/afrunk/Summer-for-Learing/blob/master/BasicKnowladge/D--DataVisualization.md)
   * [ ] pandas：数据处理
   * [x] [selenium](https://github.com/afrunk/Summer-for-Learing/blob/master/BasicKnowladge/F--Selenium.md):处理动态交页面数据
- 存储：
   * [x] [本地保存](https://github.com/afrunk/Summer-for-Learing/blob/master/BasicKnowladge/A--%E6%9C%AC%E5%9C%B0%E4%BF%9D%E5%AD%98.md)：txt、excle、csv
   * [ ] 数据库存储：
      - [mongodb](https://github.com/afrunk/Summer-for-Learing/blob/master/BasicKnowladge/E--mongoDB.md)
      - [mysql](https://github.com/afrunk/Summer-for-Learing/blob/master/BasicKnowladge/J-Mysql.md)
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
- [封装](https://github.com/afrunk/Spider-Summer-for-Learing/blob/master/BasicKnowladge/I-exe%E8%84%9A%E6%9C%AC%E6%89%93%E5%8C%85.md)
## Spider--Requests

##### [2019-AllNewsSpider]()
***
|  Number |   Website |      Document |
|:------:|:------:|:------:|
|1|[Digikey美国电子产品网站](https://github.com/afrunk/spiderClock)|该爬虫单独建了一个Repository,大批量抓取近900万数据。涉及多线程、数据库存储和导出、图片保存、进程监控等问题|
| 2 |[b站弹幕爬虫可视化](https://github.com/afrunk/python-Spider/blob/master/Spider/2019-AllNewsSpider/1%20b%E7%AB%99%E5%BC%B9%E5%B9%95%E7%88%AC%E8%99%AB%E5%8F%AF%E8%A7%86%E5%8C%96/bSiteSipderEasy.py)|获取b站弹幕的XML文件简单，复杂的地方在于如何处理和去重统计弹幕数。词云做的一般|
|3 |[小说爬虫](https://github.com/afrunk/python-Spider/tree/master/Spider/2019-AllNewsSpider/3%20%E5%B0%8F%E8%AF%B4%E7%88%AC%E8%99%AB)|文本写入操作的简单记录，无其他用处|
|4|[数学建模爬虫](https://github.com/afrunk/python-Spider/tree/master/Spider/2019-AllNewsSpider/2%20%E6%95%B0%E5%AD%A6%E5%BB%BA%E6%A8%A1%E7%88%AC%E8%99%AB)|一动态刷新页面的重复抓取写入Excle，碰到的难点在于如何修改而不覆盖之前的数据。|
|5|[移动通话记录](https://github.com/afrunk/python-Spider/tree/master/Spider/2019-AllNewsSpider/4%20%E7%A7%BB%E5%8A%A8%E9%80%9A%E8%AF%9D%E8%AE%B0%E5%BD%95)|难点在于获取POST链接，以及写入mysql数据库|
|6|[房地产数据爬虫](https://github.com/afrunk/python-Spider/tree/master/Spider/2019-AllNewsSpider/5%20%E6%88%BF%E5%9C%B0%E4%BA%A7%E6%95%B0%E6%8D%AE%E7%88%AC%E8%99%AB)|HTMl多层循环，数据库存储 [目标网站](https://cucc.tazzfdc.com/reisPub/pub/welcome)|
|7|[去哪儿携程门票评论](https://github.com/afrunk/python-Spider/tree/master/Spider/2019-AllNewsSpider/6%20%E5%8E%BB%E5%93%AA%E5%84%BF%E6%90%BA%E7%A8%8B%E9%97%A8%E7%A5%A8%E8%AF%84%E8%AE%BA)|去哪儿的评论简单，直接get拼接的链接即可。携程的POST请求链接不同景点的全都一直，修改的是data里的cid值。数据库存储再导出成excle，快，而且可以避免重复数据的抓取。|
|8|[finar论文网站数据抓取](https://github.com/afrunk/python-Spider/tree/master/Spider/2019-AllNewsSpider/7%20finar%E8%AE%BA%E6%96%87%E7%BD%91%E7%AB%99%E6%95%B0%E6%8D%AE%E6%8A%93%E5%8F%96)|多线程、随机休眠、数据库存储、日志文件记录爬虫|
 
 

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

## PySpider
可视化爬虫框架

## APP
[抓包](https://github.com/afrunk/Summer-for-Learing/blob/master/APP/charles%E2%80%94%E2%80%94Capture%20tutorial.md)

## 其他
- [Splinter文档](https://splinter-docs-zh-cn.readthedocs.io/zh/latest/#drivers)：python开发的开源web自动化测试的工具集
- [Jack Cui](http://cuijiahua.com/blog/2018/03/spider-5.html)：python系列文章（中级可吸收）
  * [python3网络爬虫入门](https://blog.csdn.net/column/details/15321.html)(初中级入门实践)
- [pyecharts可视化模块文档](http://pyecharts.org/#/)
   * [作者简书教程](https://www.jianshu.com/p/b718c307a61c)：都是静态的可视化。
- 有趣的网站或点子
   * [聚投诉](http://ts.21cn.com/merchant/ranking)（有机会可以尝试爬取）
   * 关注某人微博如果有更新的话就将更新内容爬取下来并发送邮件
   * 爬取公众号文章并且写入到本地的pdf文件中（python绿色通道实现但是未详细分享）
- [廖雪峰python学习笔记](https://blog.csdn.net/u012084802/article/category/7370766)：python基础知识排查
- [编程派](http://codingpy.com/category/tutorials/)：python各种实现
- [爬虫合集](https://github.com/bodekjan/awesome-spider)：年久失修
- [OKEX](https://okexcomweb.bafang.com/account/login):[API](https://github.com/okcoin-okex/API-docs-OKEx.com)区块链批量交易脚本
- [网易云评论](https://github.com/monkey-soft/SchweizerMesser)：存入mogondb，该作者经营一个[公众号](https://github.com/monkey-soft/treasure)
- [NGUWQ掘金作者github库](https://github.com/NGUWQ/Python3Spider)：确实在爬虫方面做的很不错，之前我没有深入学习selenium的时候有个租房的单子没有接，有个去哪儿酒店的单子没有接，但是用selenium来做确实可以解决很多问题，就好像之前我爬取了京东的书的评价一样的，之前爬取手机的单子就可以通过这样的方法来实现了。只有不断的学习进步才可以让自己的眼界更加的开阔，更加的牛逼。[爬虫进阶之去哪儿酒店（国内外）](https://juejin.im/post/5b7b6a1fe51d4538d5175073)
- [淘宝商品爬取](https://blog.csdn.net/Leesoar521yt/article/details/81461939)：直接使用selenium来爬取淘宝上ipad的数据
- [12306抢票脚本](https://github.com/bsbforever/spider/blob/master/selenium_12306.py)
- [安居客爬虫](https://blog.csdn.net/xudailong_blog/article/details/79303820)
- [爬虫文章索引](https://blog.csdn.net/TheSnowBoy_2/article/details/55800142)
- [莫烦博客](https://morvanzhou.github.io/tutorials/data-manipulation/scraping/5-01-selenium/)
- [gitbook](https://legacy.gitbook.com/@wizardforcel):大概在五十本书左右,发现还可以下载pdf版本的文档,多好的东西阿,为什么就是这么的不稳定的呢?要不然我何苦来这里写笔记.

## 接单
- [0 Pdf转txt统计词频]():代码有全部得注释，主要难点在于统计词频和复写excle
