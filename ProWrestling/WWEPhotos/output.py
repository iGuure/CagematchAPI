# -*- coding: utf-8 -*-

# This process is aimed at starting a picture post of WWE photos on a Discuz! forum

import sys
import json

def readWWEJson():
	reload(sys)
	sys.setdefaultencoding('utf-8')

	inFile = open("items.json", 'r', 0)
	text = inFile.read()
	WWEDict = json.loads(text)
	preTitle = None
	preSummary = None
	for WWE in WWEDict:
		title = WWE["title"][0]

		if preTitle != title:
			print "\n[b]".decode("utf-8") + title + "[/b]".decode("utf-8")
			preTitle = title

		if WWE["summary"]:
			summary = WWE["summary"][0]
			if preSummary != summary:
				print "\n".decode("utf-8") + summary
				preSummary = summary

		picURL = WWE["picURL"][0]
		if WWE["caption"]:
			caption = WWE["caption"][0]
			print "\n[img]".decode("utf-8") + picURL + "[/img]\n\n".decode("utf-8") + caption
		else:
			print "\n[img]".decode("utf-8") + picURL + "[/img]".decode("utf-8")

readWWEJson()