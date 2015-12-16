# -*- coding: utf-8 -*-

import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from TNAPhotos.items import TnaphotosItem

class TNAPhotosSpider(CrawlSpider):
	name = 'tnaphotos'
	allowed_domains = ["impactwrestling.com"]
	start_urls = [
		"http://www.impactwrestling.com/roster/Wrestler-Roster"
	]

	rules = ( # Crawl the links and put them into start_urls
		Rule(
			# Some limitation to the links. See the API doc for more paras.
			LinkExtractor(restrict_xpaths=('//div[@class="catItemBody"]', '//li[contains(@class, "alumni-list-item")]'), ),
			# Attention: This callback function can't be 'parse', as it's already existed in the CrawlSpider. Use another name instead.
			callback="parse_start_url"
		),
	)

	def parse_start_url(self, response):
		item = TnaphotosItem()
		item['name'] = response.xpath('//title/text()').extract()
		for info in response.xpath('//ul[contains(@class, "sigProContainer")]'):
			item['link'] = info.xpath('li//a/@href').extract()
			yield item