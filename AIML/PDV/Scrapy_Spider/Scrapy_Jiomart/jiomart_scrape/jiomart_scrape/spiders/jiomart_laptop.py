import scrapy
    
class JioMartSpider(scrapy.Spider):
    name = 'jiomart'
    start_urls = ['https://www.jiomart.com/search/laptop/in/prod_mart_master_vertical?prod_mart_master_vertical%5Bpage%5D=4&prod_mart_master_vertical%5BhierarchicalMenu%5D%5Bcategory_tree.level0%5D%5B0%5D=Categoryprod_mart_groceries_products_popularity%5Bpage%5D=3']
    page_number = 1
    max_pages = 10

    def parse(self, response):
        products = response.css('#algolia_hits .c-card')

        for product in products:
            name = product.css('.jm-fc-primary-grey-80::text').get().strip()
            price = product.css('.jm-mb-xxs::text').get().strip()
            original_price = product.css('.line-through::text').get().strip()
            discount = product.css('.jm-mb-xxs .jm-badge::text').get().strip()

            yield {
                'Name': name,
                'Price': price,
                'Original Price': original_price,
                'Discount': discount,
            }

        # Follow pagination links
        next_page = response.css('a[rel="next"]::attr(href)').get()
        if self.page_number <= self.max_pages and next_page:
            self.page_number += 1
            yield scrapy.Request(url=next_page, callback=self.parse)
