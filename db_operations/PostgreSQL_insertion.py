#!/usr/bin/env python3
# #By Marcus Chan
#Last Updated 2020-08-20
#Required Libraries: psycopg2, PostgreSQL_analysis.py
#Purpose:To create a conviennient wrapper for psycopg2 and create a few other functions to interact with inserting things
#       from the database

import psycopg2
from db_operations.PostgreSQL_analysis import db_interactions

#this entire class is untested however the insert help should owork based on test results of the other .py file
class db_insert:
    """This class is used for helping with inserting data into the database"""
    def __init__(self):
        self.db_extract = db_interactions()

    def insert_help(self):
        """Creates guide to help the user see and interact with directing insertions into the database"""
        possible_tables = self.db_extract.list_tables()
        for tables in possible_tables:
            print(tables)
            print("\n")
        table_name = input("Now please enter the table you have chosen")
        try:
            possible_columns = self.db_extract.list_columns(table_name)
        except ValueError:
            print("Table not found unable to proceed")
        for column in possible_columns:
            print(column)
            print("\n")

    def data_clean(self, string):
        """this function clears away any special characters from the string leaving the spaces"""


    def auto_insert(self,table, columns, values):
        """this function should automatically help the user place their values into the PostgreSQL database"""
        columnstring = ""   #holds column format
        valuesstring = ""   #holds values format
        x = 0
        y =0
        columnstring = ", ".join(columns)
        x = len(columns)
        valuesstring = """', '""".join(values)
        valuesstring = """'""" + valuesstring + """'"""
        y = len(values)
        if x == y:
            print(table)
            sql_string = "INSERT INTO {table_name} ({columns}) VALUES ({values});".format(table_name = table,columns = columnstring, values = valuesstring)
            print(sql_string)
            print("Executing Query")
            self.db_extract.execute_query(sql_string) # executes the insertion based on the string created above
        else:
            print("The number of columns and value do not match")

    def delete_recent(self):
        """idea to reverse the changes just made on the database incase of error (database time log?) last 5 mins?"""
        print("Placeholder")

def main():
    test = db_insert()

if __name__ == '__main__':
    main()