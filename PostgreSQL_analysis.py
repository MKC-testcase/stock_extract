#!/usr/bin/env python3
#By Marcus Chan
#Last Updated 2020-08-20
#Required Libraries: psycopg2
#Purpose:To create a conviennient wrapper for psycopg2 and create a few other functions to interact with observing things
#       from the database

import psycopg2

class db_interactions:
    """ This class will be used to control the interactions between a PostgreSQL or not"""
    def __init__(self):
        self.db_content = []
        try:
            self.conn = psycopg2.connect(host="localhost", database="mdata", user="postgres", password="deus3stm4china")
            self.cur = self.conn.cursor()
        except Exception as exc:
            print('Error: {} exception raised by connection request'.format(exc))
            raise

    def SQL_command_builder(self):
        """The purpose of this function is to offer to Create SQL command easily"""

    def execute_query(self, command):
        try:
            self.cur.execute(command)
            self.conn.commit()
            print('Finished Executing Query')
        except ValueError:
            print("An incorrect SQL command was given Please Try Again")

    def query_version(self):
        """Base query to test initial connection"""
        self.cur.execute('SELECT version()')

    def print_db(self):
        """prints everythings that has been collected - as easy check"""
        for i in self.db_content:
            print(i)

    def list_tables(self):
        """This function lists the table names of the database (used in PostgreSQL_insertion.py)"""
        # THIS STILL NEEDS A TESTCASE(unittest)
        command1 = """SELECT tablename
                    FROM pg_catalog.pg_tables
                    WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';"""
        try:
            self.execute_query(command1)
            db_content = self.get_fetch()
            return db_content
        except ValueError:
            print("There was an error in selecting the table name of the database returning empty list")
            temp_list = []
            return temp_list

    def list_columns(self, table_name):
        """This function lists the column names of the table selected (used in PostgreSQL_insertion.py)"""
        #THIS STILL NEEDS A TESTCASE(unittest)
        command2 = """SELECT column_name
                    FROM information_schema.columns
                    WHERE table_schema = 'public' AND table_name = '{}'""".format(table_name)
        try:
            self.execute_query(command2)
            db_content = self.get_fetch()
            return db_content
        except ValueError:
            print("There was an error in selecting the table name of the database returning empty list")
            temp_list = []
            return temp_list

#New structure for fetch, have 1 fetchas that does all the other fetch when other input given, if no input fetch all
    def get_fetch(self, *args, **kwargs): # *args checks for any number of inputs afterwards the self, and ** kwargs represents the option input
        """implementation of variable fetches(one, many or all) """
        collect = kwargs.get('collect', None) #this just checks if the variable written in is collect
        # (if nothing is written then assumed it is collect)
        try:
            if collect == None:
                self.db_content = self.cur.fetchall()
                return self.db_content
            elif collect != None:
                self.db_content = self.cur.fetchmany(collect)
                return self.db_content
        except ValueError:
            print("You have entered a non supported variable for this function. User a Number next time")

    def get_fetchone(self):
        """collects 1 of the results of the query"""
        self.db_content = self.cur.fetchone()
        return self.db_content

    def get_fetchall(self):
        """collects all of the results of the query"""
        self.db_content = self.cur.fetchall()
        return self.db_content

    def __enter__(self):
        """hopefully when this class is called it will automatically use this after the __init__"""
        try:
            self.conn = psycopg2.connect(host="localhost", database="mdata", user="postgres", password="deus3stm4china")
            self.cur = self.conn.cursor()
        except Exception as exc:
            print('Error: {} exception raised by connection request'.format(exc))
            raise

    def __exit__(self):
        """This function closes the database after object is used"""
        self.conn.close()

class db_analysis:
    def __init__(self):
        inter = db_interactions()

def main():
    test = db_interactions()

if __name__ == '__main__':
    main()