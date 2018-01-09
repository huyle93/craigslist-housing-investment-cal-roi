#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 10:28:25 2017

@author: huyle
"""
#import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import numpy as np

mylist = []
myIntList = []
mypricelist = []



principal = float(input("how much is your house: "))
state = input("which state is this property? ")
urlRental = input("enter the rental url: ")

tax = {'nh': 0.0205,'ma': 0.01207 }



html = urlopen(urlRental)
soup = BeautifulSoup(html, "html.parser")

for i in soup.find_all("li", {"class":"result-row"})[1:]:
    for n in i.find_all("time", {"class":"result-date"}):
        time = (n['title'])
    for a in i.find_all('a', {"class":"result-title"}, href=True):
        href = a['href']
    a = i.find_all("a")
    for p in i.find_all('span',{"class":"result-price"}):
        price = p.get_text()
            
    data = time, a[1].text, "https://nh.craigslist.org/"+href, price
    mypricelist.append(price)
#    mylist.append(data)
for i in mypricelist:
    x = i[1:]
    if len(x) > 4:
        continue
    else:
        myIntList.append(x)
    print(i, "\n")
    
myIntList = [ int(x) for x in myIntList ]
avg = np.mean(myIntList)


# math
def getROI(avg, principalAfterTax):
    roi = (avg/principalAfterTax)*1000
    return roi
def getPrincipalAfterTax(principal, taxrate):
    principalAfterTax = principal - (principal*taxrate)
    return principalAfterTax


# return
text = "Average Rental Price is: "
print(text + str('$'+ str(avg)))
roi = getROI(avg, getPrincipalAfterTax(principal, tax['nh']))
print("Your ROI for this rental property is : " + str(roi) + "%")


 
#for li in x.find_all("li"):
#    for span in li.find_all("span"):
#        print(span)

#with open('myfile.csv', 'a') as outcsv:   
#    writer = csv.writer(outcsv, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
#    for item in mylist:
#        writer.writerow(item)

