# coding=utf-8
# 创建人员
import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Content-Type': 'application/json; charset=UTF-8'
}
data = {
    "userid": "fenxiaohui",
    "name": "冯晓辉",
    "alias": "jackzhang",
    "mobile": "18310822643",
    "department": [3],
    "position": "UFO",
    "gender": "1",
    "email": "fengxiaohui@163.com",
    "telephone": "020-123456",
    "address": "北京市达官营",
}

cookies = {}
with open("cookies.txt", 'r') as file:
    for line in file.read().split(';'):
        name, value = line.strip().split('=', 1)
        cookies[name] = value

requests = requests.post('http://localhost:8082/wetchat/createUser', data=json.dumps(data),
                         headers=headers,
                         cookies=cookies);

print(requests.text);
