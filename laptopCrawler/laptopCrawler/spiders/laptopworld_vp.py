import scrapy
from datetime import datetime

class LaptopWorld_VP(scrapy.Spider):
    name = "laptopworld_vp"
    allowed_domains = ["laptopworld.vn"]
    start_urls = ["https://laptopworld.vn/laptop-van-phong.html"]
    a = 1
    item_count = 0

    def parse(self, response):
        laps = response.css('div.product-list div.p-item div.p-container a.p-name')
        for lap in laps:
            yield scrapy.Request('https://laptopworld.vn' + lap.attrib['href'], callback=self.lap_parse)
        if self.a < 24:
            next_page_url = 'https://laptopworld.vn/laptop-van-phong.html?page=' + str(self.a + 1)
            yield response.follow(next_page_url, callback=self.parse)
            self.a += 1

    def lap_parse(self, response):
        details = response.css('div#tab1 div.content-text table tr')
        result = {
            f'{detail.css("td:first-child span::text").get() if detail.css("td:first-child span::text").get() != None else detail.css("td:first-child strong::text").get() }': detail.css("td:last-child span::text").get() for index, detail in enumerate(details)
        }
        result['url'] = response.url
        result['name'] = response.css('div.content-top-detail-left h1::text').get()
        result['gia goc'] = response.css('div.price-chinhhang del::text').get()
        result['gia khuyen mai'] = response.css('div.price-khuyemai div.content b::text').get()
        
        self.item_count += 1
        yield result

    def closed(self, reason):
        with open(f'../database/crawl_status_{self.name}.txt', 'w') as f:
            f.write(f"laptopworld.vn {datetime.now()} - {self.item_count} items scraped.\n")
