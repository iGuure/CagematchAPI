# -*- coding: utf-8 -*-

import scrapy
from TNAPhotos.items import TnaphotosItem

class TNARosterPhotosSpider(scrapy.Spider):
	name = 'tnarosterphotos'
	allowed_domains = ["impactwrestling.com"]
	start_urls = [
		"http://www.impactwrestling.com/roster/Wrestler-Roster"
	]

	def parse(self, response):
		item = TnaphotosItem()
		for info in response.xpath('//div[@class="catItemBody"]//a'):
			item['name'] = info.xpath('@title').extract()
			item['link'] = info.xpath('@href').extract()
			yield item