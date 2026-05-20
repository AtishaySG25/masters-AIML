import scrapy

class Recipes(scrapy.Spider):
    name = 'recipe'
    start_urls = ('https://www.vegrecipesofindia.com/',
                  'https://www.vegrecipesofindia.com/recipes/')
    
    def parse(self, response):
        category = response.xpath('//p[contains(@class, "entry-category")]//text()').extract()
        names = response.xpath('//h3/a/text()').extract()
        links = response.xpath('//div[contains(@class, "block-quick-links")]/a/@href').extract()
        types = response.xpath('//div[contains(@class, "block-quick-links")]/a/span/text()').extract()
        yield{'Recipe Category': category,
              'Recipe Names': names,
              'Recipe Links': links,
              'Recipe Types': types}