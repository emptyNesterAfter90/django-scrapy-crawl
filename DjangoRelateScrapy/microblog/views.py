from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from microblog.models import HotSpot, FreshNews, TopEvent, TopList, FunnyStory, Fashion, Society


def weibo(request):
    return render(request, 'weibo.html')


def detail(request, num=1):
    list = HotSpot.objects.order_by('-approve')
    paginator = Paginator(list, 10)

    page = paginator.page(num)

    return render(request, 'weibo.html', {'spotList': page, 'key': 'detail'})


def freshNewsInfo(request, num=1):
    list = FreshNews.objects.all()
    paginator = Paginator(list, 10)

    page = paginator.page(num)

    return render(request, 'weibo.html', {'spotList': page, 'key': 'freshNewsInfo'})


def topEventInfo(request, num=1):
    list = TopEvent.objects.order_by('-approve')
    paginator = Paginator(list, 10)

    page = paginator.page(num)

    return render(request, 'weibo.html', {'spotList': page, 'key': 'topevent'})


def topListInfo(request, num=1):
    list = TopList.objects.order_by('-approve')
    paginator = Paginator(list, 10)

    page = paginator.page(num)

    return render(request, 'weibo.html', {'spotList': page, 'key': 'toplist'})


def funnyStoryInfo(request, num=1):
    list = FunnyStory.objects.order_by('-approve')
    paginator = Paginator(list, 10)

    page = paginator.page(num)

    return render(request, 'weibo.html', {'spotList': page, 'key': 'funnystory'})


def fashionInfo(request, num=1):
    list = Fashion.objects.order_by('-approve')
    paginator = Paginator(list, 10)

    page = paginator.page(num)

    return render(request, 'weibo.html', {'spotList': page, 'key': 'fashion'})


def societyInfo(request, num=1):
    list = Society.objects.order_by('-approve')
    paginator = Paginator(list, 10)

    page = paginator.page(num)

    return render(request, 'weibo.html', {'spotList': page, 'key': 'society'})


def search(request):
    q = request.GET.get('q')
    print(q)
    error_msg = ''

    list = []
    details = HotSpot.objects.filter(content__icontains=q)
    for k in details:
        list.append(k)
    society = Society.objects.filter(content__icontains=q)
    for k in society:
        list.append(k)
    fashion = Fashion.objects.filter(content__icontains=q)
    for k in fashion:
        list.append(k)
    funny = FunnyStory.objects.filter(content__icontains=q)
    for k in funny:
        list.append(k)
    topList = TopList.objects.values('id').filter(content__icontains=q).distinct()
    for k in topList:
        list.append(k)
    topEvent = TopEvent.objects.filter(content__icontains=q)
    for k in topEvent:
        list.append(k)
    freshNews = FreshNews.objects.filter(content__icontains=q).distinct()
    for k in freshNews:
        list.append(k)
    print(len(list))
    return render(request, 'weibo.html', {'error_msg': error_msg, 'spotList': list})


