# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ExpectItem(scrapy.Item):
    # define the fields for your item here like:
    symbol = scrapy.Field()
    type = scrapy.Field()
    r0 = scrapy.Field()
    r1 = scrapy.Field()
    r2 = scrapy.Field()
    pass
