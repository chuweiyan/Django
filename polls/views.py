from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from .models import Question
from .models import Population
from .models import PollsVideo
import json
from django.core import serializers  # 用于返回jsonarray


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def population(request):
    print(request.method)
    if request.method == 'POST':  # if后面没有大括号
        postBody = request.body
        json_result = json.loads(postBody)
        fromAttr = json_result['from']
        toAttr = json_result['to']
        result = Population.objects.filter(population__gte=fromAttr).filter(
            population__lt=toAttr).count()  # filter函数的使用
        # print(json_result)
        # print(Population.objects.order_by('-id'))  # 默认升序，-降序
        dic = {}
        dic['count'] = result
        dic = json.dumps(dic)
        return HttpResponse(dic)
    else:
        return HttpResponse("get")


def video(request):
    print(request.method)
    if request.method == 'POST':  # if后面没有大括号
        postBody = request.body
        json_result = json.loads(postBody)
        print(json_result)
        source = json_result['source']
        print(source)
        # toAttr = json_result['to']
        result = PollsVideo.objects.filter(video_source__iexact=source)  # filter函数的使用
        jsonData = serializers.serialize("json", result)
        #dic = {}
        #dic['list'] = jsonData
        #dic = json.dumps(dic) 序列化成字符串
        return HttpResponse(jsonData)  # json.dumps HttpResponse

    else:
        return HttpResponse("get")
