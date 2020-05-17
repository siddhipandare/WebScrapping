""" You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers. """

from bs4 import BeautifulSoup
import re
import urllib.request,urllib.parse,urllib.error

url="http://py4e-data.dr-chuck.net/comments_416294.html"
html=urllib.request.urlopen(url).read()
x=BeautifulSoup(html,"html.parser")

tags=x("span")
s=list()
for tag in tags:
    tag=tag.decode()
    y=re.findall("[0-9]+",tag)
    s.extend(y)
s=[int(x) for x in s]  
print(sum(s))