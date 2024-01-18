import scrapy

class Olxneww(scrapy.Spider):
    name="olx"
    start_urls=["https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723"]
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}

yield scrapy.Request(url, headers=headers, callback=self.parse)


    def parse(self,response):
        for products in response.css("li._1DNjI"):

            
            yield{
                "property_name" :products.css("span._2poNJ::text").get(),
                "price" :products.css("span._2Ks63::text").get(),
                "image_url":products.css("img::attr(src)").get(),
                "location":products.css("span._2VQu4::text").get(),
                "breadcrumbs":products.xpath("//ol[@class='rui-2Pidb']/li/a/text()").getall()[0:3],
                "property_id":products.css("a::attr(href)").get()[63:-1],


                
                
                "description":products.css('div[data-aut-id="itemDescriptionContent"].p::text').getall(),
                /response.css(".itemDescriptionContent p::text

                "property_id":products.css("a::attr(href)").get()[63:-1],
                products.css("div strong::text").getall(),
                products.css("_1-oS0.strong::text").getall()
                products.xpath("//div[@class='_1-oS0']/strong/following-sibling::text()").extract()
                "seller_name":products.css("div.eHFQs").getall(),
                "property_type":products.css("span.B6X7c").getall(),
                "bathrooms":products.css('span.B6X7c[data-aut-id="value_bathrooms"]::text').getall(),
                "bedrooms":products.css('span.B6X7c[data-aut-id="value_rooms"]::text').getall()



                # "item_deatls":products.css("span._2VQu4::text").get()
                }
            
                
        loadmorebutton=products.css("button.btnLoadMore")
        if loadmorebutton:
            button_value=loadmorebutton.css("::text").get()
            yield scrapy.Request(response.url,callback=self.parse_load_more,meta={'button_value':button_value})
    def parse_load_more(self,response):
        pass

