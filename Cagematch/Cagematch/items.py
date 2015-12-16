# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CagematchItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank = scrapy.Field()
    gimmick = scrapy.Field()
    birthplace = scrapy.Field()
    height = scrapy.Field()
    weight = scrapy.Field()
    promotion = scrapy.Field()
    rating = scrapy.Field()