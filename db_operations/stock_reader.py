#!/usr/bin/env python3

from selenium import webdriver
from time import sleep
import csv

class web_interaction():
    def __init__(self):
        self.rData = []
        self.csv_data = []

    def csv_extract(self, csv_name):
        i =0
        with open('{}'.format(csv_name), newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                for r_elem in row:
                    if i == 1:
                        self.csv_data.append(r_elem)
                    i = i+1
                i = 0

    def open_browser(self):
        self.browser = webdriver.Chrome('D:/Marcus/Python/Github_PG_cnd/PostgreSQL_cnd_exchange/db_operations/chromedriver')
        self.browser.get('https://ca.finance.yahoo.com/')

    def navigate_to_page(self, tick_name):
        search_bar = self.browser.find_element_by_name('yfin-usr-qry')
        search_bar.send_keys('{}'.format(tick_name))
        search_button = self.browser.find_element_by_id('search-button')
        search_button.click()

    def extract_left(self):
        """extracts the information from the left hand table on the Yahoo finance page"""
        for row in range(1, 9):
            try:
                xpath = '//table[@class="W(100%)"]/tbody/tr[{}]/td[2]'.format(row)
                elem = self.browser.find_element_by_xpath(xpath)
                self.rData.append(elem.text)
                print(elem.text)
            except:
                print("It appears that the company doesn't have all of the information usually provided, we have still saved the data that we have gathered")
                print("However this might cause values to be placed incorrectly, please make sure to double check")
                break

    def extract_right(self):
        """extracts the information from the right hand table on the Yahoo finance page"""
        for row in range(1, 9):
            try:
                xpath = '//table[@class="W(100%) M(0) Bdcl(c)"]/tbody/tr[{}]/td[2]'.format(row)
                elem = self.browser.find_element_by_xpath(xpath)
                self.rData.append(elem.text)
                print(elem.text)
            except:
                print(
                    "It appears that the company doesn't have all of the information usually provided, we have still saved the data that we have gathered")
                print("However this might cause values to be placed incorrectly, please make sure to double check")
                break

    def to_local(self):
        return self.rData

    def content_reset(self):
        """The purpose of this function is to reset the information for extraction"""
        self.rData = []

    def exit_browser(self):
        self.browser.quit()

if __name__ =='__main__':
    temp = web_interaction()
    temp.open_browser()
    temp.navigate_to_page('BCE')
    sleep(4)
    temp.extract_left()
    temp.extract_right()
    temp.exit_browser()