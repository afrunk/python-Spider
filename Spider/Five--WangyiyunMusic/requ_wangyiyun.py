import requests
import json
import xlwt
j=0
style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')
wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')#当前表的名字
ws.write(j, 0, 'id')
ws.write(j, 1, '评论')
ws.write(j, 2, '点赞数')
ws.write(j,3,'头像')
for i in range(100,69800,100):
	try:
		# print(i)
		url='http://music.163.com/api/v1/resource/comments/R_SO_4_477251491?limit=100&offset='+str(i)
		headers={
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Accept-Encoding':'gzip, deflate',
			'Accept-Language':'zh-HK,zh;q=0.9,zh-CN;q=0.8,en;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
			'Cache-Control':'max-age=0',
			'Connection':'keep-alive',
			'Cookie':'_ntes_nuid=047774d0e618c09c1a825679ccb3ac3e; vjuids=-6514ef7b0.15b3402fb0e.0.a92a55e29ad98; __utma=187553192.1324303449.1486870988.1497609575.1504674339.12; __oc_uuid=5dc3c470-f0d5-11e6-9c31-b5160baded17; _ngd_tid=5%2FHP8ZQrvvZxm7VGFr5CYKI%2FuaAER4Zv; _iuqxldmzr_=32; _ga=GA1.2.1324303449.1486870988; _ntes_nnid=047774d0e618c09c1a825679ccb3ac3e,1519304657923; usertrack=ezq0plrByTmGu3QyyCiFAg==; mp_MA-B154-F82F55E16A53_hubble=%7B%22sessionReferrer%22%3A%20%22https%3A%2F%2Fkada.163.com%2F%3Finref%3Dindex_bottomlink%22%2C%22updatedTime%22%3A%201522905946260%2C%22sessionStartTime%22%3A%201522905946246%2C%22deviceUdid%22%3A%20%2285945fbb-2f26-42a9-89ca-200a16546578%22%2C%22initial_referrer%22%3A%20%22http%3A%2F%2Fwww.icourse163.org%2Fhome.htm%3FuserId%3D1023989942%22%2C%22initial_referring_domain%22%3A%20%22www.icourse163.org%22%2C%22persistedTime%22%3A%201522905946241%2C%22LASTEVENT%22%3A%20%7B%22eventId%22%3A%20%22da_screen%22%2C%22time%22%3A%201522905946260%7D%2C%22sessionUuid%22%3A%20%2240203e00-b9a3-436e-a62b-ca1e3ea93b4e%22%7D; P_INFO=afrunk7@yeah.net|1523370799|0|urs|00&99|gas&1523370766&mailyeah#gas&620100#10#0#0|&0|mailyeah|afrunk7@yeah.net; __f_=1526573348344; vinfo_n_f_l_n3=6a2771ce64f9a8a9.1.7.1491226262312.1527172151663.1528625836992; vjlast=1491226262.1530716635.11; WM_TID=pnfJvDdtNHwVP%2BMRN5xODbIwHvU28Yy0; __utmz=94650624.1533269085.9.8.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmc=94650624; __utma=94650624.1324303449.1486870988.1533780744.1533792988.12; JSESSIONID-WYYY=QG2EoBa7%2F1B6x3pIpRCgrPzTyG%5CRcxjIq9dX8bruu0enADFB%5CXPKnyYvA2pQFjrz%5CzG93r57vea8wRdgMS8X3KEoAX%2FNUcH3M7A1J89JodTccIABqAOcNSahzj5lXANGAgz0%5CMfnX6nvm1TAnK3J6EJte8bUIVMJs7R%5CqMPaRjG2A%2BXc%3A1533796527713; __utmb=94650624.7.10.1533792988; playerid=71070855; WM_NI=fVIHpnPgEY6zKggP%2BM8evru6Ko896cUnpfVEQSVlXPdR0ksrBTXt%2FaoSfGnvxtI1YljSEzhvaG488kziub%2Fw24kO2%2F%2FAJqhuC%2BSyEWc6i5vNFyIRFF1RGP%2FuaP4NAC%2BSa3U%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee91f780f88dfeb5aa64b7b39ad7f825a19cae8dc84689a689d5b37cb4948686ec2af0fea7c3b92aa68a87a9f36694b98bbab57289b9a9b1aa47fcbbba93f83e89b1f8dab56997b2c087d54f938d9a8ddb5ca88e008cf27a828c9895ae6bad8daaa8ed7ebcac87d2dc68aa8d8b9beb7ea399fcd9bb61bab7bb83ae7df2eca5b0b125ed9f8692eb7f81f59d9ac85da1eaa7d6f54686a787b3c54ef38e89b1ae7fa390fcafc449e98dafd4d837e2a3',
			'Host':'music.163.com',
			'Upgrade-Insecure-Requests':'1',
			'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
		}
		response=requests.get(url=url,headers=headers).json()
		# print(response)
		data=response['comments']
		# print(data)
		for i in data:
			j += 1
			# try:
			print(str(j)+'  '+i['user']['nickname']+'\t'+i['content']+'\t'+str(i['likedCount'])+'\t'+i['user']['avatarUrl'])
			ws.write(j, 0, i['user']['nickname'])
			ws.write(j, 1, i['content'])
			ws.write(j, 2, str(i['likedCount']))
			ws.write(j,3,i['user']['avatarUrl'])
			# except:
			# 	pass
			# try:
			# 	print('评论者'+i['beReplied'][0]['user']['nickname']+'\t'+i['beReplied'][0]['content'])
			# except:
			# 	pass
		wb.save('郭源潮.xls')
	except:
		pass
