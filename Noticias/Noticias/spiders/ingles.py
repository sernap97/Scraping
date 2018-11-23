import scrapy
from Noticias.items import NoticiasItem
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
#rom scrapy.contrib.spiders import CrawlSpider, Rule

class inglesSpider(CrawlSpider):
    name = 'ingles'

    allowed_domains = ['www.nbcnews.com']
    #start_urls = ['https://www.nbcnews.com/news/us-news/california-communities-band-together-bring-thanksgiving-wildfire-survivors-n939306'] 
    start_urls = ['https://www.nbcnews.com'] 

    """rules = {
		# Para cada item
        Rule(LinkExtractor(allow =(), restrict_xpaths = ('//div[@class="article___1MtWi"]/article/div/a/@href')),
                                                callback = 'parse_item', follow = False)
        }
"""

    def parse(self, response):
        links = []
        links = response.xpath('//div[@class="article___1MtWi"]/article/div/a/@href').extract()
        for i in range(len(links)):
            if (links[i][0:5] != "https"):
                links[i] = "https://www.nbcnews.com" + links[i]
        
        for link in links:
            yield scrapy.Request(url=link, callback=self.getItem)    
        
    def getItem(self, response):
        item = NoticiasItem()
        item['title'] = response.xpath('normalize-space(//h1/text())').extract()
        item['body'] = response.xpath('normalize-space(//p/text())').extract()
        yield item
        
