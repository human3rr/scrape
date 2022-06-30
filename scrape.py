from bs4 import BeautifulSoup
import re
from urllib.request import Request, urlopen
import youtube_dl

def getWSHlinks(page):
    req = Request(page, headers={'User-Agent': 'Mozilla/5.0'})
    html_page = urlopen(req).read()

    soup = BeautifulSoup(html_page, 'html.parser')

    soup.body.find_all("time")


    results = soup.find_all('a', attrs={"class":"video-box"})

    hrefs = []
    for x in results:
        #print(x.get('href'))
        hrefs.append(x.get('href'))
    return hrefs

weekLongVidRefs = getWSHlinks("https://worldstarhiphop.com/videos/")
weekLongVidRefs.extend(getWSHlinks("https://worldstarhiphop.com/videos/?start=2"))

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(weekLongVidRefs)
print(len(weekLongVidRefs))
