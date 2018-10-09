# 抓取二进制数据
import requests
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') # Change default encoding to utf8
r=requests.get('http://github.com/favicon.ico')
print(r.text)
print(r.content)
with open('favicon.ico','wb') as f:
    f.write(r.content)
