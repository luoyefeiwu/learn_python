# coding=utf-8
# 发送消息
import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Content-Type': 'application/json; charset=UTF-8'
}
data = {
    "touser": "LuoYeFeiWu",
    "msgtype": "text",
    "agentid": '1000012',
    "text": {
        "content": "我是测试发送消息!此消息就你能看"
    },
}
cookies = {}
with open("cookies.txt", 'r') as file:
    for line in file.read().split(';'):
        name, value = line.strip().split('=', 1)
        cookies[name] = value

requests = requests.post('http://localhost:8082/wetchat/send', data=json.dumps(data),
                         headers=headers,
                         cookies=cookies);

print(requests.text);
