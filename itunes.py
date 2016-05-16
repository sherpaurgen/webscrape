from lxml import html
import requests

class AppCrawler:
    
    def __init__(self,starting_url,depth):
        self.starting_url=starting_url
        self.depth=depth
        self.current_depth=0
        self.depth_links=[]
        self.apps=[]

    def crawl(self):
        app=self.get_app_from_link(self.starting_url)
        self.apps.append(app)
        self.depth_links.append(app.links)

        while self.current_depth < self.depth:      #0 < 0
            current_links=[]
            for link in self.depth_links[self.current_depth]:
                current_app = self.get_app_from_link(link)
                current_links.extend(current_app.links)
                self.apps.append(current_app)
            self.current_depth += 1
            self.depth_links.append(current_links)

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
        price=str(temp_price[0].lstrip('$'))
        if price=="Install":
            price="0"
        templinks = tree.xpath("//a[@class='title']/@href")
        
        links=[]
        length=len(templinks)
        domain="https://play.google.com"
        for i in templinks:
            i="https://play.google.com"+i
            links.append(i)
#        print links            
        #print len(testlinks)
        #links = [h for h in tree.xpath("//a[@class='title']/@href")]
        #print links
        #return name,developer[1],price,links
        app = App(name,developer[1],price,links)
        return app

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

crawler = AppCrawler('https://play.google.com/store/apps/details?id=com.mojang.minecraftpe',1)
crawler.crawl()
#print type(crawler.apps)
for app in crawler.apps:
    print app
