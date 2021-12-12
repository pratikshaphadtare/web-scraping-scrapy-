import scrapy


class NecklacesetbotSpider(scrapy.Spider):
    
    #scrapy crawl necklacesetbot

    #name of spider
    name = 'necklacesetbot'

    #list of allowed domains
    allowed_domains = ['www.houseofindya.com/zyra/necklace-sets/cat']

    #starting url
    start_urls = ['http://www.houseofindya.com/zyra/necklace-sets/cat/']

    #location of output file
    # custom_settings = {
    #     'FEED_FORMAT': 'json',
    #     'FEED_URI' : 'jsonfiles/necklaceset.json'
    # }

    def parse(self, response):
        #Extracting the content using css selectors
        description = response.css("li::attr(data-name)").extract()
        price = response.css("li::attr(data-price)").extract()
        catgItem = response.css(".catgItem")
        itemImage = catgItem.css("img::attr(data-original)").getall()

        #Give the extracted content row wise
        for item in zip(description,price,itemImage):
            #create a dictionary to store the scraped info
            scraped_info = {
                'description' : item[0],
                'price': item[1],
                'image_urls' : [item[2]]
            }

            #yield or give the scraped info to scrapy
            yield scraped_info
        

