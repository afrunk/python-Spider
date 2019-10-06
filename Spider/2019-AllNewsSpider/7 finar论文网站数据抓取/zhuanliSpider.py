'''
date:2019-10-3
技术难点：
    - 存入数据库：
        数据库表 七个字段
    - 多线程
    - 日志记录爬取内容
    - 随机睡眠时间

总数 15900 = 15 * 1060

'''

# https://www.finra.org/rules-guidance/oversight-enforcement/finra-disciplinary-actions?search=&firms=&individuals=&field_fda_case_id_txt=&field_core_official_dt%5Bmin%5D=1/1/2007&field_core_official_dt%5Bmax%5D=&field_fda_document_type_tax=All&page=1058  1059

# https://www.finra.org/rules-guidance/oversight-enforcement/finra-disciplinary-actions?search=&firms=&individuals=&field_fda_case_id_txt=&field_core_official_dt%5Bmin%5D=1/1/2007&field_core_official_dt%5Bmax%5D=&field_fda_document_type_tax=All&page=1056 1057

# https://www.finra.org/rules-guidance/oversight-enforcement/finra-disciplinary-actions?search=&firms=&individuals=&field_fda_case_id_txt=&field_core_official_dt%5Bmin%5D=1/1/2007&field_core_official_dt%5Bmax%5D=&field_fda_document_type_tax=All&page=0 1

# https://www.finra.org/rules-guidance/oversight-enforcement/finra-disciplinary-actions?search=&firms=&individuals=&field_fda_case_id_txt=&field_core_official_dt%5Bmin%5D=1/1/2007&field_core_official_dt%5Bmax%5D=&field_fda_document_type_tax=All&page=1059

import requests
from bs4 import BeautifulSoup
import time
import random # 随机函数
from multiprocessing import Pool # 多线程
import pymysql
db = pymysql.connect(host='127.0.0.1',
                     port=3306,
                     user='root',
                     password='password',
                     db='world',
                     charset='utf8')
cursor = db.cursor()


def get_html(url):


    # try except来确保程序一直运行 如果一直try则不操作 如果 except 则将链接存入到log日志文件中 方便下次重新读取
    try:
        con = requests.get(url, timeout=10)  # 请求超过10s超时

        # print(con.text) # 输出是否可以请求到HTML页面
        # print(con.status_code) # 状态码


        # 如果状态码是200 则证明可以获取到
        if con.status_code == 200:
            print("正在分析页面---")
            s_content = BeautifulSoup(con.text,'lxml')
            # 包含所有目标内容的标签 table
            table = s_content.find('table',class_='table views-table views-view-table cols-5')
            # print(table) # 输出是否筛选正确
            tbody=table.find('tbody') # 去掉导航栏之后的表格内容 所有目标内容都包含在tbody下的tr内
            # print(tbody)
            trs = tbody.find_all('tr')# 一个链接下有15个tr 包含每一行的目标内容
            for tr in trs:
                # print(tr.text) # 输出每个tr的内容 不包含标签
                tds=tr.find_all('td')
                # print(tds) # 输出测试用语 是否获取到正确的内容

                # 第一个 td pdf链接和编号
                a_href = tds[0].find('a') # 第一个td获取 pdf链接 目标数据 0
                pdf_href ='https://www.finra.org/sites/default/files/fda_documents/'+ a_href.get('href') # pdf 下载链接
                print(pdf_href)
                CaseID = a_href.text   # pdf 编号  目标数据 1
                print(CaseID)

                # 第二个 td Casu Summary 描述
                CaseSummary=tds[1].text # 目标数据 2
                print(CaseSummary)

                # 第三个 td Document Type
                DocumentType=tds[2].text # 目标数据 3
                print(DocumentType)

                # 第四个 td Firms/ Individuals
                FirmsOrIndividuals = tds[3].find('div',class_='row').find_all('span') # class=row下的span只有两个第一个是类别 第二个是内容
                # print(FirmsOrIndividuals[1])
                labels = FirmsOrIndividuals[0].find_all('i',class_='fa fa-user anchor-blue') # 如果查找到符合条件的i标签 则 数字会等于1 则填充1 否则就是0 即人是1 房子是0
                print("查找到的符合条件的标签数： "+str(len(labels)))
                label_num = len(labels)  # 目标数据 4
                print(label_num)

                Individuals = FirmsOrIndividuals[1].text # 第二个span的标签即内容
                print(Individuals) # 目标数据 5

                # 第五个 td ActionDate
                ActionDate = tds[4].text # 目标数据 6
                print(ActionDate+'\n')

                # 将数据插入数据库 避免重复打开 excle带来的时间等待
                try:
                    sql_2 = """
                            INSERT IGNORE INTO finar (a_href,CaseID,CaseSummary,DocumentType,label_num,Individuals,ActionDate)VALUES('{}','{}','{}','{}','{}','{}','{}' )
                                        """ \
                        .format(
                        pdf_href, # 报错 去掉括号 网站的解决是如此 实践之后确实没有问题
                        pymysql.escape_string(CaseID),
                        pymysql.escape_string(CaseSummary),
                        pymysql.escape_string(DocumentType),
                        label_num,
                        pymysql.escape_string(Individuals),
                        pymysql.escape_string(ActionDate),
                    )
                    print(sql_2)
                    cursor.execute(sql_2)  # 执行命令
                    db.commit()  # 提交事务
                # 如果提交失败 依旧写入到log日志中
                except:
                    # 如果报错直接跳出当前循环
                    # break
                    pass
                # break # 测试用语 只输出第一个 tr里的tds

        # 随机睡眠1-5s
        time.sleep(random.random(1,5))
    except(Exception, BaseException) as e:
        print(e)
        # 如果读取失败 则写入到 日志文件
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write(url + '\n')
            f.close()

if __name__=='__main__':
    # 构建链接池
    url_list =[]
    for i in range(0,1060): # 总共有1059页
        url_test ='https://www.finra.org/rules-guidance/oversight-enforcement/finra-disciplinary-actions?search=&firms=&individuals=&field_fda_case_id_txt=&field_core_official_dt%5Bmin%5D=1/1/2007&field_core_official_dt%5Bmax%5D=&field_fda_document_type_tax=All&page='+str(i)
        url_list.append(url_test) # 将构建好的链接添加到列表中去

    # 多线程方法
    # start_2 = time.time()
    # pool = Pool(processes=10)
    # pool.map(get_html, url_list) # 将函数传入 然后将链接列表传入
    # end_2 = time.time()
    # print('2进程爬虫耗时:', end_2 - start_2)

    # 单线程方法
    for url_true in url_list:
        get_html(url_true)