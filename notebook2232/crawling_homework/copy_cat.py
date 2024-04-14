
#라이브러리 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd
from datetime import datetime, timedelta
import xlsxwriter 
import schedule

def python_project():
    #라이브러리 
    browser = webdriver.Chrome()
    url = 'https://www.koreabaseball.com/Record/TeamRank/TeamRankDaily.aspx'
    browser.get(url)
    recent_day = browser.find_element(By.CLASS_NAME, "date").text
    browser.find_element(By.CLASS_NAME, "ui-datepicker-trigger").click() # 데이트피커 클릭
    time.sleep(1)
    browser.find_element(By.XPATH, "//*[@id=\"ui-datepicker-div\"]/div/a[1]").click() # 이전달 클릭
    browser.find_element(By.XPATH, "//*[@id=\"ui-datepicker-div\"]/table/tbody/tr[4]/td[7]/a").click()
    excel_writer = pd.ExcelWriter('baseball_data.xlsx', engine='xlsxwriter')
    while True:
        time.sleep(1)
        table = browser.find_element(By.CLASS_NAME, "tData").text
        lines = table.strip().split('\n')
        rows = [line.split() for line in lines]
        df = pd.DataFrame(rows[1:], columns=rows[0])
        df = df.drop(columns=['게임차', '연속', '홈', '방문'])
        sheet_name = browser.find_element(By.CLASS_NAME, "date").text
        df.to_excel(excel_writer, index=False, sheet_name=sheet_name)
        next_button = browser.find_element(By.CLASS_NAME, "date_next")  
        next_button.click()
        date = browser.find_element(By.CLASS_NAME, "date").text
        if date == recent_day:
            print("데이터 수집 완료")
            break   
    excel_writer.close()
python_project()
schedule.every().day.at("08:00").do(python_project)
while True:
    schedule.run_pending()
    time.sleep(1)