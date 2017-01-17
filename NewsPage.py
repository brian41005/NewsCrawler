# -*- coding: utf-8 -*-
#! python3.5.1

import requests
import lxml
from News import News
import time
import timecode
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError


class NewsPage:
    '''
    '''

    def __init__(self, url):
        self.url = url
        self.newsList = []
        self.__GetNewsUrl()

    def __GetNewsUrl(self):
        try:
            soup = BeautifulSoup(requests.get(self.url).text, 'lxml')
            for news_block in soup.findAll('div', attrs={'class': 'fc-item__content'}):
                for each_block in news_block.findAll('a', href=True):

                    if each_block['href'] != '' and each_block['href'] != None and each_block['href'].find('https://www.theguardian.com') >= 0:
                        self.newsList.append(News(url=each_block['href']))
        except ConnectionError as msg:
            return

    def CheckThreadAlive(self):
        while True:
            i = True
            for thread in self.newsList:
                if thread.isAlive():
                    i = False
                    time.sleep(.001)
            if i:
                break

    def GetAllNewsData(self):
        for news in self.newsList:
            news.start()

    def get(self):
        return [news.get() for news in self.newsList if not news.isNone()]

if __name__ == "__main__":
    urlList = ['https://www.theguardian.com/world/2010/feb/23/all']
    Classification = ['world']
    #urlList = timecode.generate_url_list('https://www.theguardian.com', 2010, 2010, Classification)
    myNewsPage = NewsPage(urlList[0])
    myNewsPage.GetAllNewsData()
    print(myNewsPage.__dict__)
