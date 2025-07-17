import scrapy

class TopdiodnewparsSpider(scrapy.Spider):
    name = "topdiodnewpars"
    allowed_domains = ["topdiod.ru"]
    start_urls = ["https://topdiod.ru/catalog/svetodiodnye_lenty/ "]

    def parse(self, response):
        svetodiodnye_lenty = response.css('div.product.bx_catalog_item')

        for lenta in svetodiodnye_lenty:
            yield {
                'name': lenta.css('.bx_catalog_item_title a::text').get(default='').strip(),
                'price': lenta.css('.bx_price::text').get(default='').strip(),
                'url': response.urljoin(lenta.css('.bx_catalog_item_title a::attr(href)').get(default='')),
                'power': lenta.xpath('.//div[@title="Мощность"]/text()[last()]').get(default='').strip(),
                'light_output': lenta.xpath('.//div[@title="Световой поток"]/text()[last()]').get(default='').strip(),
                'protection_class': lenta.xpath('.//div[@title="Класс защиты"]/text()[last()]').get(default='').strip(),
                'color_temp': lenta.xpath('.//div[@title="Цветовая температура"]/text()[last()]').get(default='').strip()
            }