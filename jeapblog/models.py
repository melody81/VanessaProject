#coding:utf-8
from django.db import models
class Blog(models.Model): #表， 括号里面是父类，继承django model提供的方法
	title = models.CharField(max_length = 140)#字段

'''
python manage.py syncdb
python manage.py shell
from jeapblog.models import Blog
b = Blog() #创个空的记录
b.title = "Vanessa's blog!"#给字段赋值
b.save()
b1 = Blog(title='第二个博客')
b1.save()
Blog(title = '第三个博客').save()

In [5]: all = Blog.objects.all()

In [6]: all.count()
Out[6]: 3

In [7]: for a in all:
   ...:     print a.title,a.id
   ...:
第三个博客 1
第2个博客 2
第1个博客 3

#blogs2 = Blog.objects.filter(title__contains = 'title')
blogs2 = Blog.objects.filter(id__gte = '2')
blogs = Blog.objects.filter() #等价于Blog.objects.all()
blogs3 = Blog.objects.filter().order_by('-id') #id是1-5， -id是5-1
for b in blogs2:
	print b.title

In [8]: a = Blog.objects.get(id =1)

In [11]: a.title = "第一条博客！！！"

In [13]: a.save()

In [14]: all = Blog.objects.all()

In [15]: for a in all:
   ....:     print a.title
   ....:
第一条博客！！！
第2个博客
第1个博客

In [16]:a.delete()

sqlalchemy库支持mysql，sqllite3，oracle等 --》 django.db --> models

'''