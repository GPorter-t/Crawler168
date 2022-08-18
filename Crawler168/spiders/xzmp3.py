import scrapy
from scrapy.linkextractors import LinkExtractor

from Crawler168.items import Mp3Item


class Xzmp3Spider(scrapy.Spider):
    name = 'xzmp3'
    allowed_domains = ['wwww.zxmp3.com']
    start_urls = ['https://www.xzmp3.com/']

    def parse(self, response):
        for link in LinkExtractor(allow=r"/xiazai/").extract_links(response):
            yield scrapy.Request(link.url, callback=self.parse_song,dont_filter=True)

    def parse_song(self, response):
        for link in LinkExtractor(allow=r"/mp3/").extract_links(response):
            yield scrapy.Request(link.url, callback=self.parse_filelink, dont_filter=True)

    def parse_filelink(self, response):
        url = response.xpath("//a[@class='height_middle bt']/@href").extract_first()
        if url:
            item = Mp3Item()
            item["url"] = url
            yield item
