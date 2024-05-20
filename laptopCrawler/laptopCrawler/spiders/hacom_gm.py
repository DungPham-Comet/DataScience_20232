import scrapy
from datetime import datetime

class HaCom(scrapy.Spider):
    name = "hacom_gm"
    allowed_domains = ["hacom.vn"]
    start_urls = ["https://hacom.vn/laptop-gaming-do-hoa/"]
    a = 1
    item_count = 0

    def parse(self, response):
        laps = response.css('div.p-info')
        for lap in laps:
            self.item_count += 1
            yield scrapy.Request('https://hacom.vn' + lap.css('h3.p-name a').attrib['href'], callback=self.lap_parse)
        if self.a < 8:
            next_page_url = 'https://hacom.vn/laptop-gaming-do-hoa/' + str(self.a + 1) + '/'
            yield response.follow(next_page_url, callback=self.parse)
            self.a += 1
        else:
            # Log the item count
            with open(f'../database/crawl_status_{self.name}.txt', 'w') as f:
                f.write(f"hacom.vn {datetime.now()} - {self.item_count} items scraped.\n")

    def lap_parse(self, response):
        properties = response.css('div#popup-tskt  div.bang-tskt table tr')

        result = {
            f'{Property.css("td:first-child p::text").get()}': Property.css("td:last-child p::text").get() for
            index, Property in enumerate(properties[1:])}
        result['name'] = response.css('div.product_detail-title h1::text').get()
        result['url'] = response.url
        result['giá gốc'] = response.css('div#product-info-price span.gia-km-cu::text').get()
        result['giá khuyến mại'] = response.css('div#product-info-price strong.giakm::text').get().replace('\n', '').replace(' ', '')

        yield result
