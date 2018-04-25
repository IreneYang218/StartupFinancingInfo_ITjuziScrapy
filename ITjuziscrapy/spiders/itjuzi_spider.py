# -*- coding: utf-8 -*-
"""
Created on Wed Nov 01 21:28:40 2017

@author: Ailsa
"""
import scrapy
from ITjuziscrapy.items import ItjuziscrapyItem
from scrapy.conf import settings


class ItjuziscrapySpider(scrapy.Spider):
    name = "itjuzi"
    allowed_domains = ["itjuzi.com"]
    start_urls = [
            "https://www.itjuzi.com/investevents?page=89"
            ]
            
    cookie = settings['COOKIE']
    headers = {
    'Host': "www.itjuzi.com",
    'Accept-Language': "zh-CN,zh;q=0.8",
    'Accept-Encoding': "gzip, deflate, br",
    'Content-Type': "application/x-www-form-urlencoded",
    'Connection': "keep-alive",
    'Referer': "https://www.itjuzi.com/" 
    }
    

    def get_next_url(self, oldUrl):
        l = oldUrl.split('=')
        oldID = int(l[1])
        print oldID
        newID = oldID - 1
        if newID == 80:
            return
        newUrl = l[0] + "=" + str(newID)
        print newUrl
        return str(newUrl)
    
    def start_requests(self):
        yield  scrapy.Request(url=self.start_urls[0], 
                              headers = self.headers, 
                              cookies = self.cookie, 
                              callback = self.parse_event,
                              dont_filter=True)      
                             
    def parse_event(self, response):
        #self.logger.info('Parse function called on %s', response.url)
        #self.logger.debug('THIS IS A WARNING', level=log.DEBUG)
        for sel in response.xpath('//ul[@class="list-main-eventset"]/li'):
            item = ItjuziscrapyItem()
            item['event_time'] = sel.xpath('i[@class="cell date"]/span/text()').extract()
            item['link'] = sel.xpath('i[@class="cell pic"]/a/@href').extract()[0]
            item['co_name'] = sel.xpath('.//p[@class="title"]/a/span/text()').extract()
            item['industry'] = sel.xpath('.//p/span[@class="tags t-small c-gray-aset"]/a/text()').extract()
            item['city'] = sel.xpath('.//p/span[@class="loca c-gray-aset t-small"]/a/text()').extract()
            item['event_round'] = sel.xpath('i[@class="cell round"]/a/span[@class="tag gray"]/text()').extract()
            item['money'] = sel.xpath('i[@class="cell money"]/text()').extract()
            item['investors'] = sel.xpath('normalize-space(i[@class="cell name"]/div[@class="investorset"])').extract()
            print item
            yield scrapy.Request(sel.xpath('i[@class="cell pic"]/a/@href').extract()[0], 
                                 headers = self.headers, 
                                 cookies = self.cookie,
                                 meta ={'key': item},
                                 callback = self.parse_company,
                                 dont_filter=True)
        
        
        print response.url
        next_url = self.get_next_url(response.url)
        if next_url != None:
            yield scrapy.Request(next_url, 
                                 headers = self.headers, 
                                 cookies = self.cookie,
                                 callback= self.parse_event,
                                 dont_filter=True
                                 )
        return 
    
    def parse_company(self, response):
        #self.logger.info('Parse function called on %s', response.url)
        company = response
        item = response.meta['key']
        item['tags'] = company.xpath('//div[@class="tagset dbi c-gray-aset"]//span[@class="tag"]/text()').extract()
        item['co_intro'] = company.xpath('//h2[@class="seo-slogan"]/text()').extract()
        item['founder_name'] = company.xpath('//h4[@class="person-name"]//span[@class="c"]/text()').extract()
        item['founder_intro'] = company.xpath('//p[contains(@class, "person-des")]/text()').extract()
        item['found_time'] = company.xpath('//h2[@class = "seo-second-title"]/text()').extract()[1]
        item['co_size'] = company.xpath('//h2[@class = "seo-second-title"]/text()').extract()[2]
        item['trademark'] = company.xpath('//div[(@class = "brand-info")]//p[2]/span/text()').extract()
        item['found_capital'] = company.xpath('//div[@class="essential"]//tr[1]/td[1]/span[@class="tab_main"]/i/text()').extract()
        yield item
  
