#!/usr/bin/env python
#coding=utf-8
import urllib2
import re
import os

def getindex(html):

	pos1 = html.find("panel_body", 0)

	pos2 = html.find("newsUname", pos1)

	html = html[pos1:pos2]

	html = extraHtml(html)
	
	item = re.sub("&nbsp;","",html)

	return item

def spider(url):
	
	url="http://today.hitwh.edu.cn/"+url

	#print url

	html = urllib2.urlopen(url).read() 

	html = getindex(html)

	#print html

	return html



def mkdir(path,text):

	path = path.strip()

	isExits=os.path.exists(path)

	if not isExits:

		print u"bulid a folder called",path

		#os.makedirs(path)

		path=path+"txt"

		f=open(path,'w')

		f.write(text)

		f.close()

		return True

	else:

		print u"the name that called",path,'has been build successfully'

		path=path+".txt"

		f=open(path,'w')

		f.write(text)

		f.close()

		return False



def extraHtml(html):

	#html='<a href="http://www.jb51.net">脚本之家</a>,Python学习！'
	dr = re.compile(r'<[^>]+>',re.S)
	dd = dr.sub('',html)
	
	return dd



	


def getPage(html):

	pos1 = html.find("righ_list", 0)

	pos2 = html.find("</div>", pos1)

	html = html[pos1:pos2]

	#print html

	p = re.compile(r"href=(.{0,30})>(.{0,100})</a>")

	
	items=p.findall(html)

	link=[]

	#print items

	n = 0

	for item in items:

		n=n+1

		#item[0]="http://today.hitwh.edu.cn/"+str(item[0])

		#print item,n

		#print item[0]

		#print item[1]

		#mkdir(item[1])

		text = spider(item[0])

		print text

		mkdir(item[1],text)

		link.append([item[0],item[1]])







	
	#return href_list


url = "http://today.hitwh.edu.cn/news_more_list.asp?id=7"

html = urllib2.urlopen(url).read()

getPage(html)





#print extraHtml(html)