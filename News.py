# -*- coding: utf-8 -*-
#! /usr/bin/python3

import requests
import threading
import lxml
import random
import time
import webbrowser
import unicodedata
from ProcessArticle import *
from bs4 import BeautifulSoup
from requests.exceptions import *


class News(threading.Thread):
    '''
    '''

    def __init__(self, *, url='', retryTime=3):
        super(News,  self).__init__(name='')
        self.url = url
        try:
            self.newsClass = self.url.split('/')[3]
        except IndexError as msg:
            self.newsClass = ''
        self.name = ''
        self.article = ''
        self.retryTime = retryTime

    def run(self):
        try:
            # headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/55.0.2883.87 Chrome/55.0.2883.87 Safari/537.36',
            #            'Upgrade-Insecure-Requests': '1',
            #            'Connection': 'keep-alive',
            #            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            #            'Host': 'www.theguardian.com'
            #            }
            soup = BeautifulSoup(requests.get(self.url, timeout=5).text, 'lxml')
            self.__GetName(soup)
            if self.name != '':
                self.__GetArticle(soup)
        except (ConnectionError) as msg:
            print('[%d]ConnectionError:%s' % (3 - self.retryTime, self.url))
            if self.retryTime > 0:
                self.retryTime -= 1
                time.sleep(random.random())
                self.run()

        except:
            print(self.url)
            # webbrowser.open_new_tab(self.url)

    def __GetName(self, soup):
        try:
            self.name = soup.findAll(
                'h1', attrs={'class': 'content__headline js-score',
                             'itemprop': 'headline'})[0].string
            self.name = process(self.name)
            # print(self.name)
        except (IndexError, AttributeError) as errmsg:
            pass
        except UnicodeEncodeError as msg:
            pass

    def __GetArticle(self, soup):
        try:
            self.article = getArticle(soup)
            # print(self.article)
        except:
            pass

if __name__ == "__main__":
    urlList = ['https://www.theguardian.com/business/2014/may/25/astrazeneca-free-pfizer-for-now', 'https://www.theguardian.com/world/2010/feb/23/nicaragua-cancer-treatment-abortion', 'https://www.theguardian.com/business/2010/feb/23/protesters-blockade-greek-stock-exchange', 'https://www.theguardian.com/world/2010/feb/23/us-army-chief-end-anti-gay-rules', 'https://www.theguardian.com/world/2010/feb/23/china-denies-google-cyber-attacks', 'https://www.theguardian.com/world/2010/feb/23/bomb-maker-stay-in-service-iraq', 'https://www.theguardian.com/world/2010/feb/23/dennis-brutus-obituary', 'https://www.theguardian.com/world/2010/feb/23/corrie-death-law-case', 'https://www.theguardian.com/world/2010/feb/23/kenya-president-prime-minister-meet', 'https://www.theguardian.com/world/2010/feb/23/british-woman-killed-swat-valley',
               'https://www.theguardian.com/world/2010/feb/23/china-tells-schools-ban-oxfam', 'https://www.theguardian.com/world/2010/feb/23/indonesia-ranger-komodo-dragon-attack', 'https://www.theguardian.com/world/2010/feb/23/british-plane-spotters-face-jail-india', 'https://www.theguardian.com/world/2010/feb/23/32-missing-madeira-landslides-search', 'https://www.theguardian.com/world/julian-borger-global-security-blog/2010/feb/23/iran-iaea-letter', 'https://www.theguardian.com/world/2010/feb/23/iran-fuel-tehran-research-reactor', 'https://www.theguardian.com/world/2010/feb/23/taliban-captured-pakistan-abdul-kabir', 'https://www.theguardian.com/world/blog/audio/2010/feb/22/guardian-daily-podcast1', 'https://www.theguardian.com/world/picture/2010/feb/23/usa-air-transport']
    newsList = []
    for i, url in enumerate(urlList):
        newsList.append(News(url=url))
        newsList[i].start()
        break
