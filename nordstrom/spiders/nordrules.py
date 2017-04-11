# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class NordSpider(CrawlSpider):
    name = "nordrules"
    allowed_domains = ["shop.nordstrom.com"]
    start_urls = []
    
    for page in range(1,64):
        count = +12
        url = "http://shop.nordstrom.com/sr?origin=keywordsearch&keyword=suitcase&page=" + str(page) + "&top=" + str(count)
        start_urls.append(url)
    
    rules = (Rule(LinkExtractor(allow=('yoga',)), callback='parse', follow=True),)
    
    def parse(self, response):
        page_url = response.request.url
        articles = response.xpath('//p[@class="product-title"]')
        
    	for article in articles:
    	    title = article.xpath('a/span/text()').extract_first()
    	    relative_article_url = article.xpath('a/@href').extract_first()
    	    absolute_article_url  = response.urljoin(relative_article_url)
    	    
    	    yield{
    	        'Article URL': absolute_article_url,
    	        'Page URL':page_url,
                'Title':title
                }
