"""
获取历史房价

https://beijing.anjuke.com/prop/view/O1205556653841408?from=comm_one-saleMetro&spread=commsearch_r&uniqid=pc5dceb34fd8a0a1.64694915&position=1&kwtype=comm_one&now_time=1573827407

"""
import requests

def getCommid(commid):
    url ='https://beijing.anjuke.com/community/m26-p7/'
    headers={
        '':'',
        'cookie':'sessid=1F5436C1-4A4C-E7EE-745F-1FB4521979F6; aQQ_ajkguid=9CBC89D6-20A4-7202-1A58-AE3DECD664BB; lps=http%3A%2F%2Fbeijing.anjuke.com%2Fprop%2Fview%2FO1205556653841408%3Ffrom%3Dcomm_one-saleMetro%26spread%3Dcommsearch_r%26uniqid%3Dpc5dceb34fd8a0a1.64694915%26position%3D1%26kwtype%3Dcomm_one%26now_time%3D1573827407%7C; ctid=14; twe=2; browse_comm_ids=51713; ajk_member_captcha=b012fc239331ce51c9194f2278d91ac9; _ga=GA1.2.1283711408.1573827568; _gid=GA1.2.1642833745.1573827568; wmda_uuid=6ff80f8ac8f48c8991f03d3d88aa0dd9; wmda_new_uuid=1; wmda_session_id_6289197098934=1573827568665-b52c7b08-d151-2920; wmda_visited_projects=%3B6289197098934; 58tj_uuid=3f2e78f0-b87c-45b3-a85b-d18a9886a2c1; init_refer=; new_uv=1; als=0; propertys=bvc12x5a80-q10l57_; new_session=0'
    }
    con =requests.get(url).text
    print(con)

if __name__ == '__main__':
    getCommid(1)