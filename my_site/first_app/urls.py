from django.urls import path
from . import views
from django.http.response import HttpResponse


def home_view(request):
    return HttpResponse("first_app Home page")
# first_app/

urlpatterns = [
    path("", home_view),
    path("<int:num_page>", views.num_page_view),
    path('<str:topic>/',views.news_view,name='topic-page'),
]
