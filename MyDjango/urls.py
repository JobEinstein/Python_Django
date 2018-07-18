"""MyDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MyBlog import views as MyBlog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', MyBlog_views.index, name='home'),
    path('', MyBlog_views.index),
    path('add/', MyBlog_views.add, name='add'),
    path('add/<int:a>+<int:b>/', MyBlog_views.index2add2),
    path('add2/<int:a>+<int:b>/', MyBlog_views.add2, name='add2'),
    # 修改新url
    path('new_add2/<int:a>/<int:b>/', MyBlog_views.add2, name='add2'),
    path('home/', MyBlog_views.home, name='home1'),
]
