# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FreelancerItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    detail = scrapy.Field()
    tags = scrapy.Field()
    client = scrapy.Field()
