# coding: utf-8

import datetime
import csv
import time
import requests
from bs4 import BeautifulSoup

class Stocks():

    def __init__(self, stock_type):
        self.stock_type = stock_type # 0 이면 코스피, 1이면 코스


    def get_code(self):

        self.stocks = []
        page_num = 27 # 코스피 27

        if self.stock_type:
            page_num = 25

        for num in range(1, page_num+1):
            url = 'http://finance.naver.com/sise/sise_market_sum.nhn?sosok={0}&page={1}'.format(self.stock_type, num)

            req = requests.get(url)
            html = req.text

            soup = BeautifulSoup(html, 'html.parser')
            stock_codes = soup.select('table.type_2 td a.tltle')

            for code in stock_codes:
                self.stocks.append((code.text, code['href'].split('=')[-1])) # 리스트에 리스트 묶음 형태로 (종목명, 종목코드)


        return self.stocks


    def get_historical_data(self, date):

        date = datetime.datetime.strptime(date, "%Y-%m-%d") # 원하는 날짜 선택 (지정 날짜부터 가장 최근 데이터까지 가져옴)
        page_num = 1

        for name, code in self.stocks:
            while True:
                url = 'http://finance.naver.com/item/sise_day.nhn?code={0}&page={1}'.format(code, page_num)

                req = requests.get(url)

                html = req.text
                soup = BeautifulSoup(html, 'html.parser')

                rows = soup.select('.type2 tr')

                for row in rows[2:]:
                    col = row.find_all('td')

                    try:
                        stock_date = datetime.datetime.strptime(col[0].text, "%Y.%m.%d")
                        print(name, code, stock_date, col[1].text, col[3].text, col[4].text, col[5].text, col[6].text)
                        """
                        col[1] : 종가, col[3] : 시가, col[4] : 고가, col[5] : 저가, col[6] : 거래량
                        """
                        if date > (stock_date + datetime.timedelta(days=1)):
                            print('원하시는 날짜까지 데이터 추출이 완료되었습니다.')
                            return False

                    except ValueError:
                        pass

                page_num += 1


        