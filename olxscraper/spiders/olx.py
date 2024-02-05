import scrapy
import re
from scrapy_selenium import SeleniumRequest

class OlxScraper(scrapy.Spider):
    name = 'olx'
    allowed_domains = ["olx.in"]
    start_urls = ["https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723"]
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'handle_httpstatus_list': [404],  # Handle 404 status code
    }

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(url=url, callback=self.parse, wait_time=10)

    def parse(self, response):
        # Extract initial page data
        yield from self.extract_product_data(response)

        # Extract additional pages using Selenium
        page_number = 2
        while page_number <=300:
            next_page_url = f"https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723?page={page_number}"
            yield SeleniumRequest(url=next_page_url, callback=self.parse_next_page, wait_time=10)
            page_number += 1

    def extract_product_data(self, response):
        for product in response.css("li._1DNjI"):
            product_name = product.css("span._2poNJ::text").get()
            property_id_href = response.css('link[rel="canonical"]::attr(href)').get()
            property_id = re.search(r'\d+', property_id_href).group() if property_id_href else None    

            breadcrumbs = product.xpath("//ol[@class='rui-2Pidb']/li/a/text()").getall()
            price = product.css("span._2Ks63::text").get()
            image_url = product.css("img::attr(src)").get()
            location = product.css("span._2VQu4::text").get()
            bathroom = product.css("span.YBbhy::text").get()
            bedrooms = product.css("span.YBbhy::text").get()

            if bathroom:
                bathroom = bathroom[8]
            if bedrooms:
                bedrooms = bedrooms[0]

            # Extracting additional details from the product page
            product_link = product.css('li._1DNjI a::attr(href)').extract()
            for link in product_link:
                yield SeleniumRequest(url=response.urljoin(link), callback=self.parse_product_details,
                                     meta={'product_name': product_name, 'property_id': property_id,
                                           'breadcrumbs': breadcrumbs, 'price': price, 'image_url': image_url,
                                           'location': location, 'bathroom': bathroom, 'bedrooms': bedrooms})

    def parse_product_details(self, response):
        product_name = response.meta['product_name']
        property_id = response.meta['property_id']
        breadcrumbs = response.meta['breadcrumbs']
        price = response.meta['price']
        image_url = response.meta['image_url']
        location = response.meta['location']
        bathrooms = response.meta['bathroom']
        bedrooms = response.meta['bedrooms']

        # Extracting additional details
        type_info = response.css('span[data-aut-id="value_type"]::text').get()      
        description = response.css('div[data-aut-id="itemDescriptionContent"] p::text').getall()
        description_text = '\n'.join(description)
        title = response.css('div._3Yuv9.kI9QF div.eHFQs::text').get()
        yield {
            'property_name': product_name,
            'property_id': property_id,
            'breadcrumbs': breadcrumbs,
            'price': price,
            'image_url': image_url,
            'description_text': description_text,
            'location': location,
            'seller_name': title.strip() if title else None,
            'property_type': type_info.strip() if type_info else None,
            'bathrooms': bathrooms,
            'bedrooms': bedrooms,
            
            

        }

    def parse_next_page(self, response):
        # Extract additional page data using Selenium
        yield from self.extract_product_data(response)

        # Check if the response URL is the same as the start URL
        if response.url == self.start_urls[0]:
            self.logger.info('Reached the end of pages. Stopping further crawling.')
            return

        # Check if the next page button is disabled
        next_page_button = response.css('button.pageNext')
        if not next_page_button:
            self.logger.info('No more pages to crawl')
            return

        # If the button is not disabled, extract the next page URL and continue crawling
        next_page_button_link = response.css('button.pageNext::attr(href)').get()
        if next_page_button_link:
            next_page_url = response.urljoin(next_page_button_link)
            yield SeleniumRequest(url=next_page_url, callback=self.parse_next_page, wait_time=10)
        else:
            self.logger.info('No more pages to crawl')
