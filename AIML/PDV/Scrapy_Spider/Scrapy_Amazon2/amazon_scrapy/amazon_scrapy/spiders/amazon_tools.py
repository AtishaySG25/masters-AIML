# amazon_scraper/spiders/amazon_spider.py
import scrapy
#from amazon_scraper.items import AmazonScrapyItem
#from amazon_scrapy.amazon_scrapy.items import AmazonScrapyItem
from ..items import AmazonScrapyItem
from urllib.parse import urlparse, parse_qs

class AmazonSpider(scrapy.Spider):
    name = 'amazon_multiple_pages_spider'

    # Define the base URL for the first page
    base_url = 'https://www.amazon.in/s?k=manchester+united+jersey&page=1'
    
    def start_requests(self):
        # Start with the first page to extract the qid parameter
        yield scrapy.Request(self.base_url, callback=self.parse_first_page)

    def parse_first_page(self, response):
        # Extract the qid parameter from the response URL
        parsed_url = urlparse(response.url)
        qid = parse_qs(parsed_url.query).get('qid', [''])[0]

        # Continue to the next page with the qid parameter
        next_page = f'https://www.amazon.in/s?k=manchester+united+jersey&page=2&qid={qid}'
        yield response.follow(next_page, self.parse)

    def parse(self, response):
        items = AmazonScrapyItem()

        product_blocks = response.css('.s-result-item')
        for product_block in product_blocks:
            name = product_block.css('.a-size-base-plus.a-color-base.a-text-normal::text').get()
            price = product_block.css('.a-price .a-offscreen::text').get()
            brand = product_block.css('.a-size-base-plus.a-color-base::text').get()

            items['name'] = name.strip() if name else None
            items['price'] = price.strip() if price else None
            items['brand'] = brand.strip() if brand else None

            yield items

        # Extract the qid parameter from the current page's URL
        parsed_url = urlparse(response.url)
        qid = parse_qs(parsed_url.query).get('qid', [''])[0]+1  

        # Pagination: Follow the next page link with the qid parameter
        next_page_number = int(response.url.split('&page=')[1]) + 1
        next_page = f'https://www.amazon.in/s?k=manchester+united+jersey&page={next_page_number}&qid={qid}'
        yield response.follow(next_page, self.parse)