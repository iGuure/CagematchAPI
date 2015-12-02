# -*- coding: utf-8 -*-

import scrapy
from WWEPhotos.items import WwephotosItem

class WWEPhotosSpider(scrapy.Spider):
	name = 'wwephotos'
	allowed_domains = ["wwe.com"]
	start_urls = [ # Please write the URLs from the bottom up
		"http://www.wwe.com/inside/wwe-app-backstage-peeks-november-2014-photos",
		"http://www.wwe.com/inside/25-best-instagram-photos-week-11-29-2015"
	]

	def parse(self, response):
		item = WwephotosItem()
		item["title"] = response.xpath('//div[@class="content"]/h1[@class="cf"]/text()').extract()
		item["summary"] = response.xpath('//div[@class="content"]/div[@class="lb-wrap"]/div[@class="summary"]/p/text()').extract()
		for info in response.xpath('//div[@class="stage-inner"]/div[contains(@class, "slide")]'):
			if info.xpath('img/@realsrc'):
				item['picURL'] = info.xpath('img/@realsrc').extract()
			else:
				item['picURL'] = info.xpath('img/@src').extract()
			item['caption'] = info.xpath('div[@class="caption"]/text()').extract()
			yield item