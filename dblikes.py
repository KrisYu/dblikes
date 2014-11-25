import os
import urllib.request
from bs4 import BeautifulSoup
import html.parser

#最先抓出需要的东西，比如喜欢的页数
# url = "http://www.douban.com/people/yuxue/likes/"
# response = urllib.request.urlopen(url)
# soup = BeautifulSoup(response.read())
# a = soup.find_all('span',{"class":"thispage"})
# http://www.douban.com/people/yuxue/likes/
# pages = int(a[0].get('data-total-page'))

# def get_data_from_url(url,number):
#     like_href = []

#     for i in range(1,pages):
#         url_new = url + '?start=' + str(i*15)

##def get_url(url,pages):
##    for i in range(1,pages+1):
##        if i == 0:
##            return url
##        else:
##            return url + '?start=' + str(i*15)
    


def print_a_page(url):
    like_href=[]
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response.read())
    likes = soup.find_all("div",{"class":"content"})
    for like in likes:
        like_href.append((like.contents[1].contents[1].get('href'),like.contents[1].contents[1].contents,like.contents[3].contents[1].contents))
 
        #如何提出网址
        #items[0].contents[1].get('href')
        #如何提出文字
        #items[0].contents[1].contents
        #提出时间 times[0].contents
        #times = soup.find_all("p",{"class":"time"})
  

    for like in like_href:
        for i in like:
            print(i)
        print('\n')
    
    

    

def print_all(url,page):
    for i in range(page):
        if i == 0:
            print_a_page(url)
        else:
            url = url + '?start=' + str(i*15)
            print_a_page(url)

print_all('http://www.douban.com/people/yuxue/likes/',73)
    


		

