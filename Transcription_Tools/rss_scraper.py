import collections
from bs4 import BeautifulSoup
import requests 
import collections 
from datetime import datetime
import lxml


numSuc = 0
numFail = 0

with open("reuters.xml", encoding='utf-8') as fp:
    soup = BeautifulSoup(fp, 'xml')

links = collections.defaultdict()
#https://stackoverflow.com/questions/71692277/how-to-scrape-multiple-rss-feeds-and-store-results-respectively-in-their-csvs
for entry in soup.find_all("item"): 
    # Finding the day it was published to correctly name the mp3 file
    str_date = entry.find('pubDate').text
    date = datetime.strptime(str_date, "%a, %d %b %Y %H:%M:%S %z")

    # I only want things in March
    if (date.month == 3 and date.year == 2024):
      file_title = "reuters/mp3s/" + str(date.month) + "_" + str(date.day) + ".mp3"
     
      try:
        # Getting & downloading the link
        link = entry.enclosure["url"]
        print("Attempting to download podcast at ", link)
        r = requests.get(link, allow_redirects=True)
        open(file_title, 'wb').write(r.content)
        numSuc += 1
      except Exception as e:
         print(e)
         print("Failed to download mp3 at", link)
         numFail += 1

print("Number of successful downloads: ", numSuc)
print("Number of failures: ", numFail)


      


