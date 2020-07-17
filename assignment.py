import re

fname = open("data.txt")
x=list()
for line in fname:
     y = re.findall('[0-9]+',line)
     x = x+y

tot=0
for z in x:
    tot = tot+ int(z)

print(tot)
