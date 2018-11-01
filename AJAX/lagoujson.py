# coding: utf-8
from urllib import request
# json解析库，对应到lxml
import json

import jsonpath

url = "http://www.lagou.com/lbs/getAllCitySearchLabels.json"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
req = request.Request(url, headers=headers)
response = request.urlopen(req)
html = response.read()
unicodestr = json.loads(html)
# Python形式的列表
city_list = jsonpath.jsonpath(unicodestr, "$..name")

# for item in city_list:
#    print item

# dumps()默认中文为ascii编码格式，ensure_ascii默认为Ture
# 禁用ascii编码格式，返回的Unicode字符串，方便使用
array = json.dumps(city_list, ensure_ascii=False)
print(array)
print(type(array))
with open("lagoucity.json", "w") as f:
    f.write(array)
