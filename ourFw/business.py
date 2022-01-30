from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from .models import CWxSandtableWeiwanggeBusiness
import json
# from django.core import serializers  # 用于返回jsonarray
from django.db.models import Sum


def businessAllMCountCity(request):
    if request.method == 'POST':  # if后面没有大括号
        postBody = request.body
        json_result = json.loads(postBody)
        currentTimeAttr = json_result['currentTime']
        fromAttr = json_result['from']
        toAttr = json_result['to']
        # values 和annotate连用可以group by
        result = CWxSandtableWeiwanggeBusiness.objects.filter(second_label='业务总量').filter(
            month_id=currentTimeAttr).values('month_id',
                                             'city_name').annotate(
            dataSum=Sum('user_all_call_duration_m')).filter(
            dataSum__gte=fromAttr).filter(
            dataSum__lt=toAttr).count()  # filter函数的使用
        # print(json_result)
        # print(Population.objects.order_by('-id'))  # 默认升序，-降序
        dic = {}
        dic['count'] = result
        dic = json.dumps(dic)
        return HttpResponse(dic)
    else:
        return HttpResponse("get")


def businessAllMDetailCount(request):
    if request.method == 'POST':  # if后面没有大括号
        postBody = request.body
        json_result = json.loads(postBody)
        currentTimeAttr = json_result['currentTime']
        fromAttr = json_result['from']
        toAttr = json_result['to']
        # provinceAttr = request.POST.get('provinceName')
        # cityAttr = request.POST.get('cityName')
        # print(provinceAttr, cityAttr)
        result = 0
        # 如果不发provinceName参数，使用json_result.get('provinceName')不报错，使用json_result['provinceName']会报错
        if json_result.get('provinceName'):
            try:
                provinceNameAttr = json_result['provinceName']
                result = CWxSandtableWeiwanggeBusiness.objects.filter(month_id=currentTimeAttr).filter(
                    province_name=provinceNameAttr).filter(
                    user_all_call_duration_m_density__gte=fromAttr).filter(
                    user_all_call_duration_m_density__lt=toAttr).count()  # filter函数的使用
            except Exception as e:
                print('provinceName not exists')
        elif json_result.get('cityName'):
            try:
                cityNameAttr = json_result['cityName']
                result = CWxSandtableWeiwanggeBusiness.objects.filter(month_id=currentTimeAttr).filter(
                    city_name=cityNameAttr).filter(
                    user_all_call_duration_m_density__gte=fromAttr).filter(
                    user_all_call_duration_m_density__lt=toAttr).count()  # filter函数的使用
            except Exception as e:
                print('cityName not exists')

        # print(provinceNameAttr, cityNameAttr)

        # print(json_result)
        # print(Population.objects.order_by('-id'))  # 默认升序，-降序
        dic = {}
        dic['count'] = result
        dic = json.dumps(dic)
        return HttpResponse(dic)
    else:
        return HttpResponse("get")
