# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 14:09:21 2019

@author: gakel
"""

from scrapy import Spider
from scrapy import Request
from nasdaqheadlines.items import NasdaqheadlinesItem

class NewsSpider(Spider):
    name = 'news_spider'
    allowed_urls = ['https://www.nasdaq.com/news/market-headlines.aspx']
    start_urls = ['https://www.nasdaq.com/news/market-headlines.aspx']
    
    def parse(self, response):
        
        next_url = response.xpath('//*[@id="two_column_main_content_lb_NextPage"]/@href')
        
        for item in self.scrape(response):
            yield item
        
        if next_url:
            path = next_url.extract_first()
            nextpage = response.urljoin(path)
            print("Found url: {}".format(nextpage))
            yield Request(nextpage, callback=self.parse)
    
    
    def scrape(self, response):
        
        #//*[@id="newsContent"]/div/p[1]
        #//*[@id="newsContent"]/div/p[3]
         rows = response.xpath('//*[@id="newsContent"]/div/p')
         
         for row in rows:
             
             headline = row.xpath('./span[1]/a/text()').extract_first()
             
             
             #//*[@id="newsContent"]/div/p[4]/span[2]/text()[1]
             date = row.xpath('./span[2]/text()[1]').extract_first()
             
             if "Reuters" in date:
                 source = "Reuters"
                 date = date.split("-")[0]
             #//*[@id="newsContent"]/div/p[3]/span[2]/a[1]
             else:
                 source = row.xpath('./span[2]/a[1]/text()').extract_first()
             
             
             item = NasdaqheadlinesItem()
             item['headline'] = headline
             item['source'] = source
             item['date'] = date
             
             yield item
             

        
        
        
        
        
        
        