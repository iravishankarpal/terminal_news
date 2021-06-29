from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import time
import html5lib
import requests
import urllib.request        
url = "https://inshorts.com/en/read/"
r = requests.get(url)
soup = BeautifulSoup(r.content,"html.parser")
os.system("clear")
headline = soup.findAll("span")
print("reading news for\t"+url+"\n")
try:
    for span in headline:
         if(span.get('itemprop')=="headline"):
            print(span.text + "\n")
            time.sleep(5)              
except:
    print("      reading news has beens stop, exiting  ")
