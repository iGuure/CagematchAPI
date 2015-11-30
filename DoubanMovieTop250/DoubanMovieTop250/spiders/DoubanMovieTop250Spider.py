import scrapy
from DoubanMovieTop250.items import Doubanmovietop250Item

class DoubanMovieTop250Spider(scrapy.Spider):
	name = 'doubanmovietop250'
	allowed_domains = ["douban.com"]
	start_urls = [
		"http://movie.douban.com/top250/"
	]

	def parse(self, response):
		for info in response.xpath('//div[@class="item"]'):
			item = Doubanmovietop250Item()
			item['rank'] = info.xpath('div[@class="pic"]/em/text()').extract()
			item['title'] = info.xpath('div[@class="pic"]/a/img/@alt').extract()
			item['link'] = info.xpath('div[@class="pic"]/a/@href').extract()
			item['star'] = info.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()
			item['rate'] = info.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[last()]/text()').extract()
			item['quote'] = info.xpath('div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span/text()').extract()
			yield item

		nextPage = response.xpath('//span[@class="next"]/a/@href')
		if nextPage:
			url = response.urljoin(nextPage[0].extract())
			yield scrapy.Request(url, self.parse)