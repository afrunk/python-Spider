import requests
url='http://hd.chinatax.gov.cn/service/findCredit.do'
for i in range(1,100):
    print("正在抓取第{}页数据".format(i))
    headers={
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language':'zh-HK,zh;q=0.9,zh-CN;q=0.8,en;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
        'Connection': 'keep-alive',
        'Content-Length': '49',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'yfx_c_g_u_id_10003701=_ck19110217314711202359173742477; yfx_f_l_v_t_10003701=f_t_1572687107116__r_t_1572687107116__v_t_1572687107116__r_c_0; _Jo0OQK=5E1E8288F7887F14F281E6539F069F86FE862A1D033FA5D60638A3E6E7B619799E19B02487E0F9FE0ABA890F7964657F14236D97B98BC9FFCECCEF39DC3643BF8661B918CCA8FE3BB944ED14892373145994ED1489237314599BE994A6718907CADGJ1Z1RQ==; JSESSIONID=5EC3A5526DE18229E0AA01345F93091E',
        'Host': 'hd.chinatax.gov.cn',
        'Origin': 'http://hd.chinatax.gov.cn',
       'Referer': 'http://hd.chinatax.gov.cn/nszx/InitCredit.html',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    data={
        'page': '2',
        'location': '',
        'cPage': '',
        'code': '',
        'name':'',
        'evalyear': '2018'
    }
    data['page']=i
    con = requests.post(url,data=data,headers=headers).text
    print(con)