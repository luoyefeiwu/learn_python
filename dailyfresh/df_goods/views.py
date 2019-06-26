from django.shortcuts import render
from .models import *
from df_cart.models import CartInfo


def index(request):
    # 查询各个分类的最新4条，最热4条数据
    typelist = TypeInfo.objects.all()
    print(TypeInfo)
    # _set 连表操作
    type0 = typelist[0].goodsinfo_set.order_by('-id')[0:4]  # 按照上传顺序
    type01 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]  # 按照点击量
    type1 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    type11 = typelist[1].goodsinfo_set.order_by('-gclick')[0:4]
    type2 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
    type21 = typelist[2].goodsinfo_set.order_by('-gclick')[0:4]
    type3 = typelist[3].goodsinfo_set.order_by('-id')[0:4]
    type31 = typelist[3].goodsinfo_set.order_by('-gclick')[0:4]
    type4 = typelist[4].goodsinfo_set.order_by('-id')[0:4]
    type41 = typelist[4].goodsinfo_set.order_by('-gclick')[0:4]
    type5 = typelist[5].goodsinfo_set.order_by('-id')[0:4]
    type51 = typelist[5].goodsinfo_set.order_by('-gclick')[0:4]
    cart_num = 0
    # 判断是否存在登录状态
    # if request.session.has_key('user_id'):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        cart_num = CartInfo.objects.filter(user_id=int(user_id)).count()
    context = {
        'title': '首页',
        'cart_num': cart_num,
        'guest_cart': 1,
        'type0': type0, 'type01': type01,
        'type1': type1, 'type11': type11,
        'type2': type2, 'type21': type21,
        'type3': type3, 'type31': type31,
        'type4': type4, 'type41': type41,
        'type5': type5, 'type51': type51,
    }

    return render(request, 'df_goods/index.html', context)


def ordinary_search(request):
    context = {
        'title': '搜索列表',
        'search_status': 'search_status',
        'guest_cart': 'guest_cart',
        'cart_num': 'cart_num',
        'page': 'page',
        'paginator': 'paginator',
    }
    return render(request, 'df_goods/ordinary_search.html')
