# -*- coding: utf-8 -*-
#! python3.5.1
"""
Created on Wed Jun 08

@author: brian
"""
import calendar


def generate_url_list(url, startYear, endYear, newsClass, end_month=12):
    dateList = []
    year, mth = range(startYear, endYear + 1), range(1, 13)
    mth_list = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]

    #Classification = ["world","politics","uk/sport","football","uk/culture","uk/business","lifeandstyle","fashion","uk/environment","uk/technology","travel"]
    Classification = newsClass
    for y in year:
        for m in mth:
            if end_month < m and y == endYear:
                break
            for d in range(1, calendar.monthrange(y, m)[1] + 1):
                for c in Classification:
                    dateList.append('%s/%s/%d/%s/%02d/all' % (url, c, y, mth_list[m - 1], d))
    print("number of day: %d" % (len(dateList)))
    return dateList
#------------------------------------------------------------------------------
if __name__ == "__main__":
    #Classification = ["world","politics","sport","football","culture","business","lifeandstyle","fashion","environment","technology","travel"]
    Classification = ['world']
    myList = timecode('https://www.theguardian.com', 2010, 2016, Classification, end_month=5)
    print(myList)
