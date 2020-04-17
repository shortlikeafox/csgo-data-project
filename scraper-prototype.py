from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re
site = 'https://www.hltv.org/results?team=4773'
hdr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
req = Request(site,headers=hdr)
html = urlopen(req)
bs = BeautifulSoup(html, 'html.parser')
print(bs)

#We need to grab the 100 most recent matches and save them....

link_list = []
for link in bs.find_all(
        'a', {'class':'a-reset'}):
    if 'href' in link.attrs:
        link_list.append(link.attrs['href'])
        
    
with open('temp_links.txt', 'w') as f:
    f.write(str(link_list))
    