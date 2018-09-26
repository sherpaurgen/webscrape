from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re
from time import sleep
import numpy as np
delays=[13,8,9,10,12]
baseurl="https://www.tripadvisor.com"
fileName="userReview.txt"
options=Options()
#options.headless=True
browser=webdriver.Chrome(chrome_options=options,executable_path='/home/user1/hotelscrape/code/driver/chromedriver')
delay = np.random.choice(delays)
browser.implicitly_wait(delay)
with open ("urlfile.txt","r") as fh:
    for line in fh.readlines():
        urlnext=baseurl+line.split('\n')[0]
        print("Scanning: "+urlnext)
        browser.get(urlnext)
        html_doc = browser.page_source
        soup = BeautifulSoup(html_doc, 'lxml')
        hotelName=soup.find("h1",{"id":"HEADING"}).text
        try:
            streetAddress="Pokhara"
            print("Street Address: "+streetAddress)
        except:
            streetAddress="NA"
        containers=soup.find_all("div",{"class":"review-container","data-reviewid":re.compile(r'\w+')})
        for container in containers:
            username=container.find("div",{"class":"info_text"}).div.text
            rating_unparsed=container.find("span",{"class":re.compile(r'ui_bubble_rating')})["class"]
            userrating=float(rating_unparsed[-1:][0].split('_')[1])/10
            userrating=str(userrating)
            print(username+" : "+userrating+","+streetAddress)
            with open(fileName,'a') as handle:
                handle.write(hotelName+","+streetAddress+","+username+","+userrating)
                handle.write("\n")
        # last page of reviews string datatype
        try:
            lastPage=int(soup.find("a",{"class":"pageNum last taLnk "})['data-page-number'])
            startPage=1
        except:
            lastPage=1
            startPage=0
        print("Number of Pages for hotel"+hotelName+" is " + str(lastPage))
        #https://baseurl/Hotel_Review-g293890-d308286-Reviews-or5-Hotel_Shanker-Kathmandu_Kathmandu_Valley_Bagmati_Zone_Central_Region.html
        pg=5
        with open(fileName,'a') as handle:
            print("First page completed...")
            handle.write(hotelName+","+streetAddress+","+username+","+userrating)
            handle.write("\n")
            for i in range(1,lastPage):
                parts=re.sub('Reviews-','Reviews-or'+str(pg)+'-',urlnext)
                print("Next url in pagination: "+ parts)
                pg=pg+5
                browser.get(parts)
                html_doc = browser.page_source
                soup = BeautifulSoup(html_doc, 'lxml')
                hotelName = soup.find("h1", {"id": "HEADING"}).text
                containers = soup.find_all("div", {"class": "review-container", "data-reviewid": re.compile(r'\w+')})
                for container in containers:
                    username = container.find("div", {"class": "info_text"}).div.text
                    rating_unparsed = container.find("span", {"class": re.compile(r'ui_bubble_rating')})["class"]
                    userrating = float(rating_unparsed[-1:][0].split('_')[1]) / 10
                    userrating = str(userrating)
                    print(username + " : " + userrating)
                    handle.write(hotelName+","+streetAddress+","+username+","+userrating)
                    handle.write("\n")

