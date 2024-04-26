import scrapy


class LaptopWorld_Gaming(scrapy.Spider):
    name = "laptopworld_gaming"
    allowed_domains = ["laptopworld.vn"]
    start_urls = ["https://laptopworld.vn/laptop-games-do-hoa.html"]
    a = 1
    def parse(self, response):
        laps = response.css('div.product-list div.p-item div.p-container a.p-name')
        for lap in laps:
            yield scrapy.Request('https://laptopworld.vn' + lap.attrib['href'], callback=self.lap_parse)
            # yield {
            #     'url': lap.attrib['href']
            # }
        if self.a < 13:
            next_page_url = 'https://laptopworld.vn/laptop-games-do-hoa.html?page=' + str(self.a + 1)
            yield response.follow(next_page_url, callback=self.parse)
            self.a += 1
    def lap_parse(self, response):
        details = response.css('div#tab1 div.content-text table tr')
        result={
            f'{detail.css("td:first-child span::text").get() if detail.css("td:first-child span::text").get()!=None else detail.css("td:first-child strong::text").get() }':detail.css("td:last-child span::text").get() for index,detail in enumerate(details)}
        result['url']=response.url
        result['name'] = response.css('div.content-top-detail-left h1::text').get()
        result['gia_chinh_hang'] = response.css('div.price-chinhhang del::text').get()
        result['gia_khuyen_mai'] = response.css('div.price-khuyemai div.content  b::text').get()

        yield result
