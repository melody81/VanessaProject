#coding:utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

#urls是访问地址和函数的对应表
#新建models.py是数据库
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jeapblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^test$', 'jeapblog.views.test'),
	url(r'^test/(\d+)$', 'jeapblog.views.test1'),#^是起始，$是结束,()是可动的,有（）的在views中多一个参数,
	#有几个圆括号，就有几个参数，正则的方法，可以把圆括号中的内容提取出来。
	#print re.findall("a(.*?)d.*?g","abcdefg") #返回一个 bc。虽然两个正则都做了匹配，但是只返回一个
	#print re.findall("a(.*?)d(.*?)g","abcdefg")#返回两个
	url(r'^admin/', include(admin.site.urls)),
	url(r'^dt$','jeapblog.views.dt'),
	url(r'^delete/(\d+)$','jeapblog.views.delete'),
	url(r'^edit/(\d+)$','jeapblog.views.edit'),
)
