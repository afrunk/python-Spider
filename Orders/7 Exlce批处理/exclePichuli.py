import xlrd
import re
workbook2 = xlrd.open_workbook(r'数据.xlsx')
sheet2 = workbook2.sheet_by_index(0)
pcols2 = sheet2.col_values(0)
# print(pcols2[1])
content = pcols2[1].split('.')
print(content)