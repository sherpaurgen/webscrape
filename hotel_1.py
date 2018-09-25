from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re
from time import sleep
import numpy as np
delays=[13,8,9,10,12]

fileName="hotelName.csv"
url="https://www.tripadvisor.com/Hotels-g293890-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Central_Region-Hotels.html"
baseurl="https://www.tripadvisor.com"
options=Options()
#options.headless=True
browser=webdriver.Chrome(chrome_options=options,executable_path='/opt/binary/chromedriver')
urlnext=""

def scrape(urlnext):
    print("Scraping the url: "+urlnext)
    delay = np.random.choice(delays)
    browser.implicitly_wait(delay)
    browser.get(urlnext)
    html_doc = browser.page_source
    soup = BeautifulSoup(html_doc, 'lxml')
    containers=soup.find_all("div",{"data-impkey":re.compile(r'\w+')})
    for container in containers:
        hotelNameUnparsed=container.findAll("a", {"data-clicksource": "HotelName"})
        hotelNameParsed=hotelNameUnparsed[0].text
        hotelDetailUrl=hotelNameUnparsed[0]["href"]
        # for rating
        try:
            ratingUnparsed=container.findAll("span",{"class":"ui_bubble_rating"})
            ratingParsed=float(ratingUnparsed[0].attrs['alt'].split(' ')[0])
            ratingParsed=str(ratingParsed)

        except:
            ratingParsed="NA"
        #for wifi and parking
        extras=container.findAll("span", {"class": "text"})
        #for free wifi
        try:
            wifi=extras[0].text
            if wifi=="Free Wifi":
                pass
            else:
                wifi="NA"
        except:
            wifi="NA"
            pass
        #for free parking
        try:
            parking=extras[1].text
            if parking=="Free Parking":
                pass
            else:
                parking="NA"
        except:
            parking="NA"
            pass
        with open(fileName,"a") as file:
            file.write(hotelNameParsed+","+ratingParsed+","+wifi+","+parking)
            file.write("\n")
        with open("urlfile.txt","a") as urlFileHandler:
            urlFileHandler.write(hotelDetailUrl)
            urlFileHandler.write("\n")

pg = 0
for i in range(0,33):
    if pg == 0:
        print("First if statement")
        urlnext = "https://www.tripadvisor.com/Hotels-g293890-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Central_Region-Hotels.html"
        pg = pg + 30
        scrape(urlnext)

    else:
        print("Jumping next else")
        urlnext = 'https://www.tripadvisor.com/Hotels-g293890-oa' + str(pg) + '-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Central_Region-Hotels.html'
        pg = pg + 30
        scrape(urlnext)
