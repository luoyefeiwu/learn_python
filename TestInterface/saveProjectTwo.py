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
        "xmjhztz": 35.3,
        "xmdwzje": 22,
        "xmwczje": "333",
        "xmgqzje": 22,
        "cjqshte": 22,
        "xmzqzje": 34,
        "lwyyqkje": 35,
        "lwyyqknhll": "",
        "lwyyqkqx": 35,
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
            "id": "43fd4f9f-7e06-4db1-9189-95f291908e66",
            "projectId": "f4001645-c27e-4e3b-92ee-1574191aa69e",
            "type": 1,
            "gdmc": "",
            "sort": 1,
            "name": "3"
        },
        {
            "id": "963c84ed-3ed3-41d5-b212-5f90d7231fe9",
            "projectId": "f4001645-c27e-4e3b-92ee-1574191aa69e",
            "type": 2,
            "gdmc": "",
            "sort": 2,
            "name": "3"
        },
        {
            "id": "679e37fd-be5a-466a-a948-a68418550d62",
            "projectId": "f4001645-c27e-4e3b-92ee-1574191aa69e",
            "type": 3,
            "gdmc": "",
            "sort": 3,
            "name": "33"
        }
    ],
    "projectZqgcs": [
        {
            "id": "205c7a7c-03c7-46e9-8f95-00f8baf7c4e5",
            "projectId": "f4001645-c27e-4e3b-92ee-1574191aa69e",
            "type": 1,
            "gdmc": "",
            "sort": 1,
            "name": "3"
        },
        {
            "id": "c88df85c-5dcb-46cd-b365-b10d5f4f8178",
            "projectId": "f4001645-c27e-4e3b-92ee-1574191aa69e",
            "type": 1,
            "gdmc": "",
            "sort": 1,
            "name": "3"
        },
        {
            "id": "d16e0200-5190-45db-8502-4e71deb135fc",
            "projectId": "f4001645-c27e-4e3b-92ee-1574191aa69e",
            "type": 1,
            "gdmc": "",
            "sort": 1,
            "name": "3"
        },
        {
            "id": "72df3610-3875-4aa1-a1c3-d5066ea07912",
            "projectId": "f4001645-c27e-4e3b-92ee-1574191aa69e",
            "type": 1,
            "gdmc": "",
            "sort": 1,
            "name": "3"
        },
        {
            "id": "24f422c8-f83a-4c40-8ed0-907c3e421233",
            "projectId": "f4001645-c27e-4e3b-92ee-1574191aa69e",
            "type": 1,
            "gdmc": "",
            "sort": 2,
            "name": "3"
        },
        {
            "id": "798abafd-39a6-4b07-8f14-454f1a15fce6",
            "projectId": "f4001645-c27e-4e3b-92ee-1574191aa69e",
            "type": 2,
            "gdmc": "",
            "sort": 2,
            "name": "3"
        },
        {
            "id": "495ffbce-3267-4e2a-8c8e-f8ea5993430c",
            "projectId": "f4001645-c27e-4e3b-92ee-1574191aa69e",
            "type": 1,
            "gdmc": "",
            "sort": 2,
            "name": "3"
        },
        {
            "id": "003281e2-144a-4508-9d57-c2a8c9f153fd",
            "projectId": "f4001645-c27e-4e3b-92ee-1574191aa69e",
            "type": 2,
            "gdmc": "",
            "sort": 2,
            "name": "3"
        },
        {
            "id": "51ca83b0-a6d0-4c8f-8154-341f2c866068",
            "projectId": "f4001645-c27e-4e3b-92ee-1574191aa69e",
            "type": 3,
            "gdmc": "",
            "sort": 3,
            "name": "3"
        },
        {
            "id": "e52e4f1e-b75a-4f4e-be41-fc3a4653dd26",
            "projectId": "f4001645-c27e-4e3b-92ee-1574191aa69e",
            "type": 2,
            "gdmc": "",
            "sort": 3,
            "name": "3"
        },
        {
            "id": "2c649fcd-09e9-40f8-8304-838dc94ee83d",
            "projectId": "f4001645-c27e-4e3b-92ee-1574191aa69e",
            "type": 1,
            "gdmc": "",
            "sort": 3,
            "name": "3"
        },
        {
            "id": "464def64-37b2-435e-8613-74dbbe78090a",
            "projectId": "f4001645-c27e-4e3b-92ee-1574191aa69e",
            "type": 3,
            "gdmc": "",
            "sort": 3,
            "name": "3"
        },
        {
            "id": "4ab4a52b-48b7-4f26-8b54-c824896a6b1d",
            "projectId": "f4001645-c27e-4e3b-92ee-1574191aa69e",
            "type": 1,
            "gdmc": "",
            "sort": 4,
            "name": "3"
        },
        {
            "id": "43aff6ad-2f90-4b86-b77e-b0e6a2886f87",
            "projectId": "f4001645-c27e-4e3b-92ee-1574191aa69e",
            "type": 2,
            "gdmc": "",
            "sort": 4,
            "name": "3"
        },
        {
            "id": "5ff75c14-0fa9-4655-90aa-ce9cb3517fd4",
            "projectId": "f4001645-c27e-4e3b-92ee-1574191aa69e",
            "type": 3,
            "gdmc": "",
            "sort": 5,
            "name": "3"
        },
        {
            "id": "3d9fa5bb-3e38-46a4-94de-513e9d785480",
            "projectId": "f4001645-c27e-4e3b-92ee-1574191aa69e",
            "type": 2,
            "gdmc": "",
            "sort": 5,
            "name": "3"
        },
        {
            "id": "63efaadd-c253-45f7-ac00-30ac31e30667",
            "projectId": "f4001645-c27e-4e3b-92ee-1574191aa69e",
            "type": 3,
            "gdmc": "",
            "sort": 6,
            "name": "3"
        },
        {
            "id": "dff87f7b-287a-45f2-995f-1715c0c33651",
            "projectId": "f4001645-c27e-4e3b-92ee-1574191aa69e",
            "type": 2,
            "gdmc": "",
            "sort": 6,
            "name": "3"
        },
        {
            "id": "e2b0ede9-d0e7-4441-94c3-43671f4b4edf",
            "projectId": "f4001645-c27e-4e3b-92ee-1574191aa69e",
            "type": 2,
            "gdmc": "",
            "sort": 7,
            "name": "3"
        },
        {
            "id": "95826bd3-0d19-4eed-b0bc-c4d8a9bcce85",
            "projectId": "f4001645-c27e-4e3b-92ee-1574191aa69e",
            "type": 3,
            "gdmc": "",
            "sort": 8,
            "name": "3"
        },
        {
            "id": "9cb75268-ac95-4872-8c5d-8bc17353e2db",
            "projectId": "f4001645-c27e-4e3b-92ee-1574191aa69e",
            "type": 3,
            "gdmc": "",
            "sort": 9,
            "name": "3"
        },
        {
            "id": "553f10d6-ee23-436f-8a57-fdeb156f7c6c",
            "projectId": "f4001645-c27e-4e3b-92ee-1574191aa69e",
            "type": 2,
            "gdmc": "",
            "sort": 10,
            "name": "3"
        },
        {
            "id": "1bf28663-e18a-4a96-9319-6078eb483cd0",
            "projectId": "f4001645-c27e-4e3b-92ee-1574191aa69e",
            "type": 3,
            "gdmc": "",
            "sort": 11,
            "name": "3"
        },
        {
            "id": "40265d6e-9582-4502-b2f6-47c1ae42efa9",
            "projectId": "f4001645-c27e-4e3b-92ee-1574191aa69e",
            "type": 3,
            "gdmc": "",
            "sort": 12,
            "name": "3"
        }
    ]
}
cookies = {}
with open("cookies.txt", 'r') as file:
    for line in file.read().split(';'):
        name, value = line.strip().split('=', 1)
        cookies[name] = value

requests = requests.post('http://localhost:8081/ydyl/submit/saveProjectTwo', data=json.dumps(data),
                         headers=headers,
                         cookies=cookies);

print(requests.text);
