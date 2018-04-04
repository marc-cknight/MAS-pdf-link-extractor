from bs4 import BeautifulSoup

import re

import requests

import pdb

import csv


'''Get links from directory'''

links=[]

for x in range(7,8):
    #HARDCODE range (temporarily)
    url='http://www.mas.gov.sg/Regulations-and-Financial-Stability/Regulations-Guidance-and-Licensing.aspx?to=&from=&q=%20&submit=true&page='+str(x)+'&ipp=100'
    #input("Enter a website to extract the URL's from:")

    r=requests.get(url)
    
    data=r.text
    
    soup=BeautifulSoup(data)
    
    for link in soup.find_all('a',id=re.compile("^pagecontent")):
    #get href links for download page from directory and convert into list
        links.append(link.get('href'))


print (len(links))
#Sanitycheck

accesslist = list(filter(lambda x: x != None, links))
#eliminate None

print(len(accesslist))
#Sanitycheck

'''get pdf links from accesslist links'''

baseurl='http://www.mas.gov.sg'

pdflist=[]
#final list of pdf links

ilist=[]
##temporary list to help filter by content of string

for x in accesslist[:len(accesslist)+1]:

    url=str(baseurl)+str(x)
    
    r=requests.get(url)
    
    data=r.text
    
    soup=BeautifulSoup(data)
    
    for link in soup.find_all('a', attrs={'href': re.compile('pdf')}):
    #Get pdf links from soup
        
        ilist.append(link.get('href'))

print (len(ilist))
#Sanitycheck

ilist=list(filter(lambda x: x!=None,ilist))


for x in ilist:
    if 'pdf' in x:
        pdflist.append(x)
        
print (len(pdflist))
#Sanitycheck


'''export to csv file format'''

with open('list', 'w',newline='') as f:
    a=csv.writer(f)
    
    for x in pdflist:
        
        n=pdflist.index(x)
        
        a.writerow(pdflist[n:n+1])


        