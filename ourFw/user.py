from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from .models import CWxSandtableWeiwanggeUser
import json
# from django.core import serializers  # 用于返回jsonarray
from django.db.models import Sum


def allUserCountCity(request):
    if request.method == 'POST':  # if后面没有大括号
        postBody = request.body
        json_result = json.loads(postBody)
        currentTimeAttr = json_result['currentTime']
        fromAttr = json_result['from']
        toAttr = json_result['to']
        print(currentTimeAttr)
        # values 和annotate连用可以group by
        result = CWxSandtableWeiwanggeUser.objects.filter(month_id=currentTimeAttr).values('month_id',
                                                                                           'city_name').annotate(
            citySum=Sum('user_all_residentlocation')).filter(
            citySum__gte=fromAttr).filter(
            citySum__lt=toAttr).count()  # filter函数的使用
        # print(json_result)
        # print(Population.objects.order_by('-id'))  # 默认升序，-降序
        dic = {}
        dic['count'] = result
        dic = json.dumps(dic)
        return HttpResponse(dic)
    else:
        return HttpResponse("get")


def allUserDetailCount(request):
    if request.method == 'POST':  # if后面没有大括号
        postBody = request.body
        json_result = json.loads(postBody)
        currentTimeAttr = json_result['currentTime']
        print(currentTimeAttr)
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
                result = CWxSandtableWeiwanggeUser.objects.filter(month_id=currentTimeAttr).filter(
                    province_name=provinceNameAttr).filter(
                    user_all_residentlocation_density__gte=fromAttr).filter(
                    user_all_residentlocation_density__lt=toAttr).count()  # filter函数的使用
            except Exception as e:
                print('provinceName not exists')
        elif json_result.get('cityName'):
            try:
                cityNameAttr = json_result['cityName']
                result = CWxSandtableWeiwanggeUser.objects.filter(month_id=currentTimeAttr).filter(
                    city_name=cityNameAttr).filter(
                    user_all_residentlocation_density__gte=fromAttr).filter(
                    user_all_residentlocation_density__lt=toAttr).count()  # filter函数的使用
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


def g4UserCountCity(request):
    if request.method == 'POST':  # if后面没有大括号
        postBody = request.body
        json_result = json.loads(postBody)
        currentTimeAttr = json_result['currentTime']
        fromAttr = json_result['from']
        toAttr = json_result['to']
        print(currentTimeAttr)
        # values 和annotate连用可以group by
        result = CWxSandtableWeiwanggeUser.objects.filter(month_id=currentTimeAttr).values('month_id',
                                                                                           'city_name').annotate(
            citySum=Sum('user_g4_residentlocation')).filter(
            citySum__gte=fromAttr).filter(
            citySum__lt=toAttr).count()  # filter函数的使用
        # print(json_result)
        # print(Population.objects.order_by('-id'))  # 默认升序，-降序
        dic = {}
        dic['count'] = result
        dic = json.dumps(dic)
        return HttpResponse(dic)
    else:
        return HttpResponse("get")


def g4UserDetailCount(request):
    if request.method == 'POST':  # if后面没有大括号
        postBody = request.body
        json_result = json.loads(postBody)
        currentTimeAttr = json_result['currentTime']
        print(currentTimeAttr)
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
                result = CWxSandtableWeiwanggeUser.objects.filter(month_id=currentTimeAttr).filter(
                    province_name=provinceNameAttr).filter(
                    user_g4_residentlocation_density__gte=fromAttr).filter(
                    user_g4_residentlocation_density__lt=toAttr).count()  # filter函数的使用
            except Exception as e:
                print('provinceName not exists')
        elif json_result.get('cityName'):
            try:
                cityNameAttr = json_result['cityName']
                result = CWxSandtableWeiwanggeUser.objects.filter(month_id=currentTimeAttr).filter(
                    city_name=cityNameAttr).filter(
                    user_g4_residentlocation_density__gte=fromAttr).filter(
                    user_g4_residentlocation_density__lt=toAttr).count()  # filter函数的使用
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


def g5UserCountCity(request):
    if request.method == 'POST':  # if后面没有大括号
        postBody = request.body
        json_result = json.loads(postBody)
        currentTimeAttr = json_result['currentTime']
        fromAttr = json_result['from']
        toAttr = json_result['to']
        print(currentTimeAttr)
        # values 和annotate连用可以group by
        result = CWxSandtableWeiwanggeUser.objects.filter(month_id=currentTimeAttr).values('month_id',
                                                                                           'city_name').annotate(
            citySum=Sum('user_g5_residentlocation')).filter(
            citySum__gte=fromAttr).filter(
            citySum__lt=toAttr).count()  # filter函数的使用
        # print(json_result)
        # print(Population.objects.order_by('-id'))  # 默认升序，-降序
        dic = {}
        dic['count'] = result
        dic = json.dumps(dic)
        return HttpResponse(dic)
    else:
        return HttpResponse("get")


def g5UserDetailCount(request):
    if request.method == 'POST':  # if后面没有大括号
        postBody = request.body
        json_result = json.loads(postBody)
        currentTimeAttr = json_result['currentTime']
        print(currentTimeAttr)
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
                result = CWxSandtableWeiwanggeUser.objects.filter(month_id=currentTimeAttr).filter(
                    province_name=provinceNameAttr).filter(
                    user_g5_residentlocation_density__gte=fromAttr).filter(
                    user_g5_residentlocation_density__lt=toAttr).count()  # filter函数的使用
            except Exception as e:
                print('provinceName not exists')
        elif json_result.get('cityName'):
            try:
                cityNameAttr = json_result['cityName']
                result = CWxSandtableWeiwanggeUser.objects.filter(month_id=currentTimeAttr).filter(
                    city_name=cityNameAttr).filter(
                    user_g5_residentlocation_density__gte=fromAttr).filter(
                    user_g5_residentlocation_density__lt=toAttr).count()  # filter函数的使用
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


def potentialG5UserCountCity(request):
    if request.method == 'POST':  # if后面没有大括号
        postBody = request.body
        json_result = json.loads(postBody)
        currentTimeAttr = json_result['currentTime']
        fromAttr = json_result['from']
        toAttr = json_result['to']
        print(currentTimeAttr)
        # values 和annotate连用可以group by
        result = CWxSandtableWeiwanggeUser.objects.filter(month_id=currentTimeAttr).values('month_id',
                                                                                           'city_name').annotate(
            citySum=Sum('user_g5_potential_residentlocation')).filter(
            citySum__gte=fromAttr).filter(
            citySum__lt=toAttr).count()  # filter函数的使用
        # print(json_result)
        # print(Population.objects.order_by('-id'))  # 默认升序，-降序
        dic = {}
        dic['count'] = result
        dic = json.dumps(dic)
        return HttpResponse(dic)
    else:
        return HttpResponse("get")


def potentialG5UserDetailCount(request):
    if request.method == 'POST':  # if后面没有大括号
        postBody = request.body
        json_result = json.loads(postBody)
        currentTimeAttr = json_result['currentTime']
        print(currentTimeAttr)
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
                result = CWxSandtableWeiwanggeUser.objects.filter(month_id=currentTimeAttr).filter(
                    province_name=provinceNameAttr).filter(
                    user_g5_potential_residentlocation_density__gte=fromAttr).filter(
                    user_g5_potential_residentlocation_density__lt=toAttr).count()  # filter函数的使用
            except Exception as e:
                print('provinceName not exists')
        elif json_result.get('cityName'):
            try:
                cityNameAttr = json_result['cityName']
                result = CWxSandtableWeiwanggeUser.objects.filter(month_id=currentTimeAttr).filter(
                    city_name=cityNameAttr).filter(
                    user_g5_potential_residentlocation_density__gte=fromAttr).filter(
                    user_g5_potential_residentlocation_density__lt=toAttr).count()  # filter函数的使用
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


def arpuhighUserCountCity(request):
    if request.method == 'POST':  # if后面没有大括号
        postBody = request.body
        json_result = json.loads(postBody)
        currentTimeAttr = json_result['currentTime']
        fromAttr = json_result['from']
        toAttr = json_result['to']
        print(currentTimeAttr)
        # values 和annotate连用可以group by
        result = CWxSandtableWeiwanggeUser.objects.filter(month_id=currentTimeAttr).values('month_id',
                                                                                           'city_name').annotate(
            citySum=Sum('user_arpuhigh_residentlocation')).filter(
            citySum__gte=fromAttr).filter(
            citySum__lt=toAttr).count()  # filter函数的使用
        # print(json_result)
        # print(Population.objects.order_by('-id'))  # 默认升序，-降序
        dic = {}
        dic['count'] = result
        dic = json.dumps(dic)
        return HttpResponse(dic)
    else:
        return HttpResponse("get")


def arpuhighUserDetailCount(request):
    if request.method == 'POST':  # if后面没有大括号
        postBody = request.body
        json_result = json.loads(postBody)
        currentTimeAttr = json_result['currentTime']
        print(currentTimeAttr)
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
                result = CWxSandtableWeiwanggeUser.objects.filter(month_id=currentTimeAttr).filter(
                    province_name=provinceNameAttr).filter(
                    user_arpuhigh_residentlocation_density__gte=fromAttr).filter(
                    user_arpuhigh_residentlocation_density__lt=toAttr).count()  # filter函数的使用
            except Exception as e:
                print('provinceName not exists')
        elif json_result.get('cityName'):
            try:
                cityNameAttr = json_result['cityName']
                result = CWxSandtableWeiwanggeUser.objects.filter(month_id=currentTimeAttr).filter(
                    city_name=cityNameAttr).filter(
                    user_arpuhigh_residentlocation_density__gte=fromAttr).filter(
                    user_arpuhigh_residentlocation_density__lt=toAttr).count()  # filter函数的使用
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


def userTerminalPriceHighCountCity(request):
    if request.method == 'POST':  # if后面没有大括号
        postBody = request.body
        json_result = json.loads(postBody)
        currentTimeAttr = json_result['currentTime']
        fromAttr = json_result['from']
        toAttr = json_result['to']
        print(currentTimeAttr)
        # values 和annotate连用可以group by
        result = CWxSandtableWeiwanggeUser.objects.filter(month_id=currentTimeAttr).values('month_id',
                                                                                           'city_name').annotate(
            citySum=Sum('user_terminal_price_high_residentlocation')).filter(
            citySum__gte=fromAttr).filter(
            citySum__lt=toAttr).count()  # filter函数的使用
        # print(json_result)
        # print(Population.objects.order_by('-id'))  # 默认升序，-降序
        dic = {}
        dic['count'] = result
        dic = json.dumps(dic)
        return HttpResponse(dic)
    else:
        return HttpResponse("get")


def userTerminalPriceHighDetailCount(request):
    if request.method == 'POST':  # if后面没有大括号
        postBody = request.body
        json_result = json.loads(postBody)
        currentTimeAttr = json_result['currentTime']
        print(currentTimeAttr)
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
                result = CWxSandtableWeiwanggeUser.objects.filter(month_id=currentTimeAttr).filter(
                    province_name=provinceNameAttr).filter(
                    user_terminal_price_high_residentlocation_density__gte=fromAttr).filter(
                    user_terminal_price_high_residentlocation_density__lt=toAttr).count()  # filter函数的使用
            except Exception as e:
                print('provinceName not exists')
        elif json_result.get('cityName'):
            try:
                cityNameAttr = json_result['cityName']
                result = CWxSandtableWeiwanggeUser.objects.filter(month_id=currentTimeAttr).filter(
                    city_name=cityNameAttr).filter(
                    user_terminal_price_high_residentlocation_density__gte=fromAttr).filter(
                    user_terminal_price_high_residentlocation_density__lt=toAttr).count()  # filter函数的使用
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


def userDouhighCountCity(request):
    if request.method == 'POST':  # if后面没有大括号
        postBody = request.body
        json_result = json.loads(postBody)
        currentTimeAttr = json_result['currentTime']
        fromAttr = json_result['from']
        toAttr = json_result['to']
        print(currentTimeAttr)
        # values 和annotate连用可以group by
        result = CWxSandtableWeiwanggeUser.objects.filter(month_id=currentTimeAttr).values('month_id',
                                                                                           'city_name').annotate(
            citySum=Sum('user_douhigh_residentlocation')).filter(
            citySum__gte=fromAttr).filter(
            citySum__lt=toAttr).count()  # filter函数的使用
        # print(json_result)
        # print(Population.objects.order_by('-id'))  # 默认升序，-降序
        dic = {}
        dic['count'] = result
        dic = json.dumps(dic)
        return HttpResponse(dic)
    else:
        return HttpResponse("get")


def userDouhighDetailCount(request):
    if request.method == 'POST':  # if后面没有大括号
        postBody = request.body
        json_result = json.loads(postBody)
        currentTimeAttr = json_result['currentTime']
        print(currentTimeAttr)
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
                result = CWxSandtableWeiwanggeUser.objects.filter(month_id=currentTimeAttr).filter(
                    province_name=provinceNameAttr).filter(
                    user_douhigh_residentlocation_density__gte=fromAttr).filter(
                    user_douhigh_residentlocation_density__lt=toAttr).count()  # filter函数的使用
            except Exception as e:
                print('provinceName not exists')
        elif json_result.get('cityName'):
            try:
                cityNameAttr = json_result['cityName']
                result = CWxSandtableWeiwanggeUser.objects.filter(month_id=currentTimeAttr).filter(
                    city_name=cityNameAttr).filter(
                    user_douhigh_residentlocation_density__gte=fromAttr).filter(
                    user_douhigh_residentlocation_density__lt=toAttr).count()  # filter函数的使用
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
