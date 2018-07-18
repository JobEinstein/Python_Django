from django.shortcuts import render

# Create your views here.

# coding:utf-8
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'home.html')


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


# 跳转页面方法

def index2add2(request, a, b):
    return HttpResponseRedirect(reverse('add2', args=(a, b)))


def home(request):
    title = u"多多啦啦梦的世界"
    menuList = ["python", "AI"]
    info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    listadd = map(str, range(10))
    sorce = 99
    num = 73
    return render(request, 'home1.html', {'string1': title, 'list1': menuList, 'dict': info_dict, 'list2': listadd, 'var':
                                          sorce, 'num': num})

    def db(request):
        pass
