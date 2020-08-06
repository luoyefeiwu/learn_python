# 保存
import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Content-Type': 'application/json; charset=UTF-8'
}
data = [
    {
        "projectDeclare": {
            "id": "61be814b-faff-408d-9e46-ec4cc628b5d3",
            "xmbm": "cd8e93e9-1802-44cf-bd52-76883e9b5a58",
            "name": "18888888888",
            "type": "A",
            "investmentType": "并购",
            "constructionType": "",
            "projectDebriefing": "意向谋划",
            "projectDebriefingDetial": "18888888888.22222",
            "bjdsfzc": 2,
            "jfknqk": "",
            "kxwjqqk": "",
            "yyknqk": "",
            "yytcqk": "",
            "assess": 1,
            "assessContent": "18888888888",
            "assessExplanation": "18888888888",
            "standard": 0,
            "gbhdz": "AE",
            "dz": "Asia",
            "province": "AE-AZ*",
            "address": "18888888888",
            "realm": "A0002",
            "industry": "商贸会展中心",
            "twoIndustry": "",
            "jsnrhmb": "18888888888",
            "xmjhztz": 1.888888888822E10,
            "xmdwzje": 1.0,
            "xmwczje": 1.0,
            "xmzqzje": 1.0,
            "xmgqzje": 1.0,
            "lwyyqk": "无偿援助",
            "lwyyqkje": 1.888888888822E10,
            "lwyyqkwxje": 0.0,
            "lwyyqkywje": 0.0,
            "lwyyqkqxyw": 0,
            "zddbjkqk": 2,
            "yhckmfxd": 2,
            "qttjdw": 2,
            "qttjdwqc": "",
            "bsdwqc": "地方发改委",
            "mlwt": "政局变动,资金困难",
            "mlwtms": "18888888888.22222",
            "xybgzkl": "18888888888.22222",
            "sjkgsj": "2020-06-09",
            "sjwgsj": "2020-06-09",
            "pshjq": 2,
            "pshjqms": "",
            "gfltcgqd": 2,
            "gfltcgqdms": "",
            "dsfhz": 2,
            "dsfhzms": "",
            "xcld": 2,
            "xcldms": "",
            "discountPolicy": "",
            "countryDiscountPolicy": "2",
            "chinaDiscountPolicy": "1",
            "projectSignificance": "18888888888",
            "isShareInfo": 2,
            "chinaGqzb": "1",
            "projectGqzb": "1",
            "otherGqzb": "1",
            "chinaZqzb": "1",
            "projectZqzb": "1",
            "otherZqzb": "1",
            "gardenNum": "",
            "gardenAmount": "",
            "createJobNum": "",
            "taxAmount": "",
            "turnover": 0.0,
            "profit": 0.0,
            "createId": "BFA831DB0000000072B933040000000E",
            "createName": "北京发改委",
            "createDate": "2020-06-24",
            "updateId": "BFA831DB0000000072B933040000000E",
            "updateName": "北京发改委",
            "updateDate": "2020-06-26",
            "isSubmit": 1,
            "stage": 2,
            "isNewProject": 1
        },
        "projcectLnvestments": [
            {
                "id": "7578b042-2a57-4385-bf64-12dac6be47c7",
                "projectId": "61be814b-faff-408d-9e46-ec4cc628b5d3",
                "tzdwmcName": "18888888888",
                "btzdwmcName": "18888888888",
                "sort": 1
            }
        ],
        "projectConstructions": [
            {
                "id": "1955a47b-df2d-42e7-92c0-a0da83de8757",
                "projectId": "61be814b-faff-408d-9e46-ec4cc628b5d3",
                "yzdwName": "",
                "jsdwName": "",
                "address": "",
                "sort": 1
            }
        ],
        "projectGqgcs": [
            {
                "id": "361962ae-cc9e-4664-96ba-7a0bed9e6dca",
                "projectId": "61be814b-faff-408d-9e46-ec4cc628b5d3",
                "type": 3,
                "gdmc": "18888888888.22222",
                "sort": 3
            },
            {
                "id": "5d2672dc-9ab8-4446-8f97-addf4306b8e0",
                "projectId": "61be814b-faff-408d-9e46-ec4cc628b5d3",
                "type": 1,
                "gdmc": "18888888888.22222",
                "sort": 1
            },
            {
                "id": "5daa72a2-f152-4288-a5ce-2b2b190b9c46",
                "projectId": "61be814b-faff-408d-9e46-ec4cc628b5d3",
                "type": 2,
                "gdmc": "18888888888.22222",
                "sort": 2
            }
        ],
        "projectXmfxes": [
            {
                "id": "c7fbaf86-5c10-4e8f-bea5-e1bbd24e2851",
                "projectId": "61be814b-faff-408d-9e46-ec4cc628b5d3",
                "fxType": "政治风险",
                "fxcd": "7",
                "description": "18888888888.22222",
                "sort": 1
            }
        ],
        "projectXmlxrs": [
            {
                "id": "569b4508-e662-4a3e-b993-ad98100cf1cf",
                "projectId": "61be814b-faff-408d-9e46-ec4cc628b5d3",
                "name": "18888888888",
                "phone": "18888888888",
                "type": 4,
                "sort": 4
            },
            {
                "id": "91b9b6f6-73c4-411c-8225-ffb8233509af",
                "projectId": "61be814b-faff-408d-9e46-ec4cc628b5d3",
                "name": "18888888888",
                "phone": "18888888888",
                "type": 2,
                "sort": 2
            },
            {
                "id": "c05c7f49-94f7-49f6-8cf2-395f1e6e40b8",
                "projectId": "61be814b-faff-408d-9e46-ec4cc628b5d3",
                "name": "18888888888",
                "phone": "18888888888",
                "type": 1,
                "sort": 1
            },
            {
                "id": "e5a15ad6-1131-4c6c-8a7f-c20f78877a0c",
                "projectId": "61be814b-faff-408d-9e46-ec4cc628b5d3",
                "name": "18888888888",
                "phone": "18888888888",
                "type": 3,
                "sort": 3
            }
        ],
        "projectZqgcs": [
            {
                "id": "6ce1b0d4-a155-4970-b349-ce15fc588ac3",
                "projectId": "61be814b-faff-408d-9e46-ec4cc628b5d3",
                "type": 3,
                "gdmc": "18888888888.22222",
                "sort": 3
            },
            {
                "id": "952e03ee-95b6-481f-b25c-a31ae6efc965",
                "projectId": "61be814b-faff-408d-9e46-ec4cc628b5d3",
                "type": 1,
                "gdmc": "18888888888.22222",
                "sort": 1
            },
            {
                "id": "c1372c1d-81c3-4925-a6c5-c1e5692238c3",
                "projectId": "61be814b-faff-408d-9e46-ec4cc628b5d3",
                "type": 2,
                "gdmc": "18888888888.22222",
                "sort": 2
            }
        ]
    },
    {
        "projectDeclare": {
            "id": "ba747bc9-5824-45af-910a-60774d8459fa",
            "xmbm": "7e74478c-f308-46a4-9b4d-32e6702258a8",
            "name": "测试纵网",
            "type": "A,B",
            "investmentType": "绿地投资",
            "constructionType": "设计施工",
            "projectDebriefing": "意向谋划",
            "projectDebriefingDetial": "12",
            "bjdsfzc": 1,
            "jfknqk": "",
            "kxwjqqk": "",
            "yyknqk": "",
            "yytcqk": "",
            "assess": 3,
            "assessContent": "",
            "assessExplanation": "",
            "standard": 0,
            "gbhdz": "C001",
            "dz": "A1",
            "province": "E001",
            "address": "济南",
            "realm": "A0006",
            "industry": "",
            "twoIndustry": "普通",
            "jsnrhmb": "12",
            "xmjhztz": 123.0,
            "cjqshte": 123.0,
            "xmdwzje": 123.0,
            "xmwczje": 123.0,
            "xmzqzje": 12.0,
            "xmgqzje": 123.0,
            "lwyyqk": ",无偿援助,无息贷款,援外优惠贷款",
            "lwyyqkje": 12.0,
            "lwyyqkwxje": 0.0,
            "lwyyqkywje": 0.0,
            "lwyyqkqx": 12,
            "lwyyqkqxyw": 0,
            "lwyyqknhll": 12.0,
            "zddbjkqk": 1,
            "zddbjkje": 12.0,
            "yhckmfxd": 1,
            "yhckmfxdje": 12.0,
            "yhckmfxdqx": 12,
            "yhckmfxdnhll": 12,
            "qttjdw": 2,
            "qttjdwqc": "",
            "bsdwqc": "地方发改委",
            "mlwt": "政局变动",
            "mlwtms": "12",
            "xybgzkl": "12",
            "sjkgsj": "2020-06-22",
            "sjwgsj": "2020-06-22",
            "pshjq": 2,
            "pshjqms": "",
            "gfltcgqd": 2,
            "gfltcgqdms": "",
            "dsfhz": 2,
            "dsfhzms": "",
            "xcld": 2,
            "xcldms": "",
            "discountPolicy": "",
            "countryDiscountPolicy": "1",
            "chinaDiscountPolicy": "1",
            "projectSignificance": "123",
            "isShareInfo": 2,
            "chinaGqzb": "1",
            "projectGqzb": "1",
            "otherGqzb": "1",
            "chinaZqzb": "12",
            "projectZqzb": "1",
            "otherZqzb": "1",
            "gardenNum": "",
            "gardenAmount": "",
            "createJobNum": "",
            "taxAmount": "",
            "turnover": 0.0,
            "profit": 0.0,
            "createId": "BFA831DB0000000072B933040000000E",
            "createName": "北京发改委",
            "createDate": "2020-06-19",
            "updateId": "BFA831DB0000000072B933040000000E",
            "updateName": "北京发改委",
            "updateDate": "2020-06-23",
            "isSubmit": 1,
            "stage": 2,
            "isNewProject": 1
        },
        "projcectLnvestments": [
            {
                "id": "247977d8-5689-45b3-ab9c-42f0fb0215a9",
                "projectId": "ba747bc9-5824-45af-910a-60774d8459fa",
                "tzdwmcName": "123",
                "btzdwmcName": "123",
                "sort": 2
            },
            {
                "id": "548019cf-73d6-4e4f-b3fa-1a8cf80b8938",
                "projectId": "ba747bc9-5824-45af-910a-60774d8459fa",
                "tzdwmcName": "12",
                "btzdwmcName": "12",
                "sort": 1
            }
        ],
        "projectConstructions": [
            {
                "id": "4f5b53b9-e450-4f43-a271-1a3cddf952dd",
                "projectId": "ba747bc9-5824-45af-910a-60774d8459fa",
                "yzdwName": "123",
                "jsdwName": "123",
                "address": "123",
                "sort": 1
            },
            {
                "id": "e763b225-f8d6-492b-8d31-8a255f808514",
                "projectId": "ba747bc9-5824-45af-910a-60774d8459fa",
                "yzdwName": "123",
                "jsdwName": "123",
                "address": "123",
                "sort": 2
            }
        ],
        "projectGqgcs": [
            {
                "id": "3ea2feb9-8c05-4c5a-ae06-5ae168d39174",
                "projectId": "ba747bc9-5824-45af-910a-60774d8459fa",
                "type": 1,
                "gdmc": "`12`21",
                "sort": 4
            },
            {
                "id": "5ca556e5-65fa-46f4-8cc0-6f1845c03a5d",
                "projectId": "ba747bc9-5824-45af-910a-60774d8459fa",
                "type": 1,
                "gdmc": "`12",
                "sort": 3
            },
            {
                "id": "99a7f402-93a1-479d-b286-8bd58ca2ce67",
                "projectId": "ba747bc9-5824-45af-910a-60774d8459fa",
                "type": 1,
                "gdmc": "`12",
                "sort": 2
            },
            {
                "id": "be6c605c-aff9-4a14-bafb-b17fa97f7d92",
                "projectId": "ba747bc9-5824-45af-910a-60774d8459fa",
                "type": 3,
                "gdmc": "12",
                "sort": 1
            }
        ],
        "projectXmfxes": [
            {
                "id": "5d02fff2-8aaa-4ea3-98b7-ece5b31a9c7d",
                "projectId": "ba747bc9-5824-45af-910a-60774d8459fa",
                "fxType": "政治风险",
                "fxcd": "4",
                "description": "12",
                "sort": 1
            },
            {
                "id": "d8802f3f-5858-49a7-aee5-80047532b1b7",
                "projectId": "ba747bc9-5824-45af-910a-60774d8459fa",
                "fxType": "生态坏境风险",
                "fxcd": "7",
                "description": "12",
                "sort": 2
            }
        ],
        "projectXmlxrs": [
            {
                "id": "06153109-1100-4710-b4ff-f990bcbb20e4",
                "projectId": "ba747bc9-5824-45af-910a-60774d8459fa",
                "name": "123",
                "phone": "18500392662",
                "type": 3,
                "sort": 3
            },
            {
                "id": "226ffa77-7ae0-41d9-8471-023e78775834",
                "projectId": "ba747bc9-5824-45af-910a-60774d8459fa",
                "name": "122",
                "phone": "18500392662",
                "type": 2,
                "sort": 2
            },
            {
                "id": "6040a5de-8e41-4f68-be27-e6ff0a242b44",
                "projectId": "ba747bc9-5824-45af-910a-60774d8459fa",
                "name": "12·",
                "phone": "18500392662",
                "type": 1,
                "sort": 1
            },
            {
                "id": "e0fa64f0-18df-42ba-82fb-133bd319523c",
                "projectId": "ba747bc9-5824-45af-910a-60774d8459fa",
                "name": "124",
                "phone": "18500392662",
                "type": 4,
                "sort": 4
            }
        ],
        "projectZqgcs": [
            {
                "id": "396fc3a3-7ebe-40e0-9787-c60c4ba8ce2b",
                "projectId": "ba747bc9-5824-45af-910a-60774d8459fa",
                "type": 3,
                "gdmc": "12",
                "sort": 1
            }
        ]
    },
    {
        "projectDeclare": {
            "id": "1f70caad-58dc-4bb4-8bd3-e9421c69def7",
            "xmbm": "dc778c43-6ace-4a5e-8ceb-56207c1bea92",
            "name": "我是新建项目",
            "type": "",
            "investmentType": "并购",
            "constructionType": "",
            "projectDebriefing": "建前筹备",
            "projectDebriefingDetial": "123",
            "bjdsfzc": 1,
            "jfknqk": "",
            "kxwjqqk": "",
            "yyknqk": "",
            "yytcqk": "",
            "assess": 1,
            "assessContent": "阿斯蒂",
            "assessExplanation": " 阿斯蒂",
            "standard": 0,
            "gbhdz": "C001",
            "dz": "A1",
            "province": "E001",
            "address": "济南hj",
            "realm": "A0001",
            "industry": "B0001",
            "twoIndustry": "普通",
            "jsnrhmb": "按市场",
            "xmjhztz": 126.0,
            "xmdwzje": 123.0,
            "xmwczje": 123.0,
            "xmzqzje": 45.0,
            "xmgqzje": 12.0,
            "lwyyqk": "无偿援助",
            "lwyyqkje": 12.0,
            "lwyyqkwxje": 0.0,
            "lwyyqkywje": 0.0,
            "lwyyqkqxyw": 0,
            "zddbjkqk": 2,
            "yhckmfxd": 2,
            "qttjdw": 2,
            "qttjdwqc": "",
            "bsdwqc": "地方发改委",
            "mlwt": "政局变动",
            "mlwtms": "123",
            "xybgzkl": "123",
            "sjkgsj": "2020-06-18",
            "sjwgsj": "2020-06-18",
            "pshjq": 2,
            "pshjqms": "",
            "gfltcgqd": 2,
            "gfltcgqdms": "",
            "dsfhz": 2,
            "dsfhzms": "",
            "xcld": 2,
            "xcldms": "",
            "discountPolicy": "",
            "countryDiscountPolicy": "1,2",
            "chinaDiscountPolicy": "2",
            "projectSignificance": "阿斯蒂",
            "isShareInfo": 2,
            "chinaGqzb": "12",
            "projectGqzb": "12",
            "otherGqzb": "12",
            "chinaZqzb": "12",
            "projectZqzb": "12",
            "otherZqzb": "12",
            "gardenNum": "",
            "gardenAmount": "",
            "createJobNum": "",
            "taxAmount": "",
            "turnover": 0.0,
            "profit": 0.0,
            "createId": "BFA831DB0000000072B933040000000E",
            "createName": "北京发改委",
            "createDate": "2020-06-18",
            "updateId": "BFA831DB0000000072B933040000000E",
            "updateName": "北京发改委",
            "updateDate": "2020-06-23",
            "isSubmit": 1,
            "stage": 2,
            "isNewProject": 1
        },
        "projcectLnvestments": [
            {
                "id": "9232d471-53b7-4002-9002-b80b7e35927a",
                "projectId": "1f70caad-58dc-4bb4-8bd3-e9421c69def7",
                "tzdwmcName": "12",
                "btzdwmcName": "123",
                "sort": 1
            }
        ],
        "projectConstructions": [
            {
                "id": "95d710b7-6b34-4313-8629-bfec87ea614b",
                "projectId": "1f70caad-58dc-4bb4-8bd3-e9421c69def7",
                "yzdwName": "",
                "jsdwName": "",
                "address": "",
                "sort": 1
            }
        ],
        "projectGqgcs": [
            {
                "id": "7ffcdafb-320a-45f6-9dc4-1188bef1d8d0",
                "projectId": "1f70caad-58dc-4bb4-8bd3-e9421c69def7",
                "type": 1,
                "gdmc": "12",
                "sort": 1
            },
            {
                "id": "d6e88ed4-e521-4da8-855d-4989f2960e75",
                "projectId": "1f70caad-58dc-4bb4-8bd3-e9421c69def7",
                "type": 2,
                "gdmc": "12",
                "sort": 2
            },
            {
                "id": "e5355612-0add-4255-8f83-8a2d82b17978",
                "projectId": "1f70caad-58dc-4bb4-8bd3-e9421c69def7",
                "type": 3,
                "gdmc": "123",
                "sort": 3
            }
        ],
        "projectXmfxes": [
            {
                "id": "c2965649-b564-48dd-a0b3-8bbf62e3ca3c",
                "projectId": "1f70caad-58dc-4bb4-8bd3-e9421c69def7",
                "fxType": "生态坏境风险",
                "fxcd": "7",
                "description": "123",
                "sort": 1
            }
        ],
        "projectXmlxrs": [
            {
                "id": "36f73644-781c-4ea4-980b-6e846b4a58bb",
                "projectId": "1f70caad-58dc-4bb4-8bd3-e9421c69def7",
                "name": "阿达",
                "phone": "18500392662",
                "type": 1,
                "sort": 1
            },
            {
                "id": "36f79063-8263-45a4-bd2c-43d46aecdace",
                "projectId": "1f70caad-58dc-4bb4-8bd3-e9421c69def7",
                "name": "阿达",
                "phone": "18500392662",
                "type": 2,
                "sort": 2
            },
            {
                "id": "55f8e29f-d9aa-4aa1-ade6-c03b2c8bc51e",
                "projectId": "1f70caad-58dc-4bb4-8bd3-e9421c69def7",
                "name": "阿达",
                "phone": "18500392662",
                "type": 3,
                "sort": 3
            },
            {
                "id": "efb58092-9129-44b0-b4ef-83efa38f5eda",
                "projectId": "1f70caad-58dc-4bb4-8bd3-e9421c69def7",
                "name": "阿达",
                "phone": "18500392662",
                "type": 4,
                "sort": 4
            }
        ],
        "projectZqgcs": [
            {
                "id": "4889b0bb-4344-4a95-9e20-86917747169f",
                "projectId": "1f70caad-58dc-4bb4-8bd3-e9421c69def7",
                "type": 1,
                "gdmc": "12",
                "sort": 1
            },
            {
                "id": "563a5db4-ac73-4fce-bf77-0593a7b185bb",
                "projectId": "1f70caad-58dc-4bb4-8bd3-e9421c69def7",
                "type": 3,
                "gdmc": "12",
                "sort": 3
            },
            {
                "id": "64cb3089-d1f9-41f4-b8de-bfa0db431f0c",
                "projectId": "1f70caad-58dc-4bb4-8bd3-e9421c69def7",
                "type": 2,
                "gdmc": "12",
                "sort": 2
            }
        ]
    },
    {
        "projectDeclare": {
            "id": "be009293-eaff-4e82-b225-f8cece6ed4dc",
            "xmbm": "2bf83884-4d19-4836-9488-4f479a83c80e",
            "name": "我是测试项目报送0615",
            "type": "A,B",
            "investmentType": "绿地投资",
            "constructionType": "施工承包",
            "projectDebriefing": "建前筹备",
            "projectDebriefingDetial": "314",
            "bjdsfzc": 1,
            "jfknqk": "",
            "kxwjqqk": "",
            "yyknqk": "",
            "yytcqk": "",
            "assess": 5,
            "assessContent": "123",
            "assessExplanation": "123",
            "standard": 0,
            "gbhdz": "AD",
            "dz": "Europe",
            "province": "AD-02*",
            "address": "济南",
            "realm": "A0003",
            "industry": "建筑",
            "twoIndustry": "",
            "jsnrhmb": "阿斯蒂芬",
            "xmjhztz": 123.0,
            "cjqshte": 123.0,
            "xmdwzje": 123.0,
            "xmwczje": 123123.0,
            "xmzqzje": 123.0,
            "xmgqzje": 123.0,
            "lwyyqk": "无偿援助,无息贷款,援外优惠贷款",
            "lwyyqkje": 12.0,
            "lwyyqkwxje": 0.0,
            "lwyyqkywje": 0.0,
            "lwyyqkqx": 123,
            "lwyyqkqxyw": 0,
            "lwyyqknhll": 123.0,
            "zddbjkqk": 1,
            "zddbjkje": 123.0,
            "yhckmfxd": 1,
            "yhckmfxdje": 123.0,
            "yhckmfxdqx": 123,
            "yhckmfxdnhll": 123,
            "qttjdw": 1,
            "qttjdwqc": "123",
            "bsdwqc": "123123",
            "mlwt": "政局变动,资金困难,征地拆迁缓慢",
            "mlwtms": "123",
            "xybgzkl": "123",
            "sjkgsj": "2020-06-15",
            "sjwgsj": "2020-06-15",
            "pshjq": 1,
            "pshjqms": "收到",
            "gfltcgqd": 1,
            "gfltcgqdms": "请问",
            "dsfhz": 1,
            "dsfhzms": "收到",
            "xcld": 2,
            "xcldms": "请问",
            "discountPolicy": "",
            "countryDiscountPolicy": "1,2,3,4",
            "chinaDiscountPolicy": "1,2,3",
            "projectSignificance": "请问请问",
            "isShareInfo": 2,
            "chinaGqzb": "2",
            "projectGqzb": "12",
            "otherGqzb": "12",
            "chinaZqzb": "2",
            "projectZqzb": "12",
            "otherZqzb": "1",
            "gardenNum": "",
            "gardenAmount": "",
            "createJobNum": "",
            "taxAmount": "",
            "turnover": 0.0,
            "profit": 0.0,
            "createId": "BFA831DB0000000072B97A8A00000010",
            "createName": "张三",
            "createDate": "2020-06-15",
            "updateId": "BFA831DB0000000072B933040000000E",
            "updateName": "北京发改委",
            "updateDate": "2020-06-26",
            "isSubmit": 1,
            "stage": 3,
            "isNewProject": 1
        },
        "projcectLnvestments": [
            {
                "id": "b6778fca-69d6-4fd2-bd1e-5ea0ad0dcb80",
                "projectId": "be009293-eaff-4e82-b225-f8cece6ed4dc",
                "tzdwmcName": "投资2",
                "btzdwmcName": "被投资2",
                "sort": 2
            },
            {
                "id": "f44f86c0-6757-4b2f-8384-e5fc40b9e6d5",
                "projectId": "be009293-eaff-4e82-b225-f8cece6ed4dc",
                "tzdwmcName": "投资1",
                "btzdwmcName": "被投资1",
                "sort": 1
            }
        ],
        "projectConstructions": [
            {
                "id": "6cf3546b-1ac9-4220-b263-71f2cc891b5e",
                "projectId": "be009293-eaff-4e82-b225-f8cece6ed4dc",
                "yzdwName": "业主单位名称2",
                "jsdwName": "建设单位名称2",
                "address": "北京",
                "sort": 2
            },
            {
                "id": "b474ba28-b4a9-4985-a7a3-9b37fc5994cd",
                "projectId": "be009293-eaff-4e82-b225-f8cece6ed4dc",
                "yzdwName": "业主单位名称1",
                "jsdwName": " 建设单位名称1",
                "address": "北京",
                "sort": 1
            }
        ],
        "projectGqgcs": [
            {
                "id": "6715e1bf-087e-4d28-9510-791c9790af94",
                "projectId": "be009293-eaff-4e82-b225-f8cece6ed4dc",
                "type": 1,
                "gdmc": "123",
                "sort": 1
            },
            {
                "id": "77488b37-bd03-42b2-8315-5bf925268434",
                "projectId": "be009293-eaff-4e82-b225-f8cece6ed4dc",
                "type": 3,
                "gdmc": "13",
                "sort": 3
            },
            {
                "id": "b4f5130f-7ca6-4441-8762-ec4e67a03725",
                "projectId": "be009293-eaff-4e82-b225-f8cece6ed4dc",
                "type": 2,
                "gdmc": "12",
                "sort": 2
            }
        ],
        "projectXmfxes": [
            {
                "id": "1835ce4c-cfa0-437b-aba8-011647f8edf0",
                "projectId": "be009293-eaff-4e82-b225-f8cece6ed4dc",
                "fxType": "政治风险",
                "fxcd": "1",
                "description": "123",
                "sort": 1
            },
            {
                "id": "5455c114-4674-4aea-b52c-4f32e6d73e42",
                "projectId": "be009293-eaff-4e82-b225-f8cece6ed4dc",
                "fxType": "安全风险",
                "fxcd": "5",
                "description": "123",
                "sort": 2
            },
            {
                "id": "83f719f4-65da-4d75-b196-c1fa248adeb7",
                "projectId": "be009293-eaff-4e82-b225-f8cece6ed4dc",
                "fxType": "经济风险",
                "fxcd": "9",
                "description": "1231",
                "sort": 3
            }
        ],
        "projectXmlxrs": [
            {
                "id": "53388e97-d8ab-498e-a926-fd427df880a8",
                "projectId": "be009293-eaff-4e82-b225-f8cece6ed4dc",
                "name": "的",
                "phone": "18500392663",
                "type": 3,
                "sort": 3
            },
            {
                "id": "77d99f02-deb6-466b-869f-ebbd9faf0bc9",
                "projectId": "be009293-eaff-4e82-b225-f8cece6ed4dc",
                "name": "123",
                "phone": "18500392663",
                "type": 2,
                "sort": 2
            },
            {
                "id": "c4de02fc-b404-4cd8-bc02-64a7705f67da",
                "projectId": "be009293-eaff-4e82-b225-f8cece6ed4dc",
                "name": "123",
                "phone": "18500392662",
                "type": 1,
                "sort": 1
            }
        ],
        "projectZqgcs": [
            {
                "id": "2f0fc223-3e89-459b-a68e-833fca29e71e",
                "projectId": "be009293-eaff-4e82-b225-f8cece6ed4dc",
                "type": 1,
                "gdmc": "123",
                "sort": 1
            },
            {
                "id": "85aa5924-0cf5-4482-abb5-69ec8b258266",
                "projectId": "be009293-eaff-4e82-b225-f8cece6ed4dc",
                "type": 3,
                "gdmc": "123",
                "sort": 3
            },
            {
                "id": "b944574c-7a0b-4362-86db-f6bdd78c5246",
                "projectId": "be009293-eaff-4e82-b225-f8cece6ed4dc",
                "type": 2,
                "gdmc": "123",
                "sort": 2
            }
        ]
    },
    {
        "projectDeclare": {
            "id": "b32a771f-a534-40ca-9b36-5a0071f56e39",
            "xmbm": "62039ed5-7ae4-44fc-a74d-17e7f622a66c",
            "name": "项目名称",
            "type": "A",
            "investmentType": "并购",
            "constructionType": "",
            "projectDebriefing": "意向谋划",
            "projectDebriefingDetial": "测试",
            "bjdsfzc": 2,
            "jfknqk": "",
            "kxwjqqk": "",
            "yyknqk": "",
            "yytcqk": "",
            "assess": 5,
            "assessContent": "测试",
            "assessExplanation": "测试",
            "standard": 0,
            "gbhdz": "D001",
            "dz": "B1",
            "province": "G001",
            "address": "测试",
            "realm": "A0004",
            "industry": "光伏发电",
            "twoIndustry": "",
            "jsnrhmb": "测试",
            "xmjhztz": 1.0,
            "cjqshte": 1.0,
            "xmdwzje": 1.0,
            "xmwczje": 1.0,
            "xmzqzje": 1.0,
            "xmgqzje": 1.0,
            "lwyyqk": "无偿援助,无息贷款,优惠援外贷款",
            "lwyyqkje": 1.0,
            "lwyyqkwxje": 0.0,
            "lwyyqkywje": 0.0,
            "lwyyqkqx": 1,
            "lwyyqkqxyw": 0,
            "lwyyqknhll": 1.0,
            "zddbjkqk": 1,
            "zddbjkje": 1.0,
            "yhckmfxd": 1,
            "yhckmfxdje": 1.0,
            "yhckmfxdqx": 1,
            "yhckmfxdnhll": 1,
            "qttjdw": 1,
            "qttjdwqc": "测试",
            "bsdwqc": "测试",
            "mlwt": "政局变动,资金困难,征地拆迁缓慢",
            "mlwtms": "测试测试",
            "xybgzkl": "测试",
            "sjkgsj": "2020-06-08",
            "sjwgsj": "2020-06-17",
            "pshjq": 2,
            "pshjqms": "测试",
            "gfltcgqd": 1,
            "gfltcgqdms": "测试测试测试",
            "dsfhz": 2,
            "dsfhzms": "测试测试测试",
            "xcld": 2,
            "xcldms": "测试测试",
            "discountPolicy": "",
            "countryDiscountPolicy": "1,2,3",
            "chinaDiscountPolicy": "1,2",
            "projectSignificance": "测试",
            "isShareInfo": 2,
            "chinaGqzb": "1",
            "projectGqzb": "1",
            "otherGqzb": "1",
            "chinaZqzb": "1",
            "projectZqzb": "1",
            "otherZqzb": "1",
            "gardenNum": "",
            "gardenAmount": "",
            "createJobNum": "",
            "taxAmount": "",
            "turnover": 0.0,
            "profit": 0.0,
            "createId": "BFA831DB0000000072B97A8A00000010",
            "createName": "张三",
            "createDate": "2020-06-15",
            "updateId": "BFA831DB0000000072B933040000000E",
            "updateName": "北京发改委",
            "updateDate": "2020-06-19",
            "isSubmit": 1,
            "stage": 3,
            "isNewProject": 1
        },
        "projcectLnvestments": [
            {
                "id": "196f0233-fc8d-48e0-9d41-986809f40242",
                "projectId": "b32a771f-a534-40ca-9b36-5a0071f56e39",
                "tzdwmcName": "测试",
                "btzdwmcName": "测试",
                "sort": 1
            },
            {
                "id": "5cec322a-9bd3-47f8-be73-deb1a62ba09f",
                "projectId": "b32a771f-a534-40ca-9b36-5a0071f56e39",
                "tzdwmcName": "测试",
                "btzdwmcName": "测试",
                "sort": 2
            },
            {
                "id": "e9da9f19-139c-4d85-b275-faa8c2c68ea0",
                "projectId": "b32a771f-a534-40ca-9b36-5a0071f56e39",
                "tzdwmcName": "测试",
                "btzdwmcName": "测试",
                "sort": 3
            }
        ],
        "projectConstructions": [
            {
                "id": "decc205d-1a77-434c-80bd-aaa3011fdfbc",
                "projectId": "b32a771f-a534-40ca-9b36-5a0071f56e39",
                "yzdwName": "",
                "jsdwName": "",
                "address": "",
                "sort": 1
            }
        ],
        "projectGqgcs": [
            {
                "id": "1cea88cb-c959-45ae-a608-bc47b06777f5",
                "projectId": "b32a771f-a534-40ca-9b36-5a0071f56e39",
                "type": 2,
                "gdmc": "测试",
                "sort": 2
            },
            {
                "id": "3a5e7126-1b69-49fe-8c36-868446512517",
                "projectId": "b32a771f-a534-40ca-9b36-5a0071f56e39",
                "type": 2,
                "gdmc": "测试",
                "sort": 5
            },
            {
                "id": "528e6bd1-1c0c-449b-bb3d-e258576ef997",
                "projectId": "b32a771f-a534-40ca-9b36-5a0071f56e39",
                "type": 2,
                "gdmc": "测试",
                "sort": 6
            },
            {
                "id": "70c3482f-b930-41cf-977c-47b1ba1a99cf",
                "projectId": "b32a771f-a534-40ca-9b36-5a0071f56e39",
                "type": 3,
                "gdmc": "测试",
                "sort": 7
            },
            {
                "id": "7e508fe3-f384-4572-a6a8-30420f75957c",
                "projectId": "b32a771f-a534-40ca-9b36-5a0071f56e39",
                "type": 1,
                "gdmc": "测试",
                "sort": 4
            },
            {
                "id": "9228e4d0-d518-4fd4-b188-b8f815ddf4c4",
                "projectId": "b32a771f-a534-40ca-9b36-5a0071f56e39",
                "type": 1,
                "gdmc": "测试",
                "sort": 1
            },
            {
                "id": "f4de1374-188a-46b5-92ba-a37a53697661",
                "projectId": "b32a771f-a534-40ca-9b36-5a0071f56e39",
                "type": 3,
                "gdmc": "测试",
                "sort": 3
            }
        ],
        "projectXmfxes": [
            {
                "id": "43c00171-f509-498b-b7f9-4e734f2f49c3",
                "projectId": "b32a771f-a534-40ca-9b36-5a0071f56e39",
                "fxType": "安全风险",
                "fxcd": "6",
                "description": "测试",
                "sort": 2
            },
            {
                "id": "82b54869-6185-44fa-baba-68448d504818",
                "projectId": "b32a771f-a534-40ca-9b36-5a0071f56e39",
                "fxType": "政治风险",
                "fxcd": "5",
                "description": "测试",
                "sort": 1
            },
            {
                "id": "9fbf7b23-0355-4a7b-80ee-c52441da12fd",
                "projectId": "b32a771f-a534-40ca-9b36-5a0071f56e39",
                "fxType": "企业运营风险",
                "fxcd": "6",
                "description": "测试",
                "sort": 4
            },
            {
                "id": "ba4cb21b-9227-4be4-a04e-fc529f540ea5",
                "projectId": "b32a771f-a534-40ca-9b36-5a0071f56e39",
                "fxType": "经济风险",
                "fxcd": "6",
                "description": "测试",
                "sort": 3
            }
        ],
        "projectXmlxrs": [
            {
                "id": "1661052b-786d-48de-88c7-1bf0f6ef7398",
                "projectId": "b32a771f-a534-40ca-9b36-5a0071f56e39",
                "name": "测试",
                "phone": "18888888888",
                "type": 2,
                "sort": 2
            },
            {
                "id": "4e30fb68-c86b-43a4-ae69-dc75f13c5042",
                "projectId": "b32a771f-a534-40ca-9b36-5a0071f56e39",
                "name": "测试",
                "phone": "18888888888",
                "type": 1,
                "sort": 4
            },
            {
                "id": "63b38a85-30eb-48e2-9451-ed1df4fc1457",
                "projectId": "b32a771f-a534-40ca-9b36-5a0071f56e39",
                "name": "12",
                "phone": "18888888888",
                "type": 4,
                "sort": 7
            },
            {
                "id": "8472e002-76ca-4657-a18e-405a4ddbc82f",
                "projectId": "b32a771f-a534-40ca-9b36-5a0071f56e39",
                "name": "测试",
                "phone": "18888888888",
                "type": 2,
                "sort": 5
            },
            {
                "id": "c9aeff02-c3e0-4f65-9280-77d3ab1ab9d2",
                "projectId": "b32a771f-a534-40ca-9b36-5a0071f56e39",
                "name": "测试",
                "phone": "18888888888",
                "type": 3,
                "sort": 3
            },
            {
                "id": "f0f2e182-7e2c-489a-9d51-ff2d0ece2e5b",
                "projectId": "b32a771f-a534-40ca-9b36-5a0071f56e39",
                "name": "测试",
                "phone": "18888888888",
                "type": 1,
                "sort": 1
            },
            {
                "id": "f35fae8f-06ab-429a-82b6-e167b4aa5ca5",
                "projectId": "b32a771f-a534-40ca-9b36-5a0071f56e39",
                "name": "测试",
                "phone": "18888888888",
                "type": 3,
                "sort": 6
            }
        ],
        "projectZqgcs": [
            {
                "id": "169a4705-f257-4b34-9b18-bb644f66e048",
                "projectId": "b32a771f-a534-40ca-9b36-5a0071f56e39",
                "type": 1,
                "gdmc": "测试",
                "sort": 1
            },
            {
                "id": "1f489846-8f11-4675-a40e-41b9579cc0f9",
                "projectId": "b32a771f-a534-40ca-9b36-5a0071f56e39",
                "type": 2,
                "gdmc": "测试",
                "sort": 2
            },
            {
                "id": "2b492c20-0601-43e0-88cd-8d3b7c65ea29",
                "projectId": "b32a771f-a534-40ca-9b36-5a0071f56e39",
                "type": 3,
                "gdmc": "测试",
                "sort": 3
            },
            {
                "id": "6eed7533-6e22-4cc7-b065-93a368865fd1",
                "projectId": "b32a771f-a534-40ca-9b36-5a0071f56e39",
                "type": 1,
                "gdmc": "测试",
                "sort": 4
            },
            {
                "id": "6f188c65-41cb-4b75-9d25-78d211968fab",
                "projectId": "b32a771f-a534-40ca-9b36-5a0071f56e39",
                "type": 2,
                "gdmc": "测试",
                "sort": 5
            },
            {
                "id": "eb567227-0289-4aff-a34c-38222fd08df8",
                "projectId": "b32a771f-a534-40ca-9b36-5a0071f56e39",
                "type": 3,
                "gdmc": "测试",
                "sort": 6
            }
        ]
    },
    {
        "projectDeclare": {
            "id": "fd9ebb68-7cfe-4478-901b-498e0ef92241",
            "xmbm": "c0cff192-6b1d-43dc-a8b9-896e6dc9842f",
            "name": "1",
            "type": "B",
            "investmentType": "",
            "constructionType": "施工承包",
            "projectDebriefing": "建前筹备",
            "projectDebriefingDetial": "1",
            "bjdsfzc": 2,
            "jfknqk": "",
            "kxwjqqk": "",
            "yyknqk": "",
            "yytcqk": "",
            "assess": 4,
            "assessContent": "1",
            "assessExplanation": "1",
            "standard": 0,
            "gbhdz": "D001",
            "dz": "B1",
            "province": "G002",
            "address": "1",
            "realm": "A0008",
            "industry": "海上搜救",
            "twoIndustry": "",
            "jsnrhmb": "1",
            "xmjhztz": 1.8888888888E10,
            "cjqshte": 1.8888888888E10,
            "xmdwzje": 1.8888888888E10,
            "xmwczje": 1.8888888888E10,
            "xmzqzje": 1.0,
            "xmgqzje": 1.8888888888E10,
            "lwyyqk": "无",
            "lwyyqkwxje": 0.0,
            "lwyyqkywje": 0.0,
            "lwyyqkqxyw": 0,
            "zddbjkqk": 2,
            "yhckmfxd": 2,
            "qttjdw": 2,
            "qttjdwqc": "",
            "bsdwqc": "1",
            "mlwt": "资金困难",
            "mlwtms": "1",
            "xybgzkl": "1",
            "sjkgsj": "2020-06-09",
            "sjwgsj": "2020-06-24",
            "pshjq": 2,
            "pshjqms": "",
            "gfltcgqd": 2,
            "gfltcgqdms": "",
            "dsfhz": 2,
            "dsfhzms": "",
            "xcld": 2,
            "xcldms": "",
            "discountPolicy": "",
            "countryDiscountPolicy": "1",
            "chinaDiscountPolicy": "1",
            "projectSignificance": "1",
            "isShareInfo": 2,
            "chinaGqzb": "1",
            "projectGqzb": "1",
            "otherGqzb": "1",
            "chinaZqzb": "1",
            "projectZqzb": "1",
            "otherZqzb": "1",
            "gardenNum": "",
            "gardenAmount": "",
            "createJobNum": "",
            "taxAmount": "",
            "turnover": 0.0,
            "profit": 0.0,
            "createId": "BFA831DB0000000072B97A8A00000010",
            "createName": "张三",
            "createDate": "2020-06-15",
            "updateId": "BFA831DB0000000072B97A8A00000010",
            "updateName": "张三",
            "updateDate": "2020-06-15",
            "isSubmit": 1,
            "stage": 2,
            "isNewProject": 1
        },
        "projcectLnvestments": [
            {
                "id": "015e81e2-ac75-4b2b-b997-fea906f17b32",
                "projectId": "fd9ebb68-7cfe-4478-901b-498e0ef92241",
                "tzdwmcName": "",
                "btzdwmcName": "",
                "sort": 1
            }
        ],
        "projectConstructions": [
            {
                "id": "646cae8c-7a1e-4ec5-8fb9-f2c23f9e73b2",
                "projectId": "fd9ebb68-7cfe-4478-901b-498e0ef92241",
                "yzdwName": "1",
                "jsdwName": "1",
                "address": "1",
                "sort": 1
            }
        ],
        "projectGqgcs": [
            {
                "id": "6041d460-4ec2-44b2-bd7e-2b45cd172367",
                "projectId": "fd9ebb68-7cfe-4478-901b-498e0ef92241",
                "type": 1,
                "gdmc": "1",
                "sort": 1
            },
            {
                "id": "e0775cf4-61db-4c3e-bd49-1f5b91bb4a4d",
                "projectId": "fd9ebb68-7cfe-4478-901b-498e0ef92241",
                "type": 2,
                "gdmc": "1",
                "sort": 2
            },
            {
                "id": "f2ecc357-de85-4abe-985c-dbda78bae5c9",
                "projectId": "fd9ebb68-7cfe-4478-901b-498e0ef92241",
                "type": 3,
                "gdmc": "1",
                "sort": 3
            }
        ],
        "projectXmfxes": [
            {
                "id": "a302dc12-99de-4ead-8784-6ffaa194510e",
                "projectId": "fd9ebb68-7cfe-4478-901b-498e0ef92241",
                "fxType": "政治风险",
                "fxcd": "7",
                "description": "1",
                "sort": 1
            }
        ],
        "projectXmlxrs": [
            {
                "id": "87c37f03-2bca-4347-b3a2-a0e3eb5a1a22",
                "projectId": "fd9ebb68-7cfe-4478-901b-498e0ef92241",
                "name": "1",
                "phone": "18888888888",
                "type": 2,
                "sort": 2
            },
            {
                "id": "a483bc56-636c-40bb-8a29-65252c06525a",
                "projectId": "fd9ebb68-7cfe-4478-901b-498e0ef92241",
                "name": "1",
                "phone": "18888888888",
                "type": 1,
                "sort": 1
            },
            {
                "id": "d952b1db-05fb-4ac2-a1f9-b1fc335fd608",
                "projectId": "fd9ebb68-7cfe-4478-901b-498e0ef92241",
                "name": "1",
                "phone": "18888888888",
                "type": 3,
                "sort": 3
            }
        ],
        "projectZqgcs": [
            {
                "id": "93824b1b-ea3f-4b6a-a793-52f4352d2b3e",
                "projectId": "fd9ebb68-7cfe-4478-901b-498e0ef92241",
                "type": 3,
                "gdmc": "1",
                "sort": 3
            },
            {
                "id": "c347d0f5-a6ce-47ff-87a0-cb4d0299f482",
                "projectId": "fd9ebb68-7cfe-4478-901b-498e0ef92241",
                "type": 2,
                "gdmc": "1",
                "sort": 2
            },
            {
                "id": "d4dd4a8a-0d12-4e33-aa98-04f5bff981ba",
                "projectId": "fd9ebb68-7cfe-4478-901b-498e0ef92241",
                "type": 1,
                "gdmc": "1",
                "sort": 1
            }
        ]
    },
    {
        "projectDeclare": {
            "id": "675e9449-0f82-46f3-886d-640acc55559d",
            "xmbm": "2b5a394d-e538-4057-9d2d-c6d14b430b7f",
            "name": "测试001",
            "type": "A",
            "investmentType": "并购",
            "constructionType": "",
            "projectDebriefing": "建前筹备",
            "projectDebriefingDetial": "项目进展详情",
            "bjdsfzc": 1,
            "jfknqk": "",
            "kxwjqqk": "",
            "yyknqk": "",
            "yytcqk": "",
            "assess": 3,
            "assessContent": "其他",
            "assessExplanation": "严格",
            "standard": 0,
            "gbhdz": "C001",
            "dz": "A1",
            "province": "E001",
            "address": "济南市",
            "realm": "A0002",
            "industry": "境外合作区",
            "twoIndustry": "",
            "jsnrhmb": "目标",
            "xmjhztz": 10000.0,
            "cjqshte": 10000.0,
            "xmdwzje": 10000.0,
            "xmwczje": 30000.0,
            "xmzqzje": 2000.0,
            "xmgqzje": 203120.0,
            "lwyyqk": "无偿援助",
            "lwyyqkje": 10000.0,
            "lwyyqkwxje": 0.0,
            "lwyyqkywje": 0.0,
            "lwyyqkqxyw": 0,
            "zddbjkqk": 2,
            "yhckmfxd": 2,
            "qttjdw": 2,
            "qttjdwqc": "",
            "bsdwqc": "报送单位",
            "mlwt": "征地拆迁缓慢,签证效率低下,资金困难,政局变动",
            "mlwtms": "详情",
            "xybgzkl": "下一步",
            "sjkgsj": "2020-06-13",
            "sjwgsj": "2020-06-13",
            "pshjq": 1,
            "pshjqms": "批示",
            "gfltcgqd": 2,
            "gfltcgqdms": "",
            "dsfhz": 1,
            "dsfhzms": "第三方合作",
            "xcld": 2,
            "xcldms": "",
            "discountPolicy": "",
            "countryDiscountPolicy": "1,2",
            "chinaDiscountPolicy": "1,2",
            "projectSignificance": "项目意义",
            "isShareInfo": 2,
            "chinaGqzb": "30",
            "projectGqzb": "10",
            "otherGqzb": "10",
            "chinaZqzb": "10",
            "projectZqzb": "20",
            "otherZqzb": "30",
            "gardenNum": "",
            "gardenAmount": "",
            "createJobNum": "",
            "taxAmount": "",
            "turnover": 0.0,
            "profit": 0.0,
            "createId": "BFA831DB0000000072B97A8A00000010",
            "createName": "张三",
            "createDate": "2020-06-13",
            "updateId": "BFA831DB0000000072B933040000000E",
            "updateName": "北京发改委",
            "updateDate": "2020-06-24",
            "isSubmit": 1,
            "stage": 3,
            "isNewProject": 1
        },
        "projcectLnvestments": [
            {
                "id": "75214fdb-3c56-4497-9947-fa6c701b1024",
                "projectId": "675e9449-0f82-46f3-886d-640acc55559d",
                "tzdwmcName": "浪潮",
                "btzdwmcName": "有生",
                "sort": 1
            }
        ],
        "projectConstructions": [
            {
                "id": "5c774879-2b8f-4b49-a9b6-2be8c45b6df8",
                "projectId": "675e9449-0f82-46f3-886d-640acc55559d",
                "yzdwName": "",
                "jsdwName": "",
                "address": "",
                "sort": 1
            }
        ],
        "projectGqgcs": [
            {
                "id": "a5146062-62a0-445f-862d-829b06342639",
                "projectId": "675e9449-0f82-46f3-886d-640acc55559d",
                "type": 2,
                "gdmc": "所在国股份",
                "sort": 2
            },
            {
                "id": "b1c109e1-aa87-47f9-b639-adc9fca5f195",
                "projectId": "675e9449-0f82-46f3-886d-640acc55559d",
                "type": 1,
                "gdmc": "中方股东",
                "sort": 1
            },
            {
                "id": "ce67bffe-eaf5-4070-b8d9-0198547ac9ea",
                "projectId": "675e9449-0f82-46f3-886d-640acc55559d",
                "type": 3,
                "gdmc": "第三方股份",
                "sort": 3
            }
        ],
        "projectXmfxes": [
            {
                "id": "4c25cf94-7270-4aac-8ccc-424ffb210134",
                "projectId": "675e9449-0f82-46f3-886d-640acc55559d",
                "fxType": "经济风险",
                "fxcd": "5",
                "description": "经济风险",
                "sort": 2
            },
            {
                "id": "aa0c818c-b164-4618-a905-776390173ad3",
                "projectId": "675e9449-0f82-46f3-886d-640acc55559d",
                "fxType": "安全风险",
                "fxcd": "4",
                "description": "安全风险",
                "sort": 1
            }
        ],
        "projectXmlxrs": [
            {
                "id": "350f6f65-5cde-4c54-877f-562ba369231a",
                "projectId": "675e9449-0f82-46f3-886d-640acc55559d",
                "name": "刘惠民",
                "phone": "13811111111",
                "type": 3,
                "sort": 3
            },
            {
                "id": "ee42eae2-18c8-4bcc-9531-b7590655255b",
                "projectId": "675e9449-0f82-46f3-886d-640acc55559d",
                "name": "成员单位",
                "phone": "13621212121",
                "type": 2,
                "sort": 2
            },
            {
                "id": "f7133b64-c069-4a28-b34f-4865622fbf18",
                "projectId": "675e9449-0f82-46f3-886d-640acc55559d",
                "name": "孙中壮",
                "phone": "18888888888",
                "type": 1,
                "sort": 1
            }
        ],
        "projectZqgcs": [
            {
                "id": "2f85234a-400c-4af5-8191-dc34d8576992",
                "projectId": "675e9449-0f82-46f3-886d-640acc55559d",
                "type": 3,
                "gdmc": "股东名称",
                "sort": 3
            },
            {
                "id": "6a599d5f-d9de-41bb-a8a1-17ad31a2fc0b",
                "projectId": "675e9449-0f82-46f3-886d-640acc55559d",
                "type": 1,
                "gdmc": "中方",
                "sort": 1
            },
            {
                "id": "ee8e0373-81ab-4c69-9412-2e2f3d103891",
                "projectId": "675e9449-0f82-46f3-886d-640acc55559d",
                "type": 2,
                "gdmc": "股东名称",
                "sort": 2
            }
        ]
    },
    {
        "projectDeclare": {
            "id": "2d60e422-c67e-4e1f-9d19-64d8ea6f8460",
            "xmbm": "71dce67e-d176-4d9b-834c-e2658004553b",
            "name": "我是测试哦",
            "type": "A,B",
            "investmentType": "并购",
            "constructionType": "施工承包",
            "projectDebriefing": "意向谋划",
            "projectDebriefingDetial": "123",
            "bjdsfzc": 1,
            "jfknqk": "",
            "kxwjqqk": "",
            "yyknqk": "",
            "yytcqk": "",
            "assess": 2,
            "assessContent": "123",
            "assessExplanation": "123",
            "standard": 0,
            "gbhdz": "D001",
            "dz": "B1",
            "province": "G001",
            "address": "2342",
            "realm": "A0001",
            "industry": "市政",
            "twoIndustry": "",
            "jsnrhmb": "123",
            "xmjhztz": 123.0,
            "cjqshte": 123.0,
            "xmdwzje": 123.0,
            "xmwczje": 123.0,
            "xmzqzje": 123.0,
            "xmgqzje": 123.0,
            "lwyyqk": "无偿援助,无息贷款,优惠援外贷款",
            "lwyyqkje": 123232.0,
            "lwyyqkwxje": 0.0,
            "lwyyqkywje": 0.0,
            "lwyyqkqx": 12312,
            "lwyyqkqxyw": 0,
            "lwyyqknhll": 123123.0,
            "zddbjkqk": 2,
            "yhckmfxd": 2,
            "qttjdw": 2,
            "qttjdwqc": "",
            "bsdwqc": "1231",
            "mlwt": "政局变动,资金困难,征地拆迁缓慢",
            "mlwtms": "123",
            "xybgzkl": "123",
            "sjkgsj": "2020-06-24",
            "sjwgsj": "2020-06-25",
            "pshjq": 2,
            "pshjqms": "",
            "gfltcgqd": 2,
            "gfltcgqdms": "",
            "dsfhz": 2,
            "dsfhzms": "",
            "xcld": 2,
            "xcldms": "",
            "discountPolicy": "",
            "countryDiscountPolicy": "1,2,3",
            "chinaDiscountPolicy": "1",
            "projectSignificance": "123123",
            "isShareInfo": 2,
            "chinaGqzb": "123",
            "projectGqzb": "123",
            "otherGqzb": "123",
            "chinaZqzb": "123",
            "projectZqzb": "123",
            "otherZqzb": "123",
            "gardenNum": "",
            "gardenAmount": "",
            "createJobNum": "",
            "taxAmount": "",
            "turnover": 0.0,
            "profit": 0.0,
            "createId": "BFA831DB0000000072B97A8A00000010",
            "createName": "张三",
            "createDate": "2020-06-13",
            "updateId": "BFA831DB0000000072B97A8A00000010",
            "updateName": "张三",
            "updateDate": "2020-06-15",
            "isSubmit": 1,
            "stage": 2,
            "isNewProject": 1
        },
        "projcectLnvestments": [
            {
                "id": "81bcb9e0-c28e-4c19-87ec-580190ab6148",
                "projectId": "2d60e422-c67e-4e1f-9d19-64d8ea6f8460",
                "tzdwmcName": "投资单位名称",
                "btzdwmcName": "123",
                "sort": 1
            }
        ],
        "projectConstructions": [
            {
                "id": "6c71bdd4-6e74-4343-9185-99d933b488ea",
                "projectId": "2d60e422-c67e-4e1f-9d19-64d8ea6f8460",
                "yzdwName": "123",
                "jsdwName": "123",
                "address": "123",
                "sort": 1
            }
        ],
        "projectGqgcs": [
            {
                "id": "0797a9b8-4109-4eb9-bcdd-24c7d48b2d73",
                "projectId": "2d60e422-c67e-4e1f-9d19-64d8ea6f8460",
                "type": 3,
                "gdmc": "12314",
                "sort": 3
            },
            {
                "id": "235759fd-bc14-45a5-9d38-ed4df9fb4129",
                "projectId": "2d60e422-c67e-4e1f-9d19-64d8ea6f8460",
                "type": 2,
                "gdmc": "124",
                "sort": 2
            },
            {
                "id": "deeed423-96b9-482d-95d9-7bc6786aba91",
                "projectId": "2d60e422-c67e-4e1f-9d19-64d8ea6f8460",
                "type": 1,
                "gdmc": "1212",
                "sort": 1
            }
        ],
        "projectXmfxes": [
            {
                "id": "02646100-7dfe-4dbd-a159-fb7ca5b27d59",
                "projectId": "2d60e422-c67e-4e1f-9d19-64d8ea6f8460",
                "fxType": "经济风险",
                "fxcd": "3",
                "description": "123",
                "sort": 3
            },
            {
                "id": "3db4394c-a7fb-4a22-925b-d5d0f2af220d",
                "projectId": "2d60e422-c67e-4e1f-9d19-64d8ea6f8460",
                "fxType": "安全风险",
                "fxcd": "4",
                "description": "123",
                "sort": 2
            },
            {
                "id": "ef3ca978-8cff-47e5-b629-5cff3b7495ee",
                "projectId": "2d60e422-c67e-4e1f-9d19-64d8ea6f8460",
                "fxType": "政治风险",
                "fxcd": "3",
                "description": "123",
                "sort": 1
            },
            {
                "id": "f1dcbc67-361b-4a31-ad73-a7e0e1e364e4",
                "projectId": "2d60e422-c67e-4e1f-9d19-64d8ea6f8460",
                "fxType": "法律风险",
                "fxcd": "3",
                "description": "123123",
                "sort": 4
            }
        ],
        "projectXmlxrs": [
            {
                "id": "baef4556-c1cd-46ec-bcca-24e2782d2209",
                "projectId": "2d60e422-c67e-4e1f-9d19-64d8ea6f8460",
                "name": "1231",
                "phone": "18500392662",
                "type": 1,
                "sort": 1
            },
            {
                "id": "eb7c1f57-6a07-4392-92e2-7dc1f061a0b9",
                "projectId": "2d60e422-c67e-4e1f-9d19-64d8ea6f8460",
                "name": "de",
                "phone": "18500392662",
                "type": 3,
                "sort": 3
            },
            {
                "id": "ebae5d9b-2004-4501-9abe-e765590f421e",
                "projectId": "2d60e422-c67e-4e1f-9d19-64d8ea6f8460",
                "name": "de",
                "phone": "18500392662",
                "type": 2,
                "sort": 2
            }
        ],
        "projectZqgcs": [
            {
                "id": "0cbd5611-ccde-40a3-82d4-559c5b27bd9b",
                "projectId": "2d60e422-c67e-4e1f-9d19-64d8ea6f8460",
                "type": 2,
                "gdmc": "123",
                "sort": 2
            },
            {
                "id": "cf42b6f9-3ee6-4ca9-8cd9-fae57cc608dc",
                "projectId": "2d60e422-c67e-4e1f-9d19-64d8ea6f8460",
                "type": 3,
                "gdmc": "123",
                "sort": 3
            },
            {
                "id": "d3e9d074-cd84-43ea-ad18-25815cc95c37",
                "projectId": "2d60e422-c67e-4e1f-9d19-64d8ea6f8460",
                "type": 1,
                "gdmc": "123",
                "sort": 1
            }
        ]
    },
    {
        "projectDeclare": {
            "id": "93d7f748-18d5-491f-a479-9c45ecf8e0bd",
            "xmbm": "9cdeef55-57ac-421f-850a-a0f3c3dc1147",
            "name": "测试后续项目报送",
            "type": "A",
            "investmentType": "并购",
            "constructionType": "",
            "projectDebriefing": "意向谋划",
            "projectDebriefingDetial": "123",
            "bjdsfzc": 1,
            "jfknqk": "",
            "kxwjqqk": "",
            "yyknqk": "",
            "yytcqk": "",
            "assess": 1,
            "assessContent": "234",
            "assessExplanation": "234",
            "standard": 0,
            "gbhdz": "C001",
            "dz": "A1",
            "province": "E001",
            "address": "234",
            "realm": "A0001",
            "industry": "桥梁",
            "twoIndustry": "",
            "jsnrhmb": "234",
            "xmjhztz": 123.0,
            "cjqshte": 123.0,
            "xmdwzje": 123.0,
            "xmwczje": 123.0,
            "xmzqzje": 13.0,
            "xmgqzje": 123.0,
            "lwyyqk": "无偿援助,无息贷款,优惠援外贷款",
            "lwyyqkje": 123.0,
            "lwyyqkwxje": 0.0,
            "lwyyqkywje": 0.0,
            "lwyyqkqx": 123,
            "lwyyqkqxyw": 0,
            "lwyyqknhll": 123.0,
            "zddbjkqk": 2,
            "yhckmfxd": 2,
            "qttjdw": 2,
            "qttjdwqc": "",
            "bsdwqc": "234",
            "mlwt": "政局变动,资金困难",
            "mlwtms": "123",
            "xybgzkl": "123",
            "sjkgsj": "2020-06-13",
            "sjwgsj": "2020-06-14",
            "pshjq": 2,
            "pshjqms": "",
            "gfltcgqd": 2,
            "gfltcgqdms": "",
            "dsfhz": 2,
            "dsfhzms": "",
            "xcld": 2,
            "xcldms": "",
            "discountPolicy": "",
            "countryDiscountPolicy": "1,2,3",
            "chinaDiscountPolicy": "3,2,1",
            "projectSignificance": "234",
            "isShareInfo": 2,
            "chinaGqzb": "123",
            "projectGqzb": "123",
            "otherGqzb": "123",
            "chinaZqzb": "123",
            "projectZqzb": "123",
            "otherZqzb": "123",
            "gardenNum": "",
            "gardenAmount": "",
            "createJobNum": "",
            "taxAmount": "",
            "turnover": 0.0,
            "profit": 0.0,
            "createId": "BFA831DB0000000072B97A8A00000010",
            "createName": "张三",
            "createDate": "2020-06-13",
            "updateId": "BFA831DB0000000072B97A8A00000010",
            "updateName": "张三",
            "updateDate": "2020-06-15",
            "isSubmit": 1,
            "stage": 3,
            "isNewProject": 0
        },
        "projcectLnvestments": [
            {
                "id": "212357ba-7568-43eb-b332-659d8c91f5e5",
                "projectId": "93d7f748-18d5-491f-a479-9c45ecf8e0bd",
                "tzdwmcName": "234",
                "btzdwmcName": "234",
                "sort": 1
            }
        ],
        "projectConstructions": [
            {
                "id": "429b7737-018c-4535-b64a-2027f5f1d071",
                "projectId": "93d7f748-18d5-491f-a479-9c45ecf8e0bd",
                "yzdwName": "",
                "jsdwName": "",
                "address": "",
                "sort": 1
            }
        ],
        "projectGqgcs": [
            {
                "id": "7836ad70-2e91-467f-bf53-ad456f682957",
                "projectId": "93d7f748-18d5-491f-a479-9c45ecf8e0bd",
                "type": 3,
                "gdmc": "123",
                "sort": 3
            },
            {
                "id": "a3c30104-6255-4efb-8ebb-f5b3a9095daa",
                "projectId": "93d7f748-18d5-491f-a479-9c45ecf8e0bd",
                "type": 1,
                "gdmc": "123",
                "sort": 1
            },
            {
                "id": "cf431e5f-50bb-4d17-bf80-6fb28208657c",
                "projectId": "93d7f748-18d5-491f-a479-9c45ecf8e0bd",
                "type": 2,
                "gdmc": "123",
                "sort": 2
            }
        ],
        "projectXmfxes": [
            {
                "id": "5af2db01-a46e-4942-9f52-a08e0c611a6e",
                "projectId": "93d7f748-18d5-491f-a479-9c45ecf8e0bd",
                "fxType": "政治风险",
                "fxcd": "5",
                "description": "123",
                "sort": 1
            },
            {
                "id": "b87e5ef3-c31d-45ef-a86f-712548d82ba8",
                "projectId": "93d7f748-18d5-491f-a479-9c45ecf8e0bd",
                "fxType": "其他风险",
                "fxcd": "5",
                "description": "123",
                "sort": 2
            }
        ],
        "projectXmlxrs": [
            {
                "id": "324b24b9-0aee-43eb-9077-43fbccfe9649",
                "projectId": "93d7f748-18d5-491f-a479-9c45ecf8e0bd",
                "name": "234",
                "phone": "18500392662",
                "type": 1,
                "sort": 2
            },
            {
                "id": "714bf727-c7f1-4877-ab97-27b4d4a5c052",
                "projectId": "93d7f748-18d5-491f-a479-9c45ecf8e0bd",
                "name": "阿松大",
                "phone": "18500392662",
                "type": 3,
                "sort": 6
            },
            {
                "id": "a107ca6d-c208-4ed5-980a-a84285a61169",
                "projectId": "93d7f748-18d5-491f-a479-9c45ecf8e0bd",
                "name": "阿松大",
                "phone": "18500392662",
                "type": 2,
                "sort": 3
            },
            {
                "id": "ac767772-0893-424e-a035-d3707360c438",
                "projectId": "93d7f748-18d5-491f-a479-9c45ecf8e0bd",
                "name": "阿松大",
                "phone": "18500392662",
                "type": 3,
                "sort": 5
            },
            {
                "id": "e126476d-a291-4c54-8c86-4a72df32aebe",
                "projectId": "93d7f748-18d5-491f-a479-9c45ecf8e0bd",
                "name": "阿松大",
                "phone": "18500392662",
                "type": 2,
                "sort": 4
            },
            {
                "id": "e723126c-113b-49d9-875d-f83fa82fe134",
                "projectId": "93d7f748-18d5-491f-a479-9c45ecf8e0bd",
                "name": "234",
                "phone": "18500392662",
                "type": 1,
                "sort": 1
            }
        ],
        "projectZqgcs": [
            {
                "id": "1fa266c0-2144-4349-8b26-50161a7d2da1",
                "projectId": "93d7f748-18d5-491f-a479-9c45ecf8e0bd",
                "type": 2,
                "gdmc": "123",
                "sort": 2
            },
            {
                "id": "34de220f-a86a-4ec7-be35-941ba8985fd5",
                "projectId": "93d7f748-18d5-491f-a479-9c45ecf8e0bd",
                "type": 3,
                "gdmc": "123",
                "sort": 3
            },
            {
                "id": "410ff78b-8587-4c73-a94f-d78b94e11233",
                "projectId": "93d7f748-18d5-491f-a479-9c45ecf8e0bd",
                "type": 1,
                "gdmc": "123",
                "sort": 1
            }
        ]
    },
    {
        "projectDeclare": {
            "id": "6cd57474-c5d0-49f3-beac-866f8a9f98f8",
            "xmbm": "45e53ea5-7cee-42d4-8bd0-4aa9c816c394",
            "name": "新项目报送",
            "type": "A,B",
            "investmentType": "绿地投资",
            "constructionType": "EPC",
            "projectDebriefing": "意向谋划",
            "projectDebriefingDetial": "123",
            "bjdsfzc": 1,
            "jfknqk": "",
            "kxwjqqk": "",
            "yyknqk": "",
            "yytcqk": "",
            "assess": 1,
            "assessContent": "最美好的",
            "assessExplanation": "严格说明",
            "standard": 0,
            "gbhdz": "C001",
            "dz": "A1",
            "province": "E001",
            "address": "济南",
            "realm": "A0001",
            "industry": "机场",
            "twoIndustry": "",
            "jsnrhmb": "成为世界第一",
            "xmjhztz": 122.0,
            "cjqshte": 12.0,
            "xmdwzje": 123.0,
            "xmwczje": 123.0,
            "xmzqzje": 123.0,
            "xmgqzje": 123.0,
            "lwyyqk": "无偿援助,无息贷款",
            "lwyyqkje": 123.0,
            "lwyyqkwxje": 0.0,
            "lwyyqkywje": 0.0,
            "lwyyqkqx": 123,
            "lwyyqkqxyw": 0,
            "zddbjkqk": 2,
            "yhckmfxd": 2,
            "qttjdw": 2,
            "qttjdwqc": "",
            "bsdwqc": "北京百度",
            "mlwt": "政局变动,资金困难",
            "mlwtms": "1231",
            "xybgzkl": "123123",
            "sjkgsj": "2020-06-13",
            "sjwgsj": "2020-06-14",
            "pshjq": 2,
            "pshjqms": "",
            "gfltcgqd": 2,
            "gfltcgqdms": "",
            "dsfhz": 2,
            "dsfhzms": "",
            "xcld": 2,
            "xcldms": "",
            "discountPolicy": "",
            "countryDiscountPolicy": "1,2",
            "chinaDiscountPolicy": "2,1",
            "projectSignificance": "项目意义",
            "isShareInfo": 2,
            "chinaGqzb": "123",
            "projectGqzb": "123",
            "otherGqzb": "123",
            "chinaZqzb": "123",
            "projectZqzb": "2",
            "otherZqzb": "123",
            "gardenNum": "",
            "gardenAmount": "",
            "createJobNum": "",
            "taxAmount": "",
            "turnover": 0.0,
            "profit": 0.0,
            "createId": "BFA831DB0000000072B97A8A00000010",
            "createName": "张三",
            "createDate": "2020-06-13",
            "updateId": "BFA831DB0000000072B97A8A00000010",
            "updateName": "张三",
            "updateDate": "2020-06-13",
            "isSubmit": 1,
            "stage": 3,
            "isNewProject": 1
        },
        "projcectLnvestments": [
            {
                "id": "05fd5214-c2da-439f-b362-43e07d645d76",
                "projectId": "6cd57474-c5d0-49f3-beac-866f8a9f98f8",
                "tzdwmcName": "投资单位2",
                "btzdwmcName": "被投资单位2",
                "sort": 2
            },
            {
                "id": "57fce1b6-6152-4c10-ab3c-cd2db5874cca",
                "projectId": "6cd57474-c5d0-49f3-beac-866f8a9f98f8",
                "tzdwmcName": "投资单位1",
                "btzdwmcName": "被投资单位1",
                "sort": 1
            }
        ],
        "projectConstructions": [
            {
                "id": "8e003388-81e9-4677-ae88-af2dfd6e7f82",
                "projectId": "6cd57474-c5d0-49f3-beac-866f8a9f98f8",
                "yzdwName": "业主1",
                "jsdwName": "1",
                "address": "北京",
                "sort": 1
            }
        ],
        "projectGqgcs": [
            {
                "id": "14620211-a37b-499d-874f-3dc028125c83",
                "projectId": "6cd57474-c5d0-49f3-beac-866f8a9f98f8",
                "type": 3,
                "gdmc": "123",
                "sort": 3
            },
            {
                "id": "4bef8ff0-f567-48e3-96d5-f56dda791f6e",
                "projectId": "6cd57474-c5d0-49f3-beac-866f8a9f98f8",
                "type": 2,
                "gdmc": "123",
                "sort": 2
            },
            {
                "id": "50f15a2d-d660-4a33-80ac-ef84d56da30f",
                "projectId": "6cd57474-c5d0-49f3-beac-866f8a9f98f8",
                "type": 1,
                "gdmc": "123",
                "sort": 1
            }
        ],
        "projectXmfxes": [
            {
                "id": "1e0e32f0-003d-4f4f-89a6-e796fc6aa4df",
                "projectId": "6cd57474-c5d0-49f3-beac-866f8a9f98f8",
                "fxType": "政治风险",
                "fxcd": "1",
                "description": "123",
                "sort": 1
            },
            {
                "id": "b08c142c-4a63-42f3-881a-40af44cce948",
                "projectId": "6cd57474-c5d0-49f3-beac-866f8a9f98f8",
                "fxType": "安全风险",
                "fxcd": "7",
                "description": "123123",
                "sort": 2
            }
        ],
        "projectXmlxrs": [
            {
                "id": "1e59df44-328b-4d47-9434-af1ba1ce1d4a",
                "projectId": "6cd57474-c5d0-49f3-beac-866f8a9f98f8",
                "name": "张三2",
                "phone": "18500392662",
                "type": 2,
                "sort": 2
            },
            {
                "id": "7693d42f-97a6-4a14-b9cf-7680d839f29c",
                "projectId": "6cd57474-c5d0-49f3-beac-866f8a9f98f8",
                "name": "张三3",
                "phone": "18500392662",
                "type": 3,
                "sort": 3
            },
            {
                "id": "b6eb431f-0f13-4b48-a229-ef6af56290d5",
                "projectId": "6cd57474-c5d0-49f3-beac-866f8a9f98f8",
                "name": "张三1",
                "phone": "18500392662",
                "type": 1,
                "sort": 1
            }
        ],
        "projectZqgcs": [
            {
                "id": "007218d4-2db5-46ff-bbe7-0d28ae3f2df8",
                "projectId": "6cd57474-c5d0-49f3-beac-866f8a9f98f8",
                "type": 1,
                "gdmc": "123",
                "sort": 1
            },
            {
                "id": "13cf44c4-dfe5-4702-9ea8-4f7c7c92b178",
                "projectId": "6cd57474-c5d0-49f3-beac-866f8a9f98f8",
                "type": 2,
                "gdmc": "23",
                "sort": 2
            },
            {
                "id": "22cafff2-d6db-4112-a10d-60ce97dba771",
                "projectId": "6cd57474-c5d0-49f3-beac-866f8a9f98f8",
                "type": 3,
                "gdmc": "11",
                "sort": 3
            }
        ]
    }
]
cookies = {}
with open("cookies.txt", 'r') as file:
    for line in file.read().split(';'):
        name, value = line.strip().split('=', 1)
        cookies[name] = value

requests = requests.post('http://192.168.50.116:8080/ydylnw/transport/saveData', data=json.dumps(data),
                         headers=headers,
                         cookies=cookies);

print(requests.text);
