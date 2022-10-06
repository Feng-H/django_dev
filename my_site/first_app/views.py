from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect 
from django.urls import reverse

# Create your views here.

# articles = {
#     'sports':'sports page',
#     'finance':'finance page',
#     'politics':'politices page'
# }

# def news_view(request,topic):
#     try:
#         result = articles[topic]
#         return HttpResponse(articles[topic])
#     except:
#         result = "no page for that topic!"
#         return HttpResponseNotFound(result)

# def num_page_view(request,num_page):
#     topics_list = list(articles.keys())
#     topic = topics_list[num_page]
    
#     return HttpResponseRedirect(reverse('topic-page',args=[topic]))

def simple_view(request):
    return render(request, 'first_app/example.html')