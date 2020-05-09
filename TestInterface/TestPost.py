# 保存
import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Content-Type': 'application/json; charset=UTF-8'
}
data ={
    "listBanquetDepositDetails": [
        {
            "detailsid": "71D6EBA3-8060-41DF-8961-6C8773BE8F24",
            "banquetid": "da20a9a7-c55c-4d17-8219-dc529fe9b00a",
            "amount": 100,
            "paytype": 3,
            "paytime": "2020-04-28 00:00:00",
            "payee": "王丛",
            "payeeid": "ff4b960f-5bdd-44b3-878e-97a60a566042",
            "drawee": "张",
            "draweeid": "",
            "deposittype": 1,
            "type": 1
        }
    ],
    "banquetContract": {
        "depositremark": "备注",
        "banquetid": "da20a9a7-c55c-4d17-8219-dc529fe9b00a"
    },
    "listBanquetAffix": [
        {
            "banquetid": "da20a9a7-c55c-4d17-8219-dc529fe9b00a",
            "originalfilename": "微信截图_20200428185711.png",
            "contracturl": "http://banquet-uat.oss-cn-hangzhou.aliyuncs.com/609d2478-572d-4e61-9fd1-fe78a8cdc8de.png"
        }
    ]
}
cookies = {}
with open("cookies.txt", 'r') as file:
    for line in file.read().split(';'):
        name, value = line.strip().split('=', 1)
        cookies[name] = value

requests = requests.post('http://localhost:8090/signing/saveDeposit', data=json.dumps(data),
                         headers=headers,
                         cookies=cookies);

print(requests.text);
