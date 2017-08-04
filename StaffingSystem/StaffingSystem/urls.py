#coding:utf-8
"""StaffingSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from mainSystem import urls as mainSystem_urls
from mainSystem import views as mainSystme_views
from django.views.static import serve # 处理媒体文件的API
from django.conf import settings # 把django 的配置文件导入进来

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),  # ORM数据库
    url(r'^$',mainSystme_views.index,name='index'), #系统首页和主项目的首页设置成一样的
    # StaffingSystem和mainSystem都配置了login，
    # 这样127.0.0.1:8003/login和127.0.0.1:8003/mainSystem/login都能调取views的login函数了
    url(r'^login/$',mainSystme_views.login,name='login1'),
    url(r'^logout/$',mainSystme_views.logout,name='logout'),
    url(r'^reg/$',mainSystme_views.reg,name='reg'),
    url(r'^mainSystem/',include(mainSystem_urls,namespace='mainSystem')),
    url(r'^checkname/$', mainSystme_views.checkname,name='checkname'),
    #写一个媒体文件的url 并且用serve函数处理 指定媒体文件的路径
    url(r'^upload/(.*)$', serve,{'document_root':settings.MEDIA_ROOT}),
]
