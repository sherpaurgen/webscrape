#python3
from lxml import etree
from lxml import html
import requests
url='http://kathmandupost.ekantipur.com/'
page=requests.get(url)
#page=requests.get('http://kathmandupost.ekantipur.com/news/2018-01-08/supreme-court-instructs-nepal-police-to-present-dr-kc-before-court.html')
#page = requests.get('http://www.cnn.com')
html_content = html.fromstring(page.content)
headlines=html_content.xpath('//a/@href')
headlines_set=set(headlines)

del headlines
for i in headlines_set:
    print(i)
print("#########################")
for link in headlines_set:
     if link.startswith('/news/'):
         story=requests.get(url+link)
         html_content=html.fromstring(story.content)
         story_detail=html_content.xpath('//div[@class="content-wrapper "]/p/text()')
         for i in story_detail:
             print(i.strip())
