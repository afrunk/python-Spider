import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
}


def spider():
    r = requests.get('https://shanghai.8684.cn/line2', headers=headers)
    html_tree = etree.HTML(r.text)
    # 各个站点a标签列表
    a_list = html_tree.xpath('//div[@class="list clearfix"]/a')
    for a in a_list:
        # 站点名
        station = a.xpath('./text()')[0]
        # 站点链接
        station_url = 'https://shanghai.8684.cn/' + a.xpath('./@href')[0]
        get_station_list(station, station_url)


def get_station_list(station, station_url):
    r = requests.get(station_url, headers=headers)
    html_tree = etree.HTML(r.text)
    # 上行站点列表
    up_station_list = html_tree.xpath('//div[@class="bus-lzlist mb15"][1]/ol/li/a/text()')
    # 下行站点列表
    down_station_list = html_tree.xpath('//div[@class="bus-lzlist mb15"][2]/ol/li/a/text()')
    print(f'站点名:{station}')
    print('上行站点列表:')
    print(up_station_list)
    print('下行站点列表:')
    print(down_station_list)


if __name__ == '__main__':
    spider()
