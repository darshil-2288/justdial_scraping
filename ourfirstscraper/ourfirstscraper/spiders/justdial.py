import scrapy

class justdial_scraping(scrapy.Spider):
    name="justdial_scraping"
    allowed_domains=['https://www.justdial.com/']
    start_urls=['https://www.justdial.com/']

    def parse(self,response):
        nameofindustry=response.css('a::attr(title)').extract()
       
        for item in zip(nameofindustry):
            scraped_info={
                'nameofindustry':item[0]
                }
            yield scraped_info
