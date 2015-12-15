# -*- coding: utf-8 -*-

import scrapy
from TNAPhotos.items import TnaphotosItem

class TNAAlunmiPhotosSpider(scrapy.Spider):
	name = 'tnaalumniphotos'
	allowed_domains = ["impactwrestling.com"]
	start_urls = [
		"http://www.impactwrestling.com/roster/Wrestler-Roster"
	]

	def parse(self, response):
		item = TnaphotosItem()
		for info in response.xpath('//li[contains(@class, "alumni-list-item")]'):
			item['name'] = info.xpath('a/img/@alt').extract()
			item['link'] = info.xpath('a/@href').extract()
			yield item