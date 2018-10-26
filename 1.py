import urllib.request
r = urllib.request.urlopen('http://www.google.com')
print(r.read())

