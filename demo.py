import urllib2
from bs4 import BeautifulSoup

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
    	start_page=urllib2.urlopen(link)
        soup = BeautifulSoup(start_page,"html.parser")
        print soup.title.text
        # for links in soup.findAll('a'):
        #     print links.get('href')+" this is href"
        #     print links.text
        # print soup.find('div',{"class":"id-app-title"}).text
        # for links in soup.find_all('a'):
        #     print links.get("href"),links.text
        urldata=soup.find_all('a',{"class":"title","aria-hidden":"true"})
        for hreflinks in urldata:
            print hreflinks.get("href")

        
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

crawler = AppCrawler('https://play.google.com/store/apps/details?id=com.picsart.studio',0)
crawler.crawl()
for app in crawler.apps:
	print app

