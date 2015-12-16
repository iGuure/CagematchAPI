# -*- coding: utf-8 -*-

import scrapy
from WWEPhotos.items import WwephotosItem

class WWEPhotosSpider(scrapy.Spider):
	name = 'wwephotos'
	allowed_domains = ["wwe.com"]

	def __init__(self, url=None, *args, **kwargs):
		super(WWEPhotosSpider, self).__init__(*args, **kwargs)
		self.start_urls = [url]

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