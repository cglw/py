# -*- coding: utf-8 -*-
# @Time : 2018/9/27 下午4:41
# @Author : chengang
# @File : fiters.py
# @Function:

import django_filters
from django.db.models import Q

from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    pricemin = django_filters.NumberFilter(field_name='shop_price', help_text="最低价格", lookup_expr='gte')
    pricemax = django_filters.NumberFilter(field_name='shop_price', lookup_expr='lte')
    top_category = django_filters.NumberFilter(method='top_category_filter')
    name = django_filters.CharFilter(field_name="name", lookup_expr='icontains')

    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
            category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax', 'name', 'is_hot', ]
