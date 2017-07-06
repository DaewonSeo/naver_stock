# coding: utf-8

import datetime
import csv
import time
import requests
from bs4 import BeautifulSoup

class Stocks():

    def __init__(self, date, stock_type, file_name):
        self.date = date
        self.stock_type = stock_type
        self.file_name = file_name

    def
