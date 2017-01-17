# -*- coding: utf-8 -*-
#! /usr/bin/python3

import requests
import threading
import lxml
import random
import time
import unicodedata
import myUtility
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
        self.utility = myUtility.ArticleUtility()

    def run(self):
        try:
            soup = BeautifulSoup(requests.get(self.url, timeout=5).text, 'lxml')
            self.__GetName(soup)
            if self.name != '':
                self.__GetArticle(soup)

            if self.retryTime != 3:
                print('[RETRY]:%s' % (self.url))

        except (ConnectionError) as msg:
            print('[%d]ConnectionError:%s' % (3 - self.retryTime, self.url))
            if self.retryTime > 0:
                self.retryTime -= 1
                time.sleep(random.random())
                self.run()

        except NameError as msg:
            print(msg)

    def __GetName(self, soup):
        try:
            self.name = soup.findAll(
                'h1', attrs={'class': 'content__headline js-score',
                             'itemprop': 'headline'})[0].string
            self.name = self.utility.process(self.name)
            # print(self.name)
        except (IndexError, AttributeError) as errmsg:
            pass
        except UnicodeEncodeError as msg:
            pass

    def __GetArticle(self, soup):
        try:
            self.article = self.utility.getArticle(soup)
            # print(self.article)
        except:
            pass

    def get(self):
        return {'url': self.url,
                'name': self.name,
                'class': self.newsClass,
                'article': self.article}

    def isNone(self):
        return self.name == '' or self.article == ''


if __name__ == "__main__":
    urlList = ['https://www.theguardian.com/business/2014/may/25/astrazeneca-free-pfizer-for-now', 'https://www.theguardian.com/world/2010/feb/23/nicaragua-cancer-treatment-abortion', 'https://www.theguardian.com/business/2010/feb/23/protesters-blockade-greek-stock-exchange', 'https://www.theguardian.com/world/2010/feb/23/us-army-chief-end-anti-gay-rules', 'https://www.theguardian.com/world/2010/feb/23/china-denies-google-cyber-attacks', 'https://www.theguardian.com/world/2010/feb/23/bomb-maker-stay-in-service-iraq', 'https://www.theguardian.com/world/2010/feb/23/dennis-brutus-obituary', 'https://www.theguardian.com/world/2010/feb/23/corrie-death-law-case', 'https://www.theguardian.com/world/2010/feb/23/kenya-president-prime-minister-meet', 'https://www.theguardian.com/world/2010/feb/23/british-woman-killed-swat-valley',
               'https://www.theguardian.com/world/2010/feb/23/china-tells-schools-ban-oxfam', 'https://www.theguardian.com/world/2010/feb/23/indonesia-ranger-komodo-dragon-attack', 'https://www.theguardian.com/world/2010/feb/23/british-plane-spotters-face-jail-india', 'https://www.theguardian.com/world/2010/feb/23/32-missing-madeira-landslides-search', 'https://www.theguardian.com/world/julian-borger-global-security-blog/2010/feb/23/iran-iaea-letter', 'https://www.theguardian.com/world/2010/feb/23/iran-fuel-tehran-research-reactor', 'https://www.theguardian.com/world/2010/feb/23/taliban-captured-pakistan-abdul-kabir', 'https://www.theguardian.com/world/blog/audio/2010/feb/22/guardian-daily-podcast1', 'https://www.theguardian.com/world/picture/2010/feb/23/usa-air-transport']
    newsList = []
    for i, url in enumerate(urlList):
        newsList.append(News(url=url))
        newsList[i].start()
        break
