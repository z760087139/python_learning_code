import  scrapy

class QuotesSpider(scrapy.Spider)
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
            ]
        for url in ulrs:
            yeild scrapy.Request(url=url,callback=self.parse)

    def parse(self,response):
        page = response.url.split("/")[-2]