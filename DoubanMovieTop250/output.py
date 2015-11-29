import json

def readMovieJson():
	inFile = open("E:\Github\CagematchAPI\DoubanMovieTop250\items.json", 'r', 0)
	text = inFile.read()
	movieDict = json.loads(text)
	for movie in movieDict:
		rank = movie["rank"][0]
		title = movie["title"][0]

		print "top".decode("utf-8") + rank + ".".decode("utf-8") + title + "\n"