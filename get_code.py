import requests
from bs4 import BeautifulSoup


def main(stock_type, num):
    url = 'http://finance.naver.com/sise/sise_market_sum.nhn?sosok={0}&page={1}'.format(stock_type, num)

    req = requests.get(url)
    html = req.text

    soup = BeautifulSoup(html, 'html.parser')
    stock_codes = soup.select('table.type_2 td a.tltle')
    for code in stock_codes:
        print(code['href'].split('=')[-1], code.text)












if __name__ == "__main__":
    stock_type = 0 # 0이면 코스피 ,1이면 코스닥 
    page_num = 27 # 코스피는 27, 코스닥은 25
    for num in range(1, page_num+1): # +1을 해줘야 마지막 페이지까지 반복 가능.
        main(stock_type, num)