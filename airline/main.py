import os
import time
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driverPath="/usr/local/bin/chromedriver"
BaseFilePath="/Users/ush/Desktop/"
baseurl="https://www.flightradar24.com/data/airports/ktm/departures"
browser = webdriver.Chrome(driverPath)
browser.implicitly_wait(10)
browser.maximize_window()
browser.get(baseurl)
xbtncok='//button[@class="btn btn-blue"]'
BtnAcceptCookie=browser.find_element(by=By.XPATH, value=xbtncok)
BtnAcceptCookie.click()
print("Cookie accepted")
WebDriverWait(browser,25).until(EC.element_to_be_clickable((By.XPATH,'//button[text()="Load earlier flights"]'))).click()
time.sleep(10)
WebDriverWait(browser,25).until(EC.element_to_be_clickable((By.XPATH,'//button[text()="Load earlier flights"]'))).click()
time.sleep(10)
WebDriverWait(browser,25).until(EC.element_to_be_clickable((By.XPATH,'//button[text()="Load earlier flights"]'))).click()
time.sleep(10)
rawhtml=browser.find_elements(by=By.XPATH,value='//table/tbody/tr[@data-date]')
filename=BaseFilePath+"flightStatus"+str(int(time.time()))+".csv"
with open(filename,"w") as fh:
    fh.write("sep=#\n")
    fh.write("DepartureDate#InitDepTime#Flight#Dest#Airline#Aircraft#ActDepStatus#ActDepTime\n")
    for elem in rawhtml:
        DepDate=elem.get_attribute("data-date")
        Flight=elem.find_element_by_css_selector('td[class*="cell-flight-number"]').text
        Dest=elem.find_element_by_css_selector("div[ng-show='(objFlight.flight.airport.destination)']").text
        InitDepTime=elem.find_element_by_css_selector("td[class='ng-binding']").text
        ActDepStatus=elem.find_element(by=By.CSS_SELECTOR,value="span[class='ng-binding']").text
        Airline=elem.find_element_by_css_selector('td[class*="cell-airline"]').text
        Aircraft=elem.find_element_by_css_selector("span[ng-show='(objFlight.flight.aircraft.model.code)']").text
        AircraftReg=elem.find_element_by_css_selector("a[ng-show='(objFlight.flight.aircraft.registration)']").text
        ActDepTime="NA"
        if ActDepStatus=="Departed":
            tmp1=elem.find_element(by=By.CSS_SELECTOR,value="span[class='ng-binding']")
            ActDepTime=tmp1.find_element_by_xpath("./..").text
        fh.write(DepDate+"#"+InitDepTime+"#"+Flight+"#"+Dest+"#"+Airline+"#"+str(Aircraft)+" "+str(AircraftReg)+"#"+ActDepStatus+"#"+ActDepTime+"\n")
print("Finished fetching data..")
browser.quit()