from lxml import html
import requests

class AppCrawler:
    
    def __init__(self,starting_url,depth):
        self.starting_url=starting_url
        self.depth=depth
        self.apps=[]

    def crawl(self):
    	self.get_app_from_link(self.starting_url)
    	return 

    def get_app_from_link(self,link):
    	start_page=requests.get(link)
    	#print start_page.text
    	tree = html.fromstring(start_page.text)
    	name = tree.xpath('//div[@class="id-app-title"]/text()')[0]
    	#developer=tree.xpath('//a[@class="dev-link"]//*/div/@href')
    	temp_addr=tree.xpath('//a[contains(@href,"mailto") and @class="dev-link"]/@href')[0]
        developer=temp_addr.split(':')
        
        price=tree.xpath('//button[@class="price buy id-track-click id-track-impression"]/span[2]/text()')
        temp_price=price[0].split()
        price=temp_price[0].lstrip('$')
        if price=="Install":
            price=0

        #links=tree.xpath('//div[@class="cards id-card-list"]//*/div[@class="card no-rationale square-cover apps medium-minus"]//*/div[@class="card-content id-track-click id-track-impression"]//*/a[@class="card-click-target"]/@href')     
        links=tree.xpath('//*[@id="body-content"]/div[2]/div/div[1]/div[1]/div/div[1]/div/div[2]')
        #print name,developer[1],price
        print links
        
        return name,developer[1],price
    	

class App:
	def __init__(self, name,developer,price,links):
		self.name=name
		self.developer=developer
		self.price = price
		self.links=links

	def __str__(self):
		return("Name"+self.name.encode('UTF-8')+
		"\nDeveloper: " + self.developer.encode('UTF-8')+
		"\nPrice: " + self.price.encode('UTF-8')+"\n")

crawler = AppCrawler('https://play.google.com/store/apps/details?id=com.picsart.studio',0)
crawler.crawl()
for app in crawler.apps:
	print app

