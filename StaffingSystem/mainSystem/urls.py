#coding:utf-8

from django.conf.urls import url
import views
from django.views.static import serve # 处理媒体文件的API
from django.conf import settings # 把django 的配置文件导入进来

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^manage/$',views.manage,name='manage'),
    url(r'^advancedSearch/$',views.advancedSearch,name='advancedSearch'),
    url(r'^add_dpt/$',views.add_dpt,name='add_dpt'),
    url(r'^add_position/$',views.add_position,name='add_position'),
    url(r'^config/$',views.config,name='config'),#系统配置
    url(r'^empl_add/$',views.empl_add,name='empl_add'),
    url(r'^empl_edit/$', views.empl_edit,name='empl_edit'),
    url(r'^empl_del/$', views.empl_del,name='empl_del'),
    url(r'^login/$',views.login,name='login'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^reg/$',views.reg,name='reg'),
    # 写一个媒体文件的url 并且用serve函数处理 指定媒体文件的路径
    url(r'^upload/(.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^checkname/$', views.checkname,name='checkname'),
]