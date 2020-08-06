# 保存
import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    # 'Content-Type': 'application/json; charset=UTF-8'
}
data = {
    "name": "北京发改委",
    "userid": "BFA831DB0000000072B933040000000E",
    "loginname": "bjfgw",
    "password": "1",
    "phone": "18500392662",
    "departmentId": "地方发改委",
    "code": "18500392662",
    "etype": "0",
    "eclassify": "1",
    "cid": "18500392662",
    "capital": "18500392662",
    "province": "18500392662",
    "city": "18500392662",
    "area": "18500392662",
    "address": "18500392662",
    "legal": "18500392662",
    "contact": "18500392662",
    "telePhone": "18500392662",
    "mobilePhone": "18500392662",
    "zipCode": "18500392662",
    "abscription": "18500392662"
}
cookies = {}
with open("cookies.txt", 'r') as file:
    for line in file.read().split(';'):
        name, value = line.strip().split('=', 1)
        cookies[name] = value

requests = requests.get('http://localhost:8081/ydyl/person/edit', params=data,
                        headers=headers,
                        cookies=cookies);

print(requests.text);
