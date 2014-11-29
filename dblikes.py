import os
import urllib.request
import html.parser

from bs4 import BeautifulSoup

#These lines open a csv file and write the header
outfile = open('dblikes.csv','w')
outfile.write("links")
outfile.write(',')
outfile.write("title")
outfile.write(',')
outfile.write("time")
outfile.write(',')
outfile.write("\n")


def start():
    
    id = input('put the user id in: ').strip()
    url = 'http://www.douban.com/people/'+ id + '/likes/'       
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response.read())
    page = int(soup.find_all('span',{'class':'thispage'})[0].get('data-total-page'))

    write_to_file(url,page)


def print_a_page(url):

    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response.read())
    likes = soup.find_all("div",{"class":"content"})
    times = soup.find_all('p',{'class':'time'})

    for i in range(len(likes)):
        title = likes[i].find_all('div',{'class':'title'})[0].contents[1].get('href')
        href = likes[i].find_all('div',{'class':'title'})[0].contents[1].contents[0]
        time = times[i].contents[0]


        outfile.write(str(href))
        outfile.write(',')
        outfile.write(str(title))
        outfile.write(',')
        outfile.write(str(time))
        outfile.write('\n')


        print('-'*50,'\n')
        print('Writing to file....')
        print(title)
        print(time)
        print(href)
        print('\n')


def write_to_file(url,page):

    for i in range(page):
        if i == 0:
            print_a_page(url)
        else:
            print_a_page(url + '?start=' + str(i*15))


start()


    



