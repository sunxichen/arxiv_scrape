# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy import signals
from scrapy.exporters import CsvItemExporter
from scrapy.pipelines.files import FilesPipeline
import re, string

class ArxivScrapePipeline(object):
    def process_item(self, item, spider):
        return item

class CsvPipeline(object):
    def __init__(self):
        self.file = open(r"arxiv_new.csv", 'wb')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

class DownloadPapersPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        paper_url = item['link']
        yield scrapy.Request(paper_url, meta={'item':item['title']})
    def file_path(self, request, response=None, info=None):
        paper_name = request.meta['item']
        paper_name = re.sub("[\*:\?<>\|/\\\"]+", '', str(paper_name))
        print(paper_name)
        return 'download/%s.pdf' % paper_name