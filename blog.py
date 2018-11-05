from bs4 import BeautifulSoup
import urllib2
url = "http://pramode.net/"
c = urllib2.urlopen(url).read()
s = BeautifulSoup(c)
for i in s.find_all('a'):
    print(i.get("href"))
for i in s.find_all('img'):
    print(i.get("src"))

