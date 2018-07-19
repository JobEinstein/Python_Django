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
  **前三种返回object,最后一种返回元组(object,True/False)

  5.当有一对多，多对一，或者多对多的关系的时候，先把相关的对象查询出来
    test = 表名.objects.get(pk=1)
    表字段 = 表名.objects.get(表字段=...)
    test.blog = 表字段
    test.save()
查询数据:  表名.objects.get(表字段=...)




git建ssh密钥
git config --global user.name "JobEinstein"

git config --global user.email "1107273806@qq.com"

ssh-keygen -t rsa -C "1107273806@qq.com"

git提交忽略密码
git config --global credential.helper store1



