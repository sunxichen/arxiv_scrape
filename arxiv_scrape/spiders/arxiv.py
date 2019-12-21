# -*- coding: utf-8 -*-
import scrapy
import re
import json
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
# from scrapy.selector import HtmlXPathSelector
from scrapy.utils.url import urljoin_rfc
from scrapy.http import Request
# from items import ArxivScrapeItem
from .. import items

class ArxivSpider(scrapy.Spider):
    name = 'arxiv'
    allowed_domains = ['arxiv.org']
    start_urls = ['http://arxiv.org/']

    
    months = {
        "Jan":"01"
        # "Feb":"02",
        # "Mar":"03",
        # "Apr":"04",
        # "May":"05",
        # "Jun":"06"
        # "July":"07",
        # "Aug":"08",
        # "Sep":"09",
        # "Oct":"10",
        # "Nov":"11",
        # "Dec":"12"
    }

    
    def start_requests(self):
        for k, v in list(self.months.items()):
            year = '19'
            
            for i in range(1,16000):
                s = str(i)
                s = s.zfill(5)
                url = "https://arxiv.org/abs/"+year+v+"."+s
                yield Request(url=url, callback = self.parse_item, meta={'month':v})

    

    def parse_item(self,response):
        
        m = response.meta['month']
        item = items.ArxivScrapeItem()        
        
        check = response.xpath('//*[@id="abs"]/h1/text()').extract()
        if len(check)==0:
            pass
        else:
            item['title'] = check[0]
            item['authors'] = response.xpath("//div[@class='authors']/a/text()").extract()
            
            temp = response.xpath('//*[@id="abs"]/div[2]/div[1]/h1/text()').extract()[0]
            if '>' in temp:
                c= temp.split(' > ')[0]
                item['category'] = c
                
            else:
                item['category'] = temp
                
            item['Id'] = response.xpath('//span[@class="arxivid"]/a/text()').extract()[0]
            item['link'] = "https://arxiv.org" + response.xpath('//*[@id="abs"]/div[1]/div[1]/ul/li[1]/a/@href').extract()[0] + ".pdf"
            item['abstract'] = response.xpath('//*[@id="abs"]/blockquote/text()').extract()
            item['date'] = response.xpath('//div[@class="submission-history"]/text()').extract()[-1].replace('\n','')
            item['primary_subject'] = response.xpath('//span[@class="primary-subject"]/text()').extract()[0]
            
            sl = response.xpath('//td[@class="tablecell subjects"]/text()').extract()
            if len(sl)==2:
                item['subjects'] = response.xpath('//td[@class="tablecell subjects"]/text()').extract()[1][2:]
            else:
                item['subjects'] = item['primary_subject']

            yield item


class Arxiv2Spider(scrapy.Spider):
    name = 'arxiv2'
    allowed_domains = ['arxiv.org']
    start_urls = ['http://arxiv.org/']

    
    months = {
        # "Jan":"01",
        # "Feb":"02",
        # "Mar":"03",
        # "Apr":"04",
        # "May":"05",
        # "Jun":"06",
        "July":"07"
        # "Aug":"08",
        # "Sep":"09",
        # "Oct":"10",
        # "Nov":"11",
        # "Dec":"12"
    }

    
    def start_requests(self):
        for k, v in list(self.months.items()):
            year = '19'
            
            for i in range(1,16000):
                s = str(i)
                s = s.zfill(5)
                url = "https://arxiv.org/abs/"+year+v+"."+s
                yield Request(url=url, callback = self.parse_item, meta={'month':v})

    

    def parse_item(self,response):
        
        m = response.meta['month']
        item = items.ArxivScrapeItem()        
        
        check = response.xpath('//*[@id="abs"]/h1/text()').extract()
        if len(check)==0:
            pass
        else:
            item['title'] = check[0]
            item['authors'] = response.xpath("//div[@class='authors']/a/text()").extract()
            
            temp = response.xpath('//*[@id="abs"]/div[2]/div[1]/h1/text()').extract()[0]
            if '>' in temp:
                c= temp.split(' > ')[0]
                item['category'] = c
                
            else:
                item['category'] = temp
                
            item['Id'] = response.xpath('//span[@class="arxivid"]/a/text()').extract()[0]
            item['link'] = "https://arxiv.org" + response.xpath('//*[@id="abs"]/div[1]/div[1]/ul/li[1]/a/@href').extract()[0] + ".pdf"
            item['abstract'] = response.xpath('//*[@id="abs"]/blockquote/text()').extract()
            item['date'] = response.xpath('//div[@class="submission-history"]/text()').extract()[-1].replace('\n','')
            item['primary_subject'] = response.xpath('//span[@class="primary-subject"]/text()').extract()[0]
            
            sl = response.xpath('//td[@class="tablecell subjects"]/text()').extract()
            if len(sl)==2:
                item['subjects'] = response.xpath('//td[@class="tablecell subjects"]/text()').extract()[1][2:]
            else:
                item['subjects'] = item['primary_subject']

            yield item



