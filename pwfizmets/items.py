# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MeteoStamp(scrapy.Item):
    id = scrapy.Field()
    datetime_str = scrapy.Field()
    image_urls = scrapy.Field()
