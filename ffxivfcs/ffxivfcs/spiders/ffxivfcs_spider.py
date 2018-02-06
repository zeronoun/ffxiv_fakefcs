import scrapy
from scrapy.contrib.spiders import XMLFeedSpider

class FCsSpider(scrapy.Spider):
	name = 'fcs'

	start_urls = ['https://na.finalfantasyxiv.com/lodestone/freecompany/?q=&worldname=_dc_Elemental&character_count=&activetime=&join=&house=&order=5',
				  'https://na.finalfantasyxiv.com/lodestone/freecompany/?q=&worldname=_dc_Gaia&character_count=&activetime=&join=&house=&order=5',
				  'https://na.finalfantasyxiv.com/lodestone/freecompany/?q=&worldname=_dc_Mana&character_count=&activetime=&join=&house=&order=5',
				  'https://na.finalfantasyxiv.com/lodestone/freecompany/?q=&worldname=_dc_Aether&character_count=&activetime=&join=&house=&order=5',
				  'https://na.finalfantasyxiv.com/lodestone/freecompany/?q=&worldname=_dc_Primal&character_count=&activetime=&join=&house=&order=5',
				  'https://na.finalfantasyxiv.com/lodestone/freecompany/?q=&worldname=_dc_Chaos&character_count=&activetime=&join=&house=&order=5']
	
	def parse(self, response):
		for i in response.xpath(".//a[@class='entry__block']"):

			name = i.xpath(".//div[@class='entry__freecompany__inner']/div[@class='entry__freecompany__box']/p[@class='entry__name']/text()").extract_first()
			date = i.xpath(".//ul[@class='entry__freecompany__fc-data clearix']/li[@class='entry__freecompany__fc-day']/script/text()").extract_first()
			estate = i.xpath(".//li[@class='entry__freecompany__fc-housing']/text()").extract_first()
			world = i.xpath(".//div[@class='entry__freecompany__inner']/div[@class='entry__freecompany__box']/p[@class='entry__world'][2]/text()").extract_first()

			yield {
				'name': name,
				'date': date,
				'has_estate': estate,
				'world': world
			}

		next_page = response.xpath("//ul[@class='btn__pager'][2]/li[4]/a[@class='icon-list__pager btn__pager__next js__tooltip']/@href").extract_first()

		if next_page is not None:
			next_page = response.urljoin(next_page)
			yield scrapy.Request(next_page, callback=self.parse)




# //a[@class='entry__block']/ul[@class='entry__freecompany__fc-data clearix']/li[@class='entry__freecompany__fc-day']/span[@id='datetime-0.120923217366787']/text()
