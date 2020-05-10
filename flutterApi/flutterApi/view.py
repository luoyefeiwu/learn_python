# coding=utf-8
from django.http import HttpResponse, JsonResponse
import json


def homePageContent(request):
    print(request.get_full_path())
    data = {
        "data": {
            "slides": [
                {
                    "image": "http://192.168.3.8:8000/images/1.jpg"
                },
                {
                    "image": "http://192.168.3.8:8000/images/2.jpg"
                },
                {
                    "image": "http://192.168.3.8:8000/images/3.jpg"
                },
                {
                    "image": "http://192.168.3.8:8000/images/4.jpg"
                }
            ],
            "category": [
                {
                    "image": "http://192.168.3.8:8000/images/shop1.png",
                    "mallCategoryName": "超市"
                },
                {
                    "image": "http://192.168.3.8:8000/images/shop2.png",
                    "mallCategoryName": "数码电器"
                },
                {
                    "image": "http://192.168.3.8:8000/images/shop3.png",
                    "mallCategoryName": "服饰"
                },
                {
                    "image": "http://192.168.3.8:8000/images/shop4.png",
                    "mallCategoryName": "生鲜"
                },
                {
                    "image": "http://192.168.3.8:8000/images/shop5.png",
                    "mallCategoryName": "到家"
                },
                {
                    "image": "http://192.168.3.8:8000/images/shop6.png",
                    "mallCategoryName": "充值缴费"
                },
                {
                    "image": "http://192.168.3.8:8000/images/shop7.png",
                    "mallCategoryName": "拼团"
                },
                {
                    "image": "http://192.168.3.8:8000/images/shop8.png",
                    "mallCategoryName": "领券"
                },
                {
                    "image": "http://192.168.3.8:8000/images/shop9.png",
                    "mallCategoryName": "赚钱"
                },
                {
                    "image": "http://192.168.3.8:8000/images/shop10.png",
                    "mallCategoryName": "会员"
                }
            ],
            "advertesPicture": {
                "PICURE_ADDRESS": "http://192.168.3.8:8000/images/1.jpg"
            },
            "shopInfo": {
                "leaderImage": "http://192.168.3.8:8000/images/2.jpg",
                "leaderPhone": "110"
            },
            "recommend": [
                {
                    "image": "http://192.168.3.8:8000/images/hot1.jpg",
                    "malPrice": 100,
                    "price": 200
                },
                {
                    "image": "http://192.168.3.8:8000/images/hot2.jpg",
                    "malPrice": 200,
                    "price": 300
                },
                {
                    "image": "http://192.168.3.8:8000/images/hot3.jpg",
                    "malPrice": 300,
                    "price": 400
                },

            ],
            "floor1Pic": {
                "PICURE_ADDRESS": "http://192.168.3.8:8000/images/floor1.jpg"
            },
            "floor1": [
                {"image": "http://192.168.3.8:8000/images/floor2.jpg"},
                {"image": "http://192.168.3.8:8000/images/floor3.jpg"},
                {"image": "http://192.168.3.8:8000/images/floor4.jpg"},
                {"image": "http://192.168.3.8:8000/images/floor5.jpg"},
                {"image": "http://192.168.3.8:8000/images/floor6.jpg"},

            ],
        }
    }
    return JsonResponse(data)


def homePageBelowten(request):
    data = {"data": [
        {"image": "http://192.168.3.8:8000/images/floor2.jpg", "name": "iphone7", "mallPrice": 100, "price": 90},
        {"image": "http://192.168.3.8:8000/images/floor2.jpg", "name": "iphone8", "mallPrice": 100, "price": 90},
        {"image": "http://192.168.3.8:8000/images/floor2.jpg", "name": "iphone9", "mallPrice": 100, "price": 90},
        {"image": "http://192.168.3.8:8000/images/floor2.jpg", "name": "iphone10", "mallPrice": 100, "price": 90},
    ]}
    return JsonResponse(data)
