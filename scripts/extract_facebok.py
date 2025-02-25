import scrapy
from scrapy.crawler import CrawlerProcess

class FacebookSpider(scrapy.Spider):
    name = 'facebook'
    start_urls = ['https://www.facebook.com/groups/quito.local']  # Ejemplo de grupo

    def parse(self, response):
        comments = response.css('div.userContentWrapper p::text').getall()
        for comment in comments:
            yield {'comment': comment}

# Ejecutar el spider
process = CrawlerProcess(settings={'FEEDS': {'facebook_data.csv': {'format': 'csv'}}})
process.crawl(FacebookSpider)
process.start()