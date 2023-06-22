import requests                        #gets the information from the webpage in the form of html
from bs4 import BeautifulSoup          #extract information from HTML tags
import time
import csv

urls = ["https://finance.yahoo.com/quote/GOOGL?p=GOOGL&.tsrc=fin-srch","https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch",
        "https://finance.yahoo.com/quote/NFLX?p=NFLX&.tsrc=fin-srch","https://finance.yahoo.com/quote/HPE?p=HPE&.tsrc=fin-srch",
        "https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch","https://finance.yahoo.com/quote/TSLA?p=TSLA&.tsrc=fin-srch"]

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

csv_file = open("scraper.csv","w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Stock Name','Current Price', 'Previous Close','Open','Bid','Ask','Day\'s Range','52 Week Range','Volume','Avg. Volume','Market Cap','Beta (5Y Monthly)', 'PE Ratio (TTM)', 'EPS (TTM)', 'Earnings Date', 'Forward Dividend & Yield', 'Ex-Dividend Date', '1y Target Est'])

for url in urls:
    stock = []
    html_page = requests.get(url,headers=headers)

    soup = BeautifulSoup(html_page.content,'lxml')
    header_info = soup.find_all("div",id="quote-header-info")[0]

    stock_title = header_info.find("h1").get_text()
    #print(stock_title)
    stock_price = header_info.find("div", class_="D(ib) Va(m) Maw(65%) Ov(h)").find("fin-streamer").get_text()
    #print(stock_price)
    
    stock.append(stock_title)
    stock.append(stock_price)
    


    table_info = soup.find_all("div", id="quote-summary")[0].find_all("tr")

    for i in range(0,16):
        value = table_info[i].find_all("td")[1].get_text()
        stock.append(value)
    csv_writer.writerow(stock)
    time.sleep(1)

csv_file.close()