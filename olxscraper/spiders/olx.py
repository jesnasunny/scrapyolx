import scrapy

class Olxneww(scrapy.Spider):

    name="olx"
    
    start_urls=["https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723"]
    

    # custom_setting={
    #     'FEEDS':{
    #         "olx2.json":{'format': 'json','overwrite':True}
    #     }


    def parse(self,response):
    
        for products in response.css("li._1DNjI"):

            
            yield{
                "property_name" :products.css("span._2poNJ::text").get(),
                "property_id":products.css("a::attr(href)").get()[63:-1],
                "breadcrumbs":products.xpath("//ol[@class='rui-2Pidb']/li/a/text()").getall()[0:3],
                "price" :products.css("span._2Ks63::text").get(),

                "image_url":products.css("img::attr(src)").get(),
                "description":products.css('span[data-aut-id="value_description"]::text').get(),
                "seller_name":products.css("div.eHFQs").getall(),


                "location":products.css("span._2VQu4::text").get(),
                

                
                "property_type":products.css("span.B6X7c").getall(),

                "bathrooms":products.css("span.YBbhy::text").get()[8],
                
                "bedrooms":products.css("span.YBbhy::text").get()[0]
                }
        load_more_button = response.css("button.btnLoadMore")
        if load_more_button:
            button_value = load_more_button.css("::text").get()
            self.log(f'Button Value: {button_value}')
            yield scrapy.Request(response.url, callback=self.parse_load_more, meta={'button_value': button_value})

    def parse_load_more(self, response):
        button_value = response.meta.get('button_value')
        self.log(f'Processing "Load More" with value: {button_value}')
            
