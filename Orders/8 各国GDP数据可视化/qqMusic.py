import requests
import html

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Origin': 'https://y.qq.com',
    'Referer': 'https://y.qq.com/n/yqq/song/0039MnYb0qxYhV.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

for page in range(1,2):# 这里设置为抓取多少歌曲的歌词

    res = requests.get(
        'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=67198573060150304&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p={}&n=2&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'.format(
            page), headers=headers)

    search_html = res.json()
    items = search_html['data']['song']['list']
    for item in items:
        item_id = item['id']
        item_name = item['name']

        item_res = requests.get(
            'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg?nobase64=1&musicid={}&-=jsonp1&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'.format(
                item_id), headers=headers)
        item_html = item_res.json()
        print('------------------------------------{}--------------------------------------'.format(item_name))
        print(html.unescape(item_html['lyric']))