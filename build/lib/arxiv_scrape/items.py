# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ArxivScrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #arxiv代码
    Id = scrapy.Field()    
    #标题
    title = scrapy.Field()
    #作者
    authors = scrapy.Field()
    #学科
    category = scrapy.Field()
    #首要子学科
    primary_subject = scrapy.Field()
    #pdf链接
    link = scrapy.Field()
    #论文提交日期
    date = scrapy.Field()
    #论文摘要
    abstract = scrapy.Field()
    #子学科列表，除了首要子学科外，可能属于别的子学科
    subjects = scrapy.Field()
