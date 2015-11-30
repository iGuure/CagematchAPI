# -*- coding: utf-8 -*-

import json

def readMovieJson():
	inFile = open("items.json", 'r', 0)
	text = inFile.read()
	movieDict = json.loads(text)
	for movie in movieDict:
		rank = movie["rank"][0]
		title = movie["title"][0]
		link = movie["link"][0]
		star = movie["star"][0]
		rate = movie["rate"][0]
		if movie["quote"]:
			quote = movie["quote"][0]
		else: quote = "暂无".decode("utf-8")

		print "top".decode("utf-8") + rank + ".".decode("utf-8") + title + " 评分".decode("utf-8") + star + '('.decode("utf-8") + rate + ')'.decode("utf-8") + "\n链接：".decode("utf-8") + link +  "\n豆瓣评论：".decode("utf-8") + quote + "\n"