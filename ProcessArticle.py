# -*- coding: utf-8 -*-
#! python3.5.1

import re
import unicodedata


def cutUrl(line):
    clean = re.compile('<.*?>')
    line = re.sub(clean, '', line)
    return line


def process(article):
    article = unicodedata.normalize("NFKD", article)
    article = article.encode('utf-8', 'ignore').decode("utf-8", "ignore")
    article = article.strip(' ').strip('\n').strip('\r\n')
    article = re.sub('[^a-zA-Z]', ' ', article)
    article = re.sub(' . ', ' ', article)
    return article


def getArticle(soup):
    article = ''
    for articleBody in soup.findAll('div',
                                    attrs={'class': 'content__article-body from-content-api js-article__body',
                                           'itemprop': 'articleBody',
                                           'data-test-id': 'article-review-body'
                                           }):

        for each_p in articleBody.findAll('p'):
            each_p = process(cutUrl(each_p.text))
            if each_p != '':
                article += each_p
    return article
