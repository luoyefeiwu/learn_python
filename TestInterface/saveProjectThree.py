# 保存
import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Content-Type': 'application/json; charset=UTF-8'
}
data = {
    "projectDeclare": {
        "id": "f4001645-c27e-4e3b-92ee-1574191aa69e",
        "xmjhztz": "35.3",
        "xmdwzje": "22",
        "xmwczje": "22",
        "xmgqzje": "22",
        "cjqshte": "22",
        "xmzqzje": "34",
        "lwyyqkje": "35",
        "lwyyqknhll": "",
        "lwyyqkqx": "35",
        "yhckmfxdje": "",
        "zddbjkje": "",
        "yhckmfxdqx": "",
        "yhckmfxdnhll": "",
        "lwyyqk": "无息贷款",
        "chinaGqzb": "22",
        "projectGqzb": "34",
        "otherGqzb": "34",
        "chinaZqzb": "34",
        "projectZqzb": "45",
        "otherZqzb": "45",
        "lwyyqkValue": [
            "无息贷款"
        ],
        "zddbjkqk": 2,
        "yhckmfxd": 2
    },
    "projectGqgcs": [
        {
            "type": 1,
            "gdmc": "",
            "name": "股东名称"
        },
        {
            "type": 2,
            "gdmc": "",
            "name": "股东名称"
        },
        {
            "type": 3,
            "gdmc": "",
            "name": "股东名称"
        }
    ],
    "projectZqgcs": [
        {
            "type": 1,
            "gdmc": "",
            "name": "股东名称"
        },
        {
            "type": 2,
            "gdmc": "",
            "name": "股东名称"
        },
        {
            "type": 3,
            "gdmc": "",
            "name": "股东名称"
        }
    ]
}
cookies = {}
with open("cookies.txt", 'r') as file:
    for line in file.read().split(';'):
        name, value = line.strip().split('=', 1)
        cookies[name] = value

requests = requests.post('http://localhost:8081/ydyl/submit/saveProjectThree', data=json.dumps(data),
                         headers=headers,
                         cookies=cookies);

print(requests.text);
