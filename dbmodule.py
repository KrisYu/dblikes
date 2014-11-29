import os
import urllib.request
import html.parser

from bs4 import BeautifulSoup


outfile = open('time.txt','w')

outfile.write('time')
outfile.write('\n')


def print_a_page(url):
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response.read())
    times = soup.find_all('p',{'class':'time'})

    for time in times:
            outfile.write(str(time.contents[0]))
            outfile.write('\n')


def get_urls(url,page):
    for i in range(page):
        if i == 0:
            print_a_page(url)
        else:
            print_a_page(url + '?start=' + str(i*15))
    


get_urls('http://www.douban.com/people/yuxue/likes/',73)






    
# s = '2013年9月19日  17:59喜欢'
#re.findall('[0-9]{4}\u5e74.*[0-9]*.\u65e5',s)
# return  ['2013年9月19日']

        

