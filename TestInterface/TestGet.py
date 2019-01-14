# 获取 
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'

}
data = {"banquetId": "692FE42D-4D11-4493-85A9-709FBCB5546B"};
cookies = {}
with open("../cookies.txt", 'r') as file:
    for line in file.read().split(';'):
        name, value = line.strip().split('=', 1)
        cookies[name] = value

requests = requests.post("http://localhost:8090/signing/getContract", data=data, headers=headers,
                         cookies=cookies);
print(requests.text);