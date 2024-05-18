# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FreelancerItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    detail = scrapy.Field()
    tags = scrapy.Field()
    about = scrapy.Field()
    client = scrapy.Field()
