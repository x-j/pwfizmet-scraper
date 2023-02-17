from scrapy import *

class PwfizmetSpider(Spider):

    def __init__(self, name, *kwargs):
        super().__init__(name, *kwargs)