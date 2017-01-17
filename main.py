# -*- coding: utf-8 -*-
#! python3.5.1
import time
import os
import multiprocessing
import csv
from NewsPage import NewsPage
from bs4 import BeautifulSoup
from multiprocessing import Pool, freeze_support
from timecode import generate_url_list
from itertools import chain


def crawler(urlList):
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


def splitList(urlList, num_core):
    part_len = len(urlList) // num_core
    mod = len(urlList) % num_core
    return [urlList[part_len * i:part_len * i + part_len + mod * (i == num_core - 1)]
            for i in range(num_core)]


def saveAsCsv(result):
    with open('news_data.csv', 'w', encoding='utf-8') as csvfile:
        field_names = ['name', 'url', 'class', 'article']
        writer = csv.DictWriter(csvfile,
                                dialect='excel',
                                delimiter=',',
                                quoting=csv.QUOTE_MINIMAL,
                                lineterminator='\n',
                                fieldnames=field_names)
        writer.writeheader()
        for news in result:
            writer.writerow(news)

if __name__ == "__main__":
    freeze_support()
    os.system("clear")
    numProcesses = int(multiprocessing.cpu_count())
    print('You have %d core.' % (numProcesses))
    Classification = ["world", "politics", "sport", "football", "culture",
                      "business", "lifeandstyle", "fashion", "environment",
                      "technology", "travel"]
    urlList = generate_url_list('https://www.theguardian.com',
                                2010,
                                2010,
                                Classification)
    partition = splitList(urlList, numProcesses)
    pool = Pool(processes=numProcesses)
    startTime = time.time()
    newsList = pool.map(crawler, partition)
    print('cost %.1fs' % (time.time() - startTime))
    result = list(chain.from_iterable(newsList))
    print('start saving.')
    saveAsCsv(result)
    print('end')
