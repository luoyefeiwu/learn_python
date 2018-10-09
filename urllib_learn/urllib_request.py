import urllib.request
from urllib.request import urlopen


ua_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}
request = urllib.request.Request("http://www.baidu.com/", headers=ua_headers)
with urlopen(request) as res:
    res = res.read()
print(res)
