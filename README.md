网址对应   	urls.py
项目的设置 	settings.py 
部署服务器	 wsgi.py
python调用	__init__.py
访问页面内容		views.py
数据库   models.py

变量							描述
forloop.counter			索引从 1 开始算
forloop.counter0		索引从 0 开始算
forloop.revcounter		索引从最大长度到 1
forloop.revcounter0		索引从最大长度到 0
forloop.first			当遍历的元素为第一项时为真
forloop.last			当遍历的元素为最后一项时为真

forloop.parentloop		用在嵌套的 for 循环中，
						获取上一层 for 循环的 forloop

新建一个项目 python django-admin.py startproject 项目名 
新建一个app python django-admin.py startapp app名
将app添加到项目中  settings.py 中的 INSTALLED_APPS
添加表名        models.py中添加 settings.py中配置mysql数据库
项目导入mysql   __init__.py 添加(import pymysql pymysql.install_as_MySQLdb()
)
同步数据库 python manage.py makemigrations python manage.py migrate
启动服务  python manage.py runserver 
指定端口 python manage.py runserver 8001

打印sql执行语句
  settings.py 尾部加上
    LOGGING = {
      'version': 1,
      'disable_existing_loggers': False,
      'handlers': {
          'console': {
              'class': 'logging.StreamHandler',
          },
      },
      'loggers': {
          'django.db.backends': {
              'handlers': ['console'],
              'level': 'DEBUG' if DEBUG else 'INFO',
          },
      },
  }
  并且 DEBUG = True

mysql操作
安装MySQLdb模块
建数据库 create database 库名 default charset=utf8;
分配权限 grant all privileges on 库名.* to '用户名'@'localhost' identified by '用户密码';
配置mysql数据库 
		'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mall',
        'USER': 'rinka',
        'PASSWORD': 'rinka0414',
        'HOST': 'localhost',
        'PORT': '3306',
DATABASE_ENGINE 即为“背景”中所提到的那些数据库服务器

DATABASE_NAME 将数据库名称告知 django

DATABASE_USER 告诉 django 用哪个用户连接数据库

DATABASE_PASSWORD 告诉django连接用户的密码

DATABASE_HOST 告诉 django 连接哪一台主机的数据库服务器

DATABASE_PORT 告诉 django 连接数据库时使用哪个端口

 
python manage.py shell 调出python窗口




数据库数据插入查询
from app名.models import 表名
插入数据:
  1.表名.objects.create(表字段=...) 
  2.from app名.models import 表名 
   	test=表名(字段赋值) 
   	test.save()
  3.test=表名()
    test.字段=" "..
    test.save()
  4.防止数据重复
  	表名.objects.get_or_create(表字段=...)
  前三种返回object,最后一种返回元组(object,True/False)
  5.当有一对多，多对一，或者多对多的关系的时候，先把相关的对象查询出来
    test = 表名.objects.get(pk=1)
    表字段 = 表名.objects.get(表字段=...)
    test.blog = 表字段
    test.save()
查询数据: 
  表名.objects.all().distinct() 去重 
  表名.objects.get(表字段=...)
  表名.objects.all() 查询出的是所有的表名条目
  get是用来获取一个对象的，如果需要获取满足条件的一些人，就要用到filter
  表名.objects.filter(表字段="abc") # 等于Person.objects.filter(name__exact="abc") 名称严格等于 "abc" 的人
  表名.objects.filter(表字段__iexact="abc") # 名称为 abc 但是不区分大小写，可以找到 ABC, Abc, aBC，这些都符合条件 
  表名.objects.filter(表字段__contains="abc") # 名称中包含 "abc"的人
  表名.objects.filter(表字段__icontains="abc") #名称中包含 "abc"，且abc不区分大小写 
  表名.objects.filter(表字段__regex="^abc") # 正则表达式查询
  表名.objects.filter(表字段__iregex="^abc")# 正则表达式不区分大小写 
  # filter是找出满足条件的，当然也有排除符合某条件的
  表名.objects.exclude(表字段__contains="WZ") # 排除包含 WZ 的Person对象
  表名.objects.filter(表字段__contains="abc").exclude(表字段=23) # 找出名称含有abc, 但是排除年龄是23岁的
删除数据:
  表名.objects.filter(表字段__contains="abc").delete() # 删除 名称中包含 "abc"的人
更新数据:
  1.批量更新，适用于 .all()  .filter()  .exclude() 等后面 (危险操作，正式场合操作务必谨慎)
  表名.objects.filter(表字段__contains="abc").update(表字段='xxx') # 名称中包含 "abc"的人 都改成 xxx
  表名.objects.all().delete() # 删除所有 Person 记录
  2.单个 object 更新，适合于 .get(), get_or_create(), update_or_create() 等得到的 obj，和新建很类似
  表名参数 = 表名.objects.get(表字段="WeizhongTu")
  表名.表字段="xxx"
  表名.表字段="xxx"
  表名.save()  # 最后不要忘了保存！！！
注意事项：
(1). 如果只是检查 Entry 中是否有对象，应该用 Entry.objects.all().exists()
(2). QuerySet 支持切片 Entry.objects.all()[:10] 取出10条，可以节省内存
(3). 用 len(表名参数) 可以得到Entry的数量，但是推荐用 Entry.objects.count()来查询数量，后者用的是SQL：SELECT COUNT(所有)
(4). list(表名参数) 可以强行将 QuerySet 变成 列表

pickle序列化:
  import pickle
  query = pickle.loads(s)    # Assuming 's' is the pickled string. 
  qs = MyModel.objects.all()
  qs.query = query   # Restore the original 'query'.
排序:
  表名.objects.all().order_by('表字段') 顺序
  表名.objects.all().order_by('-表字段') 倒序
链式查询:
  表名.objects.filter(表字段__contains="WeizhongTu").filter(表字段="tuweizhong@163.com")
  表名.objects.filter(表字段__contains="Wei").exclude(表字段="tuweizhong@163.com") 
  # 找出名称含有abc, 但是排除年龄是23岁的
  表名.objects.filter(表字段__contains="abc").exclude(表字段=23)
不支持负索引:
  表名.objects.all()[:10] 切片操作，前10条
  表名.objects.all()[-10:] 会报错！！！ 
  # 1. 使用 reverse() 解决
  表名.objects.all().reverse()[:2] # 最后两条
  表名.objects.all().reverse()[0] # 最后一条
  # 2. 使用 order_by，在栏目名（column name）前加一个负号
  表名.objects.order_by('-表字段')[:20] # 表字段最大的20条

数据导入:
  脚本放在项目目录下

QuerySet 进阶:
  
 


git建ssh密钥
git config --global user.name "JobEinstein"

git config --global user.email "1107273806@qq.com"

ssh-keygen -t rsa -C "1107273806@qq.com"

git提交忽略密码
1.创建文件 .git-credentials 加入https://{username}:{password}@github.com
git config --global credential.helper store
2.新建环境变量HOME，值为%USERPROFILE%
新建文件_netrc 加入machine git.xxx.com login user_name password user_pwd

git从远程克隆项目
git clone 地址

cmd下建文件
echo b>.git-credentials

