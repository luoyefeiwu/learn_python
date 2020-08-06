# 保存
import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    # 'Content-Type': 'application/json; charset=UTF-8'
}
data = {
    'username': '121213',
    'password': '123123'
}
cookies = {}
with open("cookies.txt", 'r') as file:
    for line in file.read().split(';'):
        name, value = line.strip().split('=', 1)
        cookies[name] = value

requests = requests.get('http://localhost:8081/ydyl/sso/verificationUser',params=data,
                        headers=headers,
                        cookies=cookies);

print(requests.text);
