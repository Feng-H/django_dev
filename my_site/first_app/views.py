from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
# Create your views here.

articles = {
    'sports':'sports page',
    'finance':'finance page',
    'politics':'politices page'
}

def news_view(request,topic):
    try:
        result = articles[topic]
        return HttpResponse(articles[topic])
    except:
        result = "no page for that topic!"
        return HttpResponseNotFound(result)
