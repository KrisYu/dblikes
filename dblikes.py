import os
import urllib.request
from bs4 import BeautifulSoup
import html.parser

outfile = open('dblikes.txt','w')

def print_a_page(url):
    like_href=[]
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response.read())
    likes = soup.find_all("div",{"class":"content"})
    for like in likes:
        title = like.contents[1].contents[1].get('href')
        href = like.contents[1].contents[1].contents
        time = like.contents[3].contents[1].contents
 #       outfile.write('\n'.join(title.encode('ascii', 'ignore')))
#        outfile.write('\n'.join(time.encode('ascii', 'ignore')))
#        outfile.write('\n'.join(href.encode('ascii', 'ignore')))
#        outfile.write('\n')

        print('-'*50,'\n')
        print('Writing to file....')
        print(title)
        print(time)
        print(href)
        print('\n')


        '''
        like.find_all("div",{"class":"title"})[0].contents[1]
        获得如<a href="http://www.douban.com/photos/photo/2211942112/" target="_blank">知乎：如何科学的吐槽</a>
        然后根据DOM树把title， href， time 提出来
        ''' 
    

def print_all(url,page):
    for i in range(page):
        if i == 0:
            print_a_page(url)
        else:
            url = url + '?start=' + str(i*15)
            print_a_page(url)

print_all('http://www.douban.com/people/yuxue/likes/',2)
    


        

