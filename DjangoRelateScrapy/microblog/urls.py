# Author:blue
from django.urls import path
from . import views

app_name = 'microblog'

urlpatterns = [
    path('', views.weibo, name='weibo'),
    path('detail/<int:num>/', views.detail, name='detail'),
    path('freshNewsInfo/<int:num>/', views.freshNewsInfo, name='pageInfo'),
    path('topevent/<int:num>/', views.topEventInfo, name='topEventInfo'),
    path('toplist/<int:num>/', views.topListInfo, name='topListInfo'),
    path('funnystory/<int:num>/', views.funnyStoryInfo, name='funnyStoryInfo'),
    path('fashion/<int:num>/', views.fashionInfo, name='fashionInfo'),
    path('society/<int:num>/', views.societyInfo, name='societyInfo'),
    path('search/', views.search, name='search'),
]
