import ujson
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_redis import get_redis_connection
from rest_framework.decorators import api_view, action, authentication_classes
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from web.models import *
# Create your views here.
from common.captcha import *
from web.serializers import DistrictSimpleSerializer, DistrictDetailSerializer


@cache_page(timeout=365 * 86400)
@api_view(('GET', ))
def get_provinces(request):
    """获取省级行政单位"""
    queryset = District.objects.filter(parent__isnull=True)\
        .only('name')
    serializer = DistrictSimpleSerializer(queryset, many=True)
    return Response({
        'code': 10000,
        'message': '获取省级行政区域成功',
        'results': serializer.data
    })


@api_view(('GET', ))
def get_district(request, distid):
    """获取地区详情"""
    redis_cli = get_redis_connection()
    data = redis_cli.get(f'zufang:district:{distid}')
    if data:
        data = ujson.loads(data)
    else:
        district = District.objects.filter(distid=distid)\
            .defer('parent').first()
        data = DistrictDetailSerializer(district).data
        redis_cli.set(f'zufang:district:{distid}', ujson.dumps(data), ex=900)
    return Response(data)


@method_decorator(decorator=cache_page(timeout=86400), name='get')
class HotCityView(ListAPIView):
    """热门城市视图
    get:
        获取热门城市
    """
    queryset = District.objects.filter(ishot=True).only('name')
    serializer_class = DistrictSimpleSerializer
    pagination_class = None


def get_hot_distinct(request):
    if request.method == 'GET':
        hot_distinct = District.objects.filter(ishot=1)
        hot_list = []
        for distinct in hot_distinct:
            hot_list.append(distinct.name)
        return HttpResponse(hot_list)


def index(request):
    if request.method == 'GET':
        recruit = Recruiter.objects.all()
    return recruit


def main():
    result = index()
    print(result)


if __name__ == '__main__':
    main()

