# coding=utf-8
# 保存
import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Content-Type': 'multipart/form-data'
}
data = [
    {
        "projectDeclare": {
            "id": "123"
        }
    }
]
cookies = {}
with open("cookies.txt", 'r') as file:
    for line in file.read().split(';'):
        name, value = line.strip().split('=', 1)
        cookies[name] = value

files = {'file': open('导入.txt', 'rb')}
requests = requests.post('http://localhost:8081/ydyl/upload/uploadFile', files=files,
                         cookies=cookies);

print(requests.text);
