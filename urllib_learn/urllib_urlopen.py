import urllib
from urllib.request import urlopen
#向指定的url发送请求
response = urlopen("http://www.baidu.com")
# 服务器返回的类文件对象支持Python文件对象的操作方法
# read()方法就是读取文件里的全部内容，返回字符串
html = response.read()
# 打印响应内容
print(html)
