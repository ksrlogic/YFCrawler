import os
from datetime import date, timedelta

import pandas as pd
import yfinance as yf
import mplfinance as mpf


#SETTTING

today = date.today()

today_year = today.year
today_month = today.month
today_day = today.day

num_days = 100 # 거래일
delta = timedelta(days=num_days)
start_date = today - delta

# 폴더를 생성할 경로
path = f"./Saved/{today}"

# 경로에 폴더가 없으면 폴더를 생성
if not os.path.exists(path):
    os.makedirs(path)
    print("폴더가 생성되었습니다.")
else:
    print("폴더가 이미 존재합니다.")

# 가져올 데이터들 정의

name_list = ["KOSPI", "KOSDAQ", "NASDAQ", "S&P500", "DOW JONES","gold", "SOYBEAN" , "WTI"]
code_list = ['^KS11', '^KQ11', '^IXIC', '^GSPC', '^DJI', 'GLD', 'SOYB', "CL=F"]
data_list = []

for data in code_list:
    data = yf.download(data, start=start_date, end=today)
    
    data_list.append(data)



def makeChart(index, index_name): 
    
    volume_state = True
    
    if index_name == "KOSDAQ":
        volume_state = False
    
    today_closing_price = round(index['Close'].iloc[-1], 2) 
    yesterday_closing_price = round(index['Close'].iloc[-2], 2) 

    price_change = today_closing_price - yesterday_closing_price
    percent_change = round((price_change / yesterday_closing_price) * 100 , 2)

    font_color = None
    
    #주석 색깔
    
    if percent_change > 0 :
        font_color = "Red"
        percent_change = f"+{str(percent_change)}%"
    elif percent_change < 0 :
        font_color = "Blue"
        percent_change = f"-{str(percent_change)}%"
    else:
        font_color = "Black"
        percent_change = f"+{str(percent_change)}%"

    fig, axlist = mpf.plot(index, type='candle', style='yahoo', volume = volume_state , mav = [5,10,20], title=f'{index_name} - RainLight', returnfig=True)
    ax = axlist[0]

    ax.annotate(f"{today_closing_price}({percent_change})",
                xy=(0.05, 0.95),
                xycoords='axes fraction',
                fontsize=12,
                ha='left',
                va='top', 
                color = f"{font_color}")

    mpf.show()
    fig.savefig(f'./Saved/{today}/{today} {index_name}')

for data, name in zip(data_list , name_list) :
    makeChart(data, name)