import scrapy
from Noticias.items import NoticiasItem
from scrapy.spider import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
#rom scrapy.contrib.spiders import CrawlSpider, Rule

class inglesSpider(CrawlSpider):
    name = 'ingles'

    allowed_domains = ['https://www.nbcnews.com/']
    start_urls = ['https://www.nbcnews.com/']
                  #'https://www.nbcnews.com/news/us-news/california-communities-band-together-bring-thanksgiving-wildfire-survivors-n939306']

    rules = {
		# Para cada item
        Rule(LinkExtractor(allow =(), restrict_xpaths = ('//div[@class="article___1MtWi"]/article/div/a/@href')),
                                                callback = 'parse_item', follow = False)
        }


    def parse_item(self, response):
        item = NoticiasItem()
        item['title'] = response.xpath('normalize-space(//h1/text())').extract()
        item['body'] = response.xpath('normalize-space(//p/text())').extract()
        yield item
