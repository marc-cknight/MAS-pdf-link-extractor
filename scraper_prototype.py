from bs4 import BeautifulSoup

import requests

import pdb

import csv

'''Develop filter for href list to filter out useless links'''

filterurl='http://www.mas.gov.sg/Regulations-and-Financial-Stability/Regulations-Guidance-and-Licensing.aspx?'

r=requests.get(filterurl)

data=r.text

soup=BeautifulSoup(data)

filterlist=[]

for link in soup.find_all('a'):
    #develop filter list for href links and convert to list
    filterlist.append(link.get('href'))
    


'''Get lists of all links out'''

links=[]

for x in range(1,16):
    #HARDCODE range (temporarily)
    url='http://www.mas.gov.sg/Regulations-and-Financial-Stability/Regulations-Guidance-and-Licensing.aspx?to=&from=&q=%20&submit=true&page='+str(x)+'&ipp=100'
    #input("Enter a website to extract the URL's from:")

    r=requests.get(url)
    
    data=r.text
    
    soup=BeautifulSoup(data)
    
    for link in soup.find_all('a'):
        #get href links for download page from directory and convert into list
        
        links.append(link.get('href'))



'''filter out useless links from lists into list.accesslist'''

accesslist=list(set(links)-set(filterlist))


accesslist = list(filter(lambda x: x != None, accesslist))
#eliminate None



'''get pdf location'''

baseurl='http://www.mas.gov.sg'

pdflist=[]

ilist=[]
#temporary list to help filter by content of string

for x in accesslist[:len(accesslist)]:

    url=str(baseurl)+str(x)
    
    r=requests.get(url)
    
    data=r.text
    
    soup=BeautifulSoup(data)
    
    for link in soup.find_all('a'):
        
        ilist.append(link.get('href'))
        
ilist=list(filter(lambda x: x!=None,ilist))

for x in ilist:
    if 'pdf' in x:
        pdflist.append(x)
        
print (len(pdflist))
#countercheck number of links



'''export to csv file format'''

with open('list', 'w',newline='') as f:
    a=csv.writer(f)
    
    for x in pdflist:
        
        n=pdflist.index(x)
        
        a.writerow(pdflist[n:n+1])


        