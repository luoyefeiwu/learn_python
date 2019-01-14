# 保存
import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Content-Type': 'application/json; charset=UTF-8'
}
data = {
    "banquetid": "692FE42D-4D11-4493-85A9-709FBCB5546B",
    "contractguatables": "12",
    "contractsparetables": "1",
    "contractafamount": 12000
};
cookies = {}
with open("../cookies.txt", 'r') as file:
    for line in file.read().split(';'):
        name, value = line.strip().split('=', 1)
        cookies[name] = value

requests = requests.post('http://localhost:8090/signing/saveSigning', data=json.dumps(data), headers=headers,
                         cookies=cookies);

print(requests.text);