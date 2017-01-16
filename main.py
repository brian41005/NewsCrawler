# -*- coding: utf-8 -*-
#! python3.5.1
import threading
import time
import os
import lxml
import multiprocessing
import timecode
import requests
from NewsPage import NewsPage
from bs4 import BeautifulSoup
from multiprocessing import Pool, freeze_support


def crawler(urlList):
    news = []
    templen = len(urlList)
    previousPercent = 0.0
    for i, url in enumerate(urlList):
        news.append(NewsPage(url))
        news[i].GetAllNewsData()
        news[i].CheckThreadAlive()

        percent = (float(i) / templen) * 100
        if abs(percent - previousPercent) > 1:
            print('%d%%' % (percent))
            previousPercent = percent
    return news


def splitList(urlList, num_core):
    partition = []
    for i in range(0, num_core):
        part_len = int(len(urlList) / num_core)
        index = part_len * i
        if num_core - 1 == i:
            partition.append(urlList[index:])
        else:
            partition.append(urlList[index:index + part_len])
    return partition

# def CreateCSV():
#     with open('news_data.csv', 'w', encoding='utf-8') as csvfile:
#         field_names = ['name', 'url', 'news_class','article']
#         writer = csv.DictWriter(csvfile,
#                                 dialect='excel',
#                                 delimiter = ',',
#                                 quoting = csv.QUOTE_MINIMAL,
#                                 lineterminator='\n',
#                                 fieldnames = field_names)
#         writer.writeheader()

if __name__ == "__main__":
    freeze_support()
    os.system("clear")
    # CreateCSV()
    numProcesses = int(multiprocessing.cpu_count())

    print('You have %d core.' % (numProcesses))

    Classification = ["world", "politics", "sport", "football", "culture",
                      "business", "lifeandstyle", "fashion", "environment",
                      "technology", "travel"]
    urlList = timecode.generate_url_list('https://www.theguardian.com', 2010, 2016, Classification)
    partition = splitList(urlList, numProcesses)

    pool = Pool(processes=numProcesses)
    startTime = time.time()
    news = pool.map(crawler, partition)
    print('[DONE]')
