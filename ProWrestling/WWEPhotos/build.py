import os

urls = [
		"http://www.wwe.com/shows/raw/2015-12-21/2015-slammy-award-winners-photos",
		"http://www.wwe.com/shows/raw/2015-12-21/stephanie-mcmahon-wipes-the-smile-off-roman-reigns-face-photos",
		"http://www.wwe.com/shows/raw/2015-12-21/kane-the-dudley-boyz-tommy-dreamer-vs-the-wyatt-family-photos",
		"http://www.wwe.com/shows/raw/2015-12-21/dolph-ziggler-vs-kevin-owens-photos",
		"http://www.wwe.com/shows/raw/2015-12-21/jack-swagger-vs-alberto-del-rio-photos",
		"http://www.wwe.com/shows/raw/2015-12-21/the-usos-vs-the-new-day-2-on-3-handicap-match-photos",
		"http://www.wwe.com/shows/raw/2015-12-21/neville-vs-rusev-photos",
		"http://www.wwe.com/shows/raw/2015-12-21/becky-lynch-vs-brie-bella-photos",
		"http://www.wwe.com/shows/raw/2015-12-21/dean-ambrose-vs-sheamus-steel-cage-match-photos",
		"http://www.wwe.com/shows/raw/2015-12-21/meet-the-2015-slammy-award-winners"
	]

for url in urls:
	os.system("scrapy crawl wwephotos -a url=%s -o items.json"%url)
	os.system("python output.py")
	os.system("del items.json")

f = open('output.txt', 'a+')
text = f.read()

print text.count("[img]")

f.close()