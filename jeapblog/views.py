#coding:utf-8
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext #解决csrf token错误
from jeapblog.models import Blog

#Views是访问地址和函数的对应表
'''
def test(request): #客户传request
	return HttpResponse("hello world %s" % datetime.datetime.now()) #返回给客户的浏览器内容
	#根据客户传的不同参数，从数据库中查找并返回相应内容
'''
def test1(request, d): 
	res = datetime.datetime.now()
	if d == '2':
		res = datetime.date.today()
	if d == '1':
		res = datetime.datetime.now().strftime('%X')
	return HttpResponse("hello world %s" % res)

'''
def test(request):
	n = "Vanessa1"
	age = 20
	t = Template('My name is {{ name }}. Age is {{age}}')
	c = Context({'name': n, "age": age})
	return HttpResponse(t.render(c))
'''

def test(request):
	if request.method == 'POST':
		#print request.POST
		#print request.POST['a']
		Blog(title = request.POST['a']).save()
	blogs = Blog.objects.all()
	d = {'color':'#f00'}
	d["name"] = 'jack'
	d['age'] = 10
	d['blogs']=blogs
	return render_to_response('test.html', d,context_instance=RequestContext(request))

import json
def dt(request):
	Mydata = datetime.datetime.now()
	return HttpResponse(json.dumps({"Mydata":'%s' % Mydata}))#字典变成文本
	#{"Mydata": "2014-07-13 13:27:33.955000"}
#在APP jeapblog下创建templates 目录
#test --> test.html --> dt and success:function(data)-->

def delete(request,id):
	a = Blog.objects.get(id =int(id))
	a.delete()
	return redirect('/test')
	'''
	blogs = Blog.objects.all()
	for b in blogs:
		if b.id == int(id):
			b.delete()
			return redirect('/test')
'''
def edit(request,id):
	if request.method=="GET":
		b = Blog.objects.get(id = int(id))
		return render_to_response('edit.html',{'bbbbb':b},context_instance=RequestContext(request))
		#上面的函数将edit.html中定义的bbbbb都换成b，因为b是个object。所以b.title会返回在edit.html定义的a输入框中
		#edit页面中的发送函数
	if request.method == 'POST':
		b = Blog.objects.get(id = int(id))
		b.title = request.POST['a']
		b.save()
		return redirect('/test')