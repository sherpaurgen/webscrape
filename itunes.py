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
        # the tree.xpath(...) gives an array 
    	name = tree.xpath('//div[@class="id-app-title"]/text()')[0]  

    	#developer=tree.xpath('//a[@class="dev-link"]//*/div/@href')
    	temp_addr=tree.xpath('//a[contains(@href,"mailto") and @class="dev-link"]/@href')[0]
        developer=temp_addr.split(':')
        
        price=tree.xpath('//button[@class="price buy id-track-click id-track-impression"]/span[2]/text()')
        temp_price=price[0].split()
        price=temp_price[0].lstrip('$')
        if price=="Install":
            price=0
        testlinks = tree.xpath("//a[@class='title']/@href")
        #print len(testlinks)
        #links = [h for h in tree.xpath("//a[@class='title']/@href")]
        print testlinks
        #return name,developer[1],price,links
    	

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

crawler = AppCrawler('https://play.google.com/store/apps/details?id=com.mojang.minecraftpe',0)
crawler.crawl()
for app in crawler.apps:
	print app
    
