from bs4 import BeautifulSoup
import re
import urllib.request,urllib.parse,urllib.error

url="http://py4e-data.dr-chuck.net/known_by_Orran.html"
position= 18
times= 7

for i in range(1,times+1):
    tag=BeautifulSoup(urllib.request.urlopen(url).read(),"html.parser")("a")[position-1]
    url=tag.get("href",None)

print(re.search("[A-Z][a-z]+",tag.decode())[0])


