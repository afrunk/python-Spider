import time
from selenium import webdriver
from lxml import etree
class get_book(object):
    web=webdriver.Chrome(executable_path='source/chromedriver.exe')
    web.maximize_window()
    web.get('https://item.jd.com/11993134.html#comment')

    #切换到评价的tab
    web.find_element_by_xpath('//*[@id="detail"] / div[1] / ul / li[4]').click()
    while True:
        #下拉滚动条 从1开始到3结束，分两次加载完每页数据
        for i in range(1,2):
            height=300*i
            strWord="window.scrollBy(0,"+str(height)+")"
            web.execute_script(strWord)
            time.sleep(4)
        seletor=etree.HTML(web.page_source)
        divs=seletor.xpath('//*[@id="comment-0"]/div')
        with open('python_book.txt', 'a') as f:
            for div in divs:

                jd_conmment = div.xpath('./div/p')
                jd_conmment = jd_conmment[0].text if len(jd_conmment) > 0 else ''
                print(jd_conmment)
                try:
                    f.write(jd_conmment + '\n')
                except:
                    pass
        # 分析得知当为最后一页时，最后的ui-pager-next不见了
        if web.page_source.find('ui-pager-next') == -1:
            break

        # 找到“下一页”的按钮元素
        web.find_element_by_class_name('ui-pager-next').click()

        # 因为在下一个循环里首先还要把页面下拉，所以要跳到外层的frame上
        web.switch_to.parent_frame()

if __name__=='__main__':
    get_book()