import urllib.request

url = "http://www.baidu.com/s"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}

keyword = input("请输入需要查询的关键字")
wd = {"wd": keyword}

fullurl = url + "?" + wd

# 构造请求对象
request = urllib.request(fullurl, headers=headers)
response = urllib.request.urlopen(request)
print(response.read())
