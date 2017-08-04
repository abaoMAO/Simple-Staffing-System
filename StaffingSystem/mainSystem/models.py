#coding:utf-8
from django.db import models
from django.contrib.auth.models import User #MySQL扩展数据库用户表，一对一字段

# Create your models here.
class Employee(models.Model):
    name = models.CharField(verbose_name='姓名',max_length=20)
    age = models.IntegerField(verbose_name='年龄')
    telphone = models.CharField(verbose_name='手机',max_length=11)
    email = models.EmailField(verbose_name='邮箱',null=True,blank=True)
    add_date = models.DateTimeField(verbose_name='添加时间',auto_now_add=True)
    dpt = models.ForeignKey('Department')
    ptn = models.ForeignKey('Position')
    # 如果用ImageField字段类型 你需要安装Pillow模块  pip install Pillow
    # upload_to ： django-admin 上传路径
    avatar = models.ImageField(verbose_name='头像',upload_to='avatar',default='avatar/default.jpg')
    #upload_to = 'avatar', default = 'avatar/default.jpg'是给admin的ORM后台用的
    group = models.ManyToManyField('Group',verbose_name='参加社团')# 跟group公司社团表建立多对多关系

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '员工信息'

class Department(models.Model):
    name = models.CharField(verbose_name='部门名称',max_length=30,null=True,blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '部门信息'


class Position(models.Model):
    name = models.CharField(verbose_name='职位',max_length=30)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '职位信息' #ORM表名称显示成中文

class UserProfile(models.Model):
    telphone = models.CharField(verbose_name='手机',max_length=11)
    nick = models.CharField(verbose_name='昵称',max_length=30)
    user = models.OneToOneField(User)   #一对一关联扩展Django用户表

    class Meta:
        verbose_name = verbose_name_plural = '用户信息'


    def __unicode__(self):
        return self.nick #返回中文昵称

class Group(models.Model):
    name = models.CharField(verbose_name='社团名称',max_length=30)
    # group_ledder =    #社长

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = verbose_name_plural = '社团'
