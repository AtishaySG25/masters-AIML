import scrapy

class AmazonBatSpider(scrapy.Spider):
    name = 'amazon_bat'
    start_urls = ['https://www.amazon.in/s?k=bat&crid=1B5LH49P1VN8M&sprefix=bat%2Caps%2C255&ref=nb_sb_noss_1']
    page_count = 0  # Initialize a page count

    def parse(self, response):
        # Extract data from the current page
        product_listings = response.xpath('//div[@data-asin]')

        for product in product_listings:
            item = {
                'name': product.xpath('.//span[@class="a-size-base-plus a-color-base a-text-normal"]/text()').get(),
                'price': product.xpath('.//span[@class="a-price-whole"]/text()').get(),
                'rating': product.xpath('.//span[@class="a-icon-alt"]/text()').get(),
            }
            yield item

        # Increment the page count
        self.page_count += 1

        # Check if we have scraped 5 pages, and if not, continue to the next page
        if self.page_count < 5:
            next_page = response.css('a.s-pagination-next::attr(href)').get()
            if next_page:
                next_page_url = response.urljoin(next_page)
                yield scrapy.Request(next_page_url, callback=self.parse)
