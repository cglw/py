# -*- coding: utf-8 -*-
# @Time : 2018/9/20 下午4:07
# @Author : chengang
# @File : views_base.py
# @Function:
from django.views.generic.base import View
from goods.models import Goods

class GoodsListView(View):
    def get(self,request):
        json_list=[]
        goods=Goods.objects.all()[:10]
        Goods.objects.filter(Goods.)

        from django.core import serializers
        import json

        json_data=serializers.serialize("json",goods)
        json_data=json.loads(json_data)
        from  django.http import HttpResponse,JsonResponse
        return JsonResponse(json_data,safe=False)
