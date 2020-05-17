import re
fh=open("input.txt","r")
y=list()
for line in fh:
    x=re.findall("[0-9]+",line)
    y.extend(x)
y=[int(i) for i in y]
s=sum(y)
print(s)
""" y=list()
print(sum( [ int (i) for i in y.extend(re.findall("[0-9]+",line)) ]  for line in open("input.txt","r") ) ) """
