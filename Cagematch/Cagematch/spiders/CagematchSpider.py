# -*- coding: utf-8 -*-

import scrapy
from Cagematch.items import CagematchItem

class CagematchSpider(scrapy.Spider):
	name = 'cagematch'
	allowed_domains = ["cagematch.net"]
	start_urls = [
		"http://www.cagematch.net/?id=2&view=topflop"
	]

	def parse(self, response):
		item = CagematchItem()
		for info in response.xpath('//table[contains(@class, "TBase")]/tr[@class="TRow"]'):
			item['rank'] = info.xpath('td[1]/text()').extract()
			item['gimmick'] = info.xpath('td[3]/a/text()').extract()
			item['birthplace'] = info.xpath('td[4]/text()').extract()
			item['height'] = info.xpath('td[5]/text()').extract()
			item['weight'] = info.xpath('td[6]/text()').extract()
			if info.xpath('td[7]/a'):
				item['promotion'] = info.xpath('td[7]/a/img/@title').extract()
			item['rating'] = info.xpath('td[8]/span/text()').extract()
			yield item