# -*- coding: utf-8 -*-
#! python3.5.1
import os
from crawler import crawler

if __name__ == "__main__":
    os.system("clear")
    testcrawler = crawler()
    testcrawler.start()
    testcrawler.save()
    testcrawler.get()
