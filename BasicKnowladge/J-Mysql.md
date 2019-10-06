# Mysql
## 问题集
##### Program 1 ：查看报错信息是HTML页面的utf-8转换不完全导致1064报错

```python
# 参考链接为：https://blog.csdn.net/weixin_34314962/article/details/92490539
# 修改 pymysql里的connect文件里的编码，添加 ignore 即可解决
if data is not None:
if encoding is not None:
    data = data.decode(encoding,'ignore') # 添加,'ignore'
if DEBUG: print("DEBUG: DATA = ", data)
if converter is not None:
    data = converter(data)
```

##### Program 2 ：1064无原因报错
输出 sql 语句之后，仍旧没找到原因，可能是语句中有分号导致语句断句不正确，于是无法写入mysql.