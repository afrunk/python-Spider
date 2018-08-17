#-*- coding:utf-8-*-
import xlrd
from datetime import date,datetime

def read_excel():
	#打开文件
	workbook=xlrd.open_workbook(r'郭源潮.xls')
	#获取所有的sheet
	print(workbook.sheet_names())#['A Test Sheet']

	#根据sheet索引或者名称获取sheet内容
	sheet=workbook.sheet_by_index(0)#sheet索引从0开始
	# sheet=workbook.sheet_names('A Test Sheet')

	#sheet的名称，行数，列数
	print(sheet.name,sheet.nrows,sheet.ncols)

	#获取整行和整列的值（数组）
	rows=sheet.row_values(1)#获取第一行的内容
	cols=sheet.col_values(3)#获取第三列的内容

	print(rows[3])#获取第一行的第4个单元格的内容
	print(cols[2])


if __name__=='__main__':
	read_excel()