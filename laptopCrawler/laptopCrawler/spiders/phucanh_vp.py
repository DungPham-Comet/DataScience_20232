import scrapy


class PhucAnh(scrapy.Spider):
    name = "phucanh_vp"
    allowed_domains = ["www.phucanh.vn", "phucanh.vn"]
    start_urls = ["https://www.phucanh.vn/laptop.html"]
    a = 1
    def parse(self, response):
        laps = response.css('li.p-item-group div.p-container a.p-img')
        for lap in laps:
            yield scrapy.Request('https://phucanh.vn' + lap.attrib['href'], callback=self.lap_parse)

        if self.a < 27:
            next_page_url = 'https://www.phucanh.vn/laptop.html?page=' + str(self.a + 1)
            yield response.follow(next_page_url, callback=self.parse)
            self.a += 1
    def lap_parse(self, response):
        details = response.css('table.tb-product-spec tr')
        result={
            f'{detail.css("td.spec-key::text").get()}':detail.css("td.spec-value::text").get() for index,detail in enumerate(details)}
        result['url']=response.url
        result['name'] = response.css('body > div.container > h1::text').get()
        result['gia_niem_yet'] = response.css('div#product-info-price span.detail-product-old-price::text').get()
        result['gia_uu_dai'] = response.css('div#product-info-price span.detail-product-best-price::text').get()

        yield result