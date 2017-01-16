# -*- coding: utf-8 -*-
#! python3.5.1

import re
import unicodedata
import requests
from bs4 import BeautifulSoup


class ArticleUtility(object):

    def __init__(self):
        pass

    def cutUrl(self, line):
        clean = re.compile('<.*?>')
        line = re.sub(clean, '', line)
        return line

    def process(self, article):
        article = unicodedata.normalize("NFKD", article)
        article = article.encode('utf-8', 'ignore').decode("utf-8", "ignore")
        article = article.strip(' ').strip('\n').strip('\r\n')
        article = re.sub('[^a-zA-Z]', ' ', article)
        article = re.sub(' . ', ' ', article)
        return article

    def getArticle(self, soup):
        article = ''
        for articleBody in soup.findAll('div',
                                        attrs={'class': 'content__article-body from-content-api js-article__body',
                                               'itemprop': 'articleBody',
                                               'data-test-id': 'article-review-body'
                                               }):

            for each_p in articleBody.findAll('p'):
                each_p = self.process(self.cutUrl(each_p.text))
                if each_p != '':
                    article += each_p
        return article

if __name__ == '__main__':

    urlList = ['https://www.theguardian.com/business/2014/may/25/astrazeneca-free-pfizer-for-now', 'https://www.theguardian.com/world/2010/feb/23/nicaragua-cancer-treatment-abortion', 'https://www.theguardian.com/business/2010/feb/23/protesters-blockade-greek-stock-exchange', 'https://www.theguardian.com/world/2010/feb/23/us-army-chief-end-anti-gay-rules', 'https://www.theguardian.com/world/2010/feb/23/china-denies-google-cyber-attacks', 'https://www.theguardian.com/world/2010/feb/23/bomb-maker-stay-in-service-iraq', 'https://www.theguardian.com/world/2010/feb/23/dennis-brutus-obituary', 'https://www.theguardian.com/world/2010/feb/23/corrie-death-law-case', 'https://www.theguardian.com/world/2010/feb/23/kenya-president-prime-minister-meet', 'https://www.theguardian.com/world/2010/feb/23/british-woman-killed-swat-valley',
               'https://www.theguardian.com/world/2010/feb/23/china-tells-schools-ban-oxfam', 'https://www.theguardian.com/world/2010/feb/23/indonesia-ranger-komodo-dragon-attack', 'https://www.theguardian.com/world/2010/feb/23/british-plane-spotters-face-jail-india', 'https://www.theguardian.com/world/2010/feb/23/32-missing-madeira-landslides-search', 'https://www.theguardian.com/world/julian-borger-global-security-blog/2010/feb/23/iran-iaea-letter', 'https://www.theguardian.com/world/2010/feb/23/iran-fuel-tehran-research-reactor', 'https://www.theguardian.com/world/2010/feb/23/taliban-captured-pakistan-abdul-kabir', 'https://www.theguardian.com/world/blog/audio/2010/feb/22/guardian-daily-podcast1', 'https://www.theguardian.com/world/picture/2010/feb/23/usa-air-transport']
    soup = BeautifulSoup(requests.get(urlList[0]).text, 'lxml')
    obj = ArticleUtility()
    print(obj.getArticle(soup))
