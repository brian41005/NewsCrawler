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

    # def __getstate__(self):
    #     return self.__dict__.copy()
    #
    # def __setstate__(self, state):
    #     self.__dict__.update(state)

    def __repr__(self):
        return 'NewsPage:{0}'.format(self.url)

    def __GetNewsUrl(self):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
            soup = BeautifulSoup(requests.get(
                self.url, timeout=5, headers=headers).text, 'lxml')
            for news_block in soup.findAll('div', attrs={'class': 'fc-item__content'}):
                for each_block in news_block.findAll('a', href=True):

                    if each_block['href'] != '' and each_block['href'] != None and each_block['href'].find('https://www.theguardian.com') >= 0:
                        self.newsList.append(News(url=each_block['href']))

        except ConnectionError as msg:
            return
        except Exception as msg:
            print(msg)
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
            time.sleep(0.05)

    def get(self):
        self.CheckThreadAlive()
        return [news.get() for news in self.newsList if not news.isNone()]


if __name__ == "__main__":
    urlList = ['https://www.theguardian.com/world/2010/feb/23/all']
    Classification = ['world']
    # urlList = timecode.generate_url_list('https://www.theguardian.com', 2010, 2010, Classification)
    myNewsPage = NewsPage(urlList[0])
    myNewsPage.GetAllNewsData()
    print(myNewsPage.__dict__)
