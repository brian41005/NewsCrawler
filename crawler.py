# -*- coding: utf-8 -*-
#! python3.5.1
import time
import multiprocessing
import csv
import datetime
from NewsPage import NewsPage
from bs4 import BeautifulSoup
from multiprocessing import Pool, freeze_support, Queue, cpu_count
from timecode import generate_url_list
from itertools import chain


def crawlerfunc(urlList):
    pages = []
    templen = len(urlList)
    previousPercent = 0.0
    for i, url in enumerate(urlList):
        pages.append(NewsPage(url))
        pages[i].GetAllNewsData()
        pages[i].CheckThreadAlive()

        percent = (float(i) / templen) * 100
        if abs(percent - previousPercent) > 1:
            print('%d%%' % (percent))
            previousPercent = percent
    return [news for page in pages for news in page.get()]


class crawler:
    '''
    '''

    def __init__(self, core=cpu_count()):
        self.core = core
        self.classification = ["world", "politics", "sport", "football", "culture",
                               "business", "lifeandstyle", "fashion", "environment",
                               "technology", "travel"]
        self.urlList = generate_url_list('https://www.theguardian.com',
                                         2010,
                                         2016,
                                         self.classification)
        self.startTime = None
        self.endTime = None
        self.newsList = None
        self.datetime = None

    def start(self):
        print('You have %d core.' % (self.core))
        partition = self.__splitList(self.urlList, self.core)

        self.datetime = datetime.datetime.now()
        self.startTime = time.time()
        pool = Pool(processes=self.core)
        newsList = pool.map(crawlerfunc, partition)
        self.newsList = list(chain.from_iterable(newsList))
        self.endTime = time.time()

    def save(self, filename='news_data.csv'):
        print('start saving')
        with open(filename, 'w', encoding='utf-8') as csvfile:
            field_names = ['name', 'url', 'class', 'article']
            writer = csv.DictWriter(csvfile,
                                    dialect='excel',
                                    delimiter=',',
                                    quoting=csv.QUOTE_MINIMAL,
                                    lineterminator='\n',
                                    fieldnames=field_names)
            writer.writeheader()
            for news in self.newsList:
                writer.writerow(news)
        print('end')

    def get(self):
        print('start time:%s' % (self.datetime))
        print('cost:%.2fs' % (self.endTime - self.startTime))
        print('list has %d news' % (len(self.newsList)))

    def __splitList(self, urlList, num_core):
        part_len = len(urlList) // num_core
        mod = len(urlList) % num_core
        return [urlList[part_len * i:part_len * i + part_len + mod * (i == num_core - 1)]
                for i in range(num_core)]
