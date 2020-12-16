"""
By: Marcus Chan
The purpose of this file is to act as a main function and to work with all python file in the package thus far
"""
import psycopg2
from db_operations.PostgreSQL_analysis import db_interactions
from db_operations.PostgreSQL_insertion import db_insert
from db_operations.stock_reader import web_interaction
from time import sleep

column_names = ["previous_close", "open", "bid", "ask", "day_range", "weeks52", "volume", "avg_volume", " market_cap", "monthly5y", "pe_ratio", "eps", "earn_date", "forward_div_yield", "exdiv_date", "t_estimate"]
yf_reader = web_interaction()   #creates the object to interact with the functions in stock_reader
data_insert = db_insert()
query_exe = db_interactions()

#opens the csv file and sets it to web_interaction interal variable
yf_reader.csv_extract("D:\\Marcus\\Python\\Github_PG_cnd\\test_file.csv")

#this tests if the elements extracted are in the second row(TESTED)
for elem in yf_reader.csv_data:
    print(elem)
ticker_data = []

yf_reader.open_browser() #opens browser, yahoo finance

#loading the results from csv data into the rest of the web_interaction functions
for elem in yf_reader.csv_data:
    yf_reader.navigate_to_page(elem) #browser to indicate webpage
    sleep(6) #allows time for webpage to load
    yf_reader.extract_left() #gets the information from the leftside table
    yf_reader.extract_right() #gets information from the rightside table
    ticker_data.append(yf_reader.to_local()) #copies the information from internal variable to local list
    yf_reader.content_reset() #resets internal variable to empty list

#exits the browser to continue the program
yf_reader.exit_browser()#exits the browser

#turns the data collected into a string to execute
for in_elem in ticker_data:
    data_insert.auto_insert("stock_data", column_names, in_elem)
