# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
import logging

from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline

logger = logging.getLogger(__name__)

class PwfizmetsPipeline(ImagesPipeline):

    def file_path(self, request, response=None, info=None, *, item=None):
        img_type, file_ext = os.path.splitext(request.url.split('/')[-1])
        output_foldername = item['id'][:4]
        filepath = os.path.join(output_foldername, img_type, item['id'] + file_ext)
        logger.info('Saving an image: '+str(filepath))
        return str(filepath)
