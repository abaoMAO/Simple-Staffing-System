#coding:utf-8
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
import models
from django.db.models import Q #用于搜索功能
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger  #用于分页处理、异常处理
from django.contrib.auth.decorators import login_required   #引入装饰器，用于登录之前的验证
from django.contrib import auth # 用于 登录 退出 验证
from django.contrib.auth.hashers import make_password #注册时密码用于加密
from django.contrib.auth.models import User
import os  #在这里用于文件存取
import uuid # 生成唯一标识符上传图片是用的
# Create your views here.

@login_required #引入装饰器，用于登录之前的验证
#########################################################################
def index(request):
    wd = request.GET.get('wd',None)     #用于搜索和排序的连调
    order = request.GET.get('order',None)   #用于排序字段
    rule = request.GET.get('rule',None)     #用于排序规则
    pn = request.GET.get('pn',1)    #刚进网页时，pn没有值默认指定为pn=1

    # pn 传过来时是Unicode类型，要转为int类型
    try:
        pn = int(pn)
    except Exception as e:  #第一次书写时except后面加了个:号导致错误，以后注意
        pn = 1
    #----------搜索功能-------------
    if wd is not None:
        # 一个Q就是一个条件 然后用并集操作符连接
        condition = Q(name__icontains=wd) | Q(age__icontains=wd) | Q(telphone__icontains=wd) | Q(email__icontains=wd)\
         | Q(dpt__name__icontains=wd) | Q(ptn__name__icontains=wd)
        empls = models.Employee.objects.filter(condition)   #根据条件获取员工对象
        # 耿健琪写的
        # a = models.Student.objects.filter(name__icontains=wd)
        # b = models.Student.objects.filter(score__icontains=wd)
        # stus = a | b
    else:
        empls = models.Employee.objects.all()  # 获取全部员工对象，放在这里实现搜索后排序,分页

    #-----------------排序功能-------------------
    if order is not None:
        if rule == 'u': #升序
            empls = empls.order_by(order)
        else:   #降序
            empls = empls.order_by(order).reverse()

    #-----------------分页-----------------------
    setPageNums = 3  # 用于设置每页显示的条数
    per_page = request.COOKIES.get('per_page',setPageNums)# 从客户端浏览器中读取每页显示记录条数的cookie值
    setPageNums = per_page    #用于设置每页显示的条数,利用cookie设置每页显示条数
    try:
        paginator = Paginator(empls,setPageNums) #返回一个分页对象，p1:Queryset p2:每页记录条数
        empls = paginator.page(pn) # 获取某一页的记录
    except (InvalidPage,EmptyPage,PageNotAnInteger) as e:
        pn = 1 #出现异常就跳到第一页
        paginator = Paginator(empls, setPageNums)
        empls = paginator.page(pn)  # 获取某一页的记录
        print e

    sumPages = empls.paginator.num_pages    #获取总页数

    #分页数字生成
    setPages = 5    #设置底部要显示的页码数，想要显示的数字个数
    if sumPages < setPages: # 最大页数小于你想要显示的数字个数
        start =1
        end = sumPages +1
    else:   # 最大页数大于等于你想要显示的数字个数
        if pn <= 2:     # 页数左边界
            start = 1
            end = setPages +1
        elif pn >= sumPages - 2:    #页数右边界
            start = sumPages - (setPages - 1)
            end = sumPages + 1  #加1是因为range左闭右开
        else:
            start = pn - int(setPages/2)
            end = pn + int(setPages/2) + 1



    page_nums = range(start,end)
    context = {
        'index':'active',
        'empls':empls,
        'page_nums':page_nums,
    }
    return render(request,'mainSystem/index.html',context)

######################################################################
#用于左侧边栏点击效果、页面跳转
def manage(request):
    context = {
        'manage':'active'
    }
    return render(request,'mainSystem/manage.html',context)

#######################################################################
#左侧边栏系统配置页面
def config(request):
    per_page = request.GET.get('per_page', None)  # 获取用户提交过来的每页显示记录条数
    context = {
        'config':'active',

    }
    if per_page is None:# 默认访问配置页则显示配置模板
        return render(request, 'mainSystem/config.html', context)
    else:# 提交的每页显示记录条数
        rep = HttpResponseRedirect('/mainSystem/config/')
        rep.set_cookie('per_page', per_page, max_age=3600 * 24 * 365)  # 设置一个长期有效cookie 每页记录条数
        return rep  # 做一个Http响应

#######################################################################
#左侧边栏高级查询页面
def advancedSearch(request):
    context = {
        'advancedSearch':'active'
    }
    return render(request, 'mainSystem/advancedSearch.html', context)

######################################################################
#增加部门
def add_dpt(request):
    # models.Department(name='销售部').save()
    # models.Department(name='行政部').save()
    # models.Department(name='技术部').save()
    # models.Department(name='后勤部').save()
    # models.Department(name='财务部').save()
    # models.Department(name='法务部').save()
    # models.Department(name='设计部').save()
    return HttpResponse('OK')


######################################################################
#增加职位
def add_position(request):
    # models.Position(name='总经理').save()
    # models.Position(name='副总经理').save()
    # models.Position(name='销售总监').save()
    # models.Position(name='财务总监').save()
    # models.Position(name='技术总监').save()
    # models.Position(name='经理').save()
    # models.Position(name='职员').save()
    # models.Position(name='技术员').save()
    # models.Position(name='总工程师').save()
    return HttpResponse('OK')

######################################################################
# 上传文件函数，代码复用
def upload(request,file): # file就是上传的文件
    if file.size / 1024 / 1024 < 2: #判断文件上传大小
        if file.content_type == 'image/jpeg' or file.content_type == 'image/gif': #判断文件类型
            # 把文件存到服务器上了
            # 按照文件名的.进行分割 然后取最后一项后缀名
            #uuid.uuid4()前面要导入import uuid # 生成唯一标识符
            new_name = str(uuid.uuid4()) + '.' + file.name.split('.')[-1]  # lelkr.jpg  kljer.gif

            fname = 'upload/avatar/' + new_name

            dirname = os.path.dirname(fname)  #获取路径名称

            if not os.path.exists(dirname): #如果不存在这个路径就创建一个

                os.makedirs(dirname)    # 创建多级目录
            ##----文件写入----
            with open(fname,'wb') as f: #二进制，写入打开方式
                if file.multiple_chunks():  # 多块文件
                    for chunk in file.chunks(): # 遍历文件的所有块
                        f.write(chunk)
                else: #单块文件
                    f.write(file.read())
            return True,new_name    # 上传成功返回True 和 文件的新名字
        else:
            return False,'文件类型只能是jpg或者gif'#返回False 和错误描述信息
    else:
        return False,'文件大小不能超过2M'   #返回False 和错误描述信息


######################################################################
#增加员工
def empl_add(request):
    if request.method == 'POST':
        name = request.POST.get('name',None)
        age = request.POST.get('age',None)
        telphone = request.POST.get('telphone',None)
        email = request.POST.get('email',None)
        dpt_id = request.POST.get('dpt_id',None)    # 部门id
        ptn_id = request.POST.get('ptn_id',None)    #职位id
        # 用过FILES字典获取单个上传文件 avatar是通过模板里intput标签的name属性决定的
        avatar = request.FILES.get('avatar',None)   # 获取到一个文件对象
        # print avatar.content_type # 文件上传类型
        # print avatar.size # 文件大小 单位是字节
        # print avatar.name # 文件名
        # print avatar.multiple_chunks() # 如果文件大于2.5M的时候返回True 反之返回False
        # return HttpResponse('ok')

        if avatar is not None:  # 如果文件不是None则获取文件对象成功
            res = upload(request,avatar)    #调用自己写的上传函数
            if res[0] is False: # 如果上传失败则返回错误描述
                return render(request,'mainSystem/empl_add.html',{'error':res[1]})
            else:   #上传成功
                new_name = res[1] # 获取返回的文件名字

        stu_info = {
            'name':name,
            'age':age,
            'telphone':telphone,
            'email':email,
            'dpt_id':dpt_id,
            'ptn_id':ptn_id,
            'avatar':'avatar/' + new_name # 头像的路径
        }
        models.Employee.objects.create(**stu_info)  #增加员工信息
        return HttpResponseRedirect('/')    #返回主页

    else:#get请求，没有传值的时候修改样式
        departments = models.Department.objects.all()   #获取部门对象
        positions = models.Position.objects.all()  # 获取职位对象
        context = {
            'manage':'active',#选中样式
            'departments':departments,
            'positions':positions,
        }
        return render(request,'mainSystem/empl_add.html',context)


######################################################################
#修改员工信息
def empl_edit(request):
    eid = request.GET.get('eid',None)   #获取要修改的员工的id
    if request.method == 'POST':
        name = request.POST.get('name', None)
        age = request.POST.get('age', None)
        telphone = request.POST.get('telphone', None)
        email = request.POST.get('email', None)
        dpt_id = request.POST.get('dpt_id', None)  # 部门id
        ptn_id = request.POST.get('ptn_id', None)  # 职位id
        avatar = request.FILES.get('avatar', None)  # 获取到一个文件对象
        # print avatar.content_type # 文件上传类型
        # print avatar.size # 文件大小 单位是字节
        # print avatar.name # 文件名
        # print avatar.multiple_chunks() # 如果文件大于2.5M的时候返回True 反之返回False
        # return HttpResponse('ok')

        if avatar is not None:  # 如果文件不是None则获取文件对象成功
            res = upload(request, avatar)  # 调用自己写的上传函数
            if res[0] is False:  # 如果上传失败则返回错误描述
                return render(request, 'mainSystem/empl_add.html', {'error': res[1]})
            else:  # 上传成功
                new_name = res[1]  # 获取返回的文件名字
        stu_info = {
            'name': name,
            'age': age,
            'telphone': telphone,
            'email': email,
            'dpt_id': dpt_id,
            'ptn_id': ptn_id,
            'avatar':'avatar/' + new_name #头像路径
        }
        models.Employee.objects.filter(id=eid).update(**stu_info)  # 修改员工信息
        return HttpResponseRedirect('/')  # 返回主页
    else:#没有传值的时候调用
        empl = models.Employee.objects.get(id=eid)  #获取要修改的员工对象
        departments = models.Department.objects.all()   #获取部门对象
        positions = models.Position.objects.all()   #获取职位对象
        return render(request,'mainSystem/empl_add.html',{'empl':empl,'departments':departments,'positions':positions})

######################################################################
#删除员工
def empl_del(request):
    eid = request.GET.get('eid',None)
    if eid is not None:
        models.Employee.objects.filter(id=eid).delete() #删除操作
        return HttpResponseRedirect('/')    #重定向到首页
    return HttpResponse('OK')

######################################################################
#登录
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        if username is not None:
            # 对账户进行验证，如果验证成功返回用户对象，如果失败返回None
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:  #user存在为True的话，进行登录操作
                    #做登录操作
                    auth.login(request,user)
                    return HttpResponseRedirect('/')    #返回首页
                else:
                    return render(request,'mainSystem/login.html',{'error':'账号已冻结'})
            else:
                return render(request,'mainSystem/login.html',{'error':'账号名或密码错误'})
    else:
        return render(request,'mainSystem/login.html')

######################################################################
# 退出登录
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')

######################################################################
#注册
def reg(request):
    if request.method == 'POST':
        #收集用户信息
        username = request.POST.get('username',None)
        password1 = request.POST.get('password1',None)
        password2 = request.POST.get('password2',None)
        nick = request.POST.get('nick','')
        telphone = request.POST.get('telphone','')

        print username

        if username and password1 and password2:
            if password1 == password2:
                u_count = User.objects.filter(username=username).count()
                if u_count == 0: #没有这个用户名

                    # 添加自带用户表
                    user_info = {
                        'username' : username,
                        'password' : make_password(password1),  #对密码进行加密
                    }
                    user_info = User.objects.create(**user_info)

                    # 添加用户扩展信息
                    user_profile = {
                        'nick' : nick,
                        'telphone' : telphone,
                        'user' : user_info
                    }

                    models.UserProfile.objects.create(**user_profile)

                    return HttpResponseRedirect('/login/')

                else: #用户名已存在
                    return render(request,'mainSystem/reg.html',{'error':'用户名已存在'})
            else:
                return render(request,'mainSystem/reg.html',{'error':'两次密码不一样'})

    else:
        return render(request,'mainSystem/reg.html')


##-----------------ajax 验证用户名是否存在---------------
def checkname(request):
    name = request.GET.get('name',None)
    res = models.User.objects.filter(username=name).count() #到数据库当中验证用户名是否存在
    if res == 0: #如果用户名不存在
        return HttpResponse('ok')
    else:#用户名不存在
        return HttpResponse('用户名已存在')