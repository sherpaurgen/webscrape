class AppCrawler:
    
    def __init__(self,starting_url,depth):
        self.starting_url=starting_url
        self.depth=depth
        self.apps=[]

    def crawl(self):
    	return 

    def get_app_from_link(self,link):
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

crawler = AppCrawler()
