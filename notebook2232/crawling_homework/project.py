
#라이브러리 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd
from datetime import datetime, timedelta
import xlsxwriter 
import schedule

browser = webdriver.Chrome()
url = 'https://www.koreabaseball.com/Record/TeamRank/TeamRankDaily.aspx'
browser.get(url)
time.sleep(1)
all_data = pd.DataFrame()  # 모든 데이터를 저장할 데이터프레임 초기화
recent_day = browser.find_element(By.CLASS_NAME, "date").text
time.sleep(1)
table = browser.find_element(By.CLASS_NAME, "tData").text
lines = table.strip().split('\n')
rows = [line.split() for line in lines]
df = pd.DataFrame(rows[1:], columns=rows[0])
df = df.drop(columns=['게임차', '연속', '홈', '방문'])
all_data = pd.concat([all_data, df], ignore_index=True)  # 기존 데이터프레임과 새로운 데이터프레임을 합침
all_data.to_csv('baseball_practice.csv', index=False, encoding='utf-8-sig')  # 파일 저장