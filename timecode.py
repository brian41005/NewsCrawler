# -*- coding: utf-8 -*-
#! python3.5.1
"""
Created on Wed Jun 08

@author: brian
"""
import calendar
import datetime


def generate_url_list(url, startdate, enddate, newsClass, end_month=12):
    dateList = []

    start = datetime.datetime.strptime(startdate, '%Y/%m/%d')
    end = datetime.datetime.strptime(enddate, '%Y/%m/%d')

    datelist = [(start + datetime.timedelta(days=x)).strftime('%Y/%b/%d').lower()
                for x in range(0, (end - start).days + 1)]
    for d in datelist:
        for c in newsClass:
            dateList.append('https://www.theguardian.com/%s/%s/all' % (c, d))

    print("number of day: %d" % (len(dateList)))
    return dateList


if __name__ == "__main__":
    # Classification = ["world","politics","sport","football","culture","business",
    # "lifeandstyle","fashion","environment","technology","travel"]
    Classification = ['world']
    myList = generate_url_list('https://www.theguardian.com', '2007/1/1',
                               '2017/5/31', Classification, end_month=5)
    print(myList[:10])
