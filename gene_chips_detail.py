#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import os
import csv
import requests
from selenium import webdriver
from datetime import datetime

def fun(browser, file, no, name, url):
    time.sleep(3)
    s = requests.Session()
    # 从driver中获取cookie列表（是一个列表，列表的每个元素都是一个字典）
    cookies = browser.get_cookies()
    # 把cookies设置到session中
    for cookie in cookies:
        s.cookies.set(cookie['name'], cookie['value'])
    browser.get(url)
    try:
        summary=browser.find_element_by_class_name('patent_b').find_element_by_class_name('c').text.strip()
        rs=no+'|'+name+'|'+summary
        trs=browser.find_element_by_id('inid').find_elements_by_tag_name('tr')
        i=1
        for tr in trs:
            if i==3 or i==4 or i==5:
                td=tr.find_element_by_tag_name('td')
                rs=rs+'|'+td.text
            i=i+1
        rs=rs+'|'+browser.find_element_by_id('claims').text.replace(" ", "").replace("\n", "")+'\n'
        file.write(rs)
    except BaseException as e:
        print('BaseException:', e)
    finally:
        file.flush()

if __name__ == '__main__':
    chrome_drive = '/Users/jiangxingqi/Sina/chromedriver'
    browser = webdriver.Chrome(executable_path=chrome_drive)
    file = open('rs9.csv', 'w')
    sFileName = 'url_list2.csv'
    with open(sFileName, newline='', encoding='UTF-8') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            no=row[0]
            name=row[1]
            url=row[2]
            if 'http' in url:
                print(no)
                try:
                    fun(browser, file, no, name, url)
                except BaseException as e:
                    print('BaseException:', e)
                finally:
                    print("get success")
    browser.close()
    file.close()