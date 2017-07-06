# coding: utf-8

import requests
from bs4 import BeautifulSoup

def main():
    url = 'http://finance.naver.com/item/sise.nhn?code=028260'

    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    per_table = soup.select('#aside .aside_invest_info #tab_con1 .per_table')


    krx_per = per_table[0].find('em', {'id': 'krx_per'}).text
    cns_per = per_table[0].find('em', {'id': '_cns_per'}).text
    pbr = per_table[0].find('em', {'id': '_pbr'}).text # 크롤링 동작시 무한대 표시가 리턴됨.
    dvr = per_table[0].find('em', {'id': '_dvr'}).text

    print(krx_per, cns_per, pbr, dvr)




main()
