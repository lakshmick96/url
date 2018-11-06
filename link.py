def fnc(url):
    from bs4 import BeautifulSoup
    import urllib2
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content)
    return soup


url = ("http://pramode.net/")
for i in fnc(url).find_all('a'):
    print(i.get("href"))
    l = i.get("href")
    for j in fnc(l).find_all('a'):
        print(j.get("href"))

