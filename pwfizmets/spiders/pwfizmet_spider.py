from scrapy import *
from pwfizmets.items import MeteoStamp

class PwfizmetSpider(Spider):

    name = 'meteos'

    def __init__(self, url, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.start_urls = [url]
        

    def parse(self, response):
        stamp = MeteoStamp()
        stamp['datetime_str'] =  response.css('td[colspan="4"] b::text').get()
        stamp['id'] = f"{stamp['datetime_str'].split(' ')[0][2:].replace('-','')}_{'{:0>5}'.format(stamp['datetime_str'].split(' ')[1].replace(':','-'))}"

        # images
        stamp['image_urls'] = []
        for s in response.css('img[src^="warszawa"]::attr(src)'):
            # skip wiatrs
            if s.get().startswith('warszawapw/wiatr-'): continue
            stamp['image_urls'].append(response.url+s.get())
        
        yield stamp