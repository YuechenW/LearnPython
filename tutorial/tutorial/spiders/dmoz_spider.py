import scrapy

from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ['dmoztools.net']
    start_urls = [
        'http://www.dmoztools.net/Computers/Programming/Python/Books',
        'http://www.dmoztools.net/Computers/Programming/Python/Rescources'
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        sel = scrapy.selector.Selector(response)
        sites = sel.xpath('//url[@class="directory-url"]/li')
        items = []
        for site in sites:
            item = DmozItem()
            item['title'] = site.xpath('a/text()').extract()
            item['link'] = site.xpath('a/@href').erctract()
            item['desc'] = site.xpath('text()').erctract()
            items.append(item)

        return items