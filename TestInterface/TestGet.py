# 获取
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'

}
data = {"phone": "18547838692"};
cookies = {}
with open("cookies.txt", 'r') as file:
    for line in file.read().split(';'):
        name, value = line.strip().split('=', 1)
        cookies[name] = value

requests = requests.get("http://localhost:8090/bussinessFollow/searchBussinessFollow", params=data, headers=headers,
                        cookies=cookies);
print(requests.text);
