#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 14:08:21 2018

@author: Michal
"""

import requests
import bs4

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
page
print(page.status_code) 
print(page.content)

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')


