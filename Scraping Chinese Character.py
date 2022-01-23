# Try to scrape a website to collect Chinese Character, Pinyin, Definition
# import library to use


from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# identify the URL
my_url = 'http://hanzidb.org/character-list/hsk/level-1'

uClient = uReq(my_url)

# open and close the file after reading
page_html = uClient.read()
uClient.close()


page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("tr")

# identify which column you need, make a loop that loop through and grab the 
hanzi_temp = []
for container in containers:
    hanzi_temp.append(container.td)

hanzil = hanzi_temp[1:]
hanzilist = []
pinyin = []
count = 0

for x in hanzil:
    hanzi = x.text
    hanzilist.append(hanzi)

for tr in page_soup.findAll('tr'):
    td = tr.findAll('td')[1:3]
    if td:
        y = td[0].text
        z = td[1].text
        pinyin.append(y)
        

for rows in range(1,101):
    print(hanzilist[count]+ " " +pinyin[count])
    count+= 1

          
