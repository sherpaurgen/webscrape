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
    	print name
    	return 

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

crawler = AppCrawler('https://play.google.com/store/apps/details?id=com.hecorat.packagedisabler',0)
crawler.crawl()
for app in crawler.apps:
	print app

