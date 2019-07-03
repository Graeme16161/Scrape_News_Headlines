# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 14:53:46 2019

@author: gakel
"""

import os
from datetime import datetime
import time

now = datetime.now()

YMD_str = now.strftime("%Y%m%d_%H%M")

os.system("scrapy crawl news_spider")

time.sleep(180) 

new_csv_name = "nasdaq_headlines" + "_" + YMD_str + ".csv"

os.rename("nasdaq_headlines.csv",new_csv_name)