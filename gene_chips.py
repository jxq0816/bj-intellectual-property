#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import os
from selenium import webdriver
from datetime import datetime

def fun(browser,file):
    time.sleep(3)
    searchresult_v=browser.find_element_by_id('searchresult_v')
    list=searchresult_v.find_elements_by_tag_name('li')
    for li in list:
        url=li.find_element_by_name('v_TI')
        num=li.find_element_by_class_name('num').text
        href=url.get_attribute("href")
        name=url.text
        file.write(str(num)+','+name+','+href+'\n')
    print("get success")

if __name__ == '__main__':
    file = open('url_list.csv', 'w')
    chrome_drive = '/Users/jiangxingqi/Sina/chromedriver'
    browser = webdriver.Chrome(executable_path=chrome_drive)
    browser.get('http://search.beijingip.cn/search/search/result?s=%E5%9F%BA%E5%9B%A0%E8%8A%AF%E7%89%87')
    browser.find_element_by_link_text('50').click()
    for page_no in range(1,273):
        print(page_no)
        fun(browser,file)
        # js = "window.scrollTo(10000,10000);"
        # browser.execute_script(js)
        browser.find_element_by_class_name('h_page').find_element_by_class_name('next').click()
    browser.close()
    file.close()