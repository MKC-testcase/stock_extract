import unittest
import psycopg2
from db_operations.PostgreSQL_analysis import db_interactions

class PostgreSQL_Test(unittest.TestCase):

    def test_connection(self):
        """This test Initial connection to the database"""
        """This test to see if a connection can be made to the database"""
        self.conn = psycopg2.connect(host="localhost", database="mdata", user="postgres", password="deus3stm4china")
        self.cur = self.conn.cursor()
        self.cur.execute('SELECT version()')
        id_check = self.cur.fetchone()
        self.assertEqual(id_check, ('PostgreSQL 12.1, compiled by Visual C++ build 1914, 64-bit',))
        self.conn.close()

    def test_class_interaction(self):
        """Tests the basic class functions in PostgreSQL_analysis"""
        self.new_class = db_interactions()
        self.new_class.query_version()
        db_version = self.new_class.get_fetchone()
        self.assertEqual(db_version,('PostgreSQL 12.1, compiled by Visual C++ build 1914, 64-bit',))

    def test_database_id(self):
        """ Tests sending string to Execute SQL function code"""
        self.new_class = db_interactions()
        self.new_class.execute_query("SELECT version()")
        db_version = self.new_class.get_fetchone()
        self.assertEqual(db_version, ('PostgreSQL 12.1, compiled by Visual C++ build 1914, 64-bit',))

    def test_execute_SQL(self):
        """ Tests sending string to Execute SQL function code other than collecting the version"""
        self.new_class = db_interactions()
        self.new_class.execute_query("SELECT type_of_currency FROM cnd_exchange_rate WHERE id = 3")
        db_version = self.new_class.get_fetchone()
        self.assertEqual(db_version, ('Canadian-Dollar Effective Exchange Rate Index (CERI)',))

    def test_get_fetch(self):
        """ Tests get_fetch function"""
        self.new_class = db_interactions()
        self.new_class.execute_query("SELECT type_of_currency FROM cnd_exchange_rate WHERE id = 3")
        db_version = self.new_class.get_fetch(1)
        self.assertEqual(db_version, [('Canadian-Dollar Effective Exchange Rate Index (CERI)',)])

    def test_get_fetch_optional(self):
        """ Tests get_fetch function"""
        self.new_class = db_interactions()
        self.new_class.execute_query("SELECT type_of_currency FROM cnd_exchange_rate WHERE id = 3")
        db_version = self.new_class.get_fetch()
        self.assertEqual(db_version, [('Canadian-Dollar Effective Exchange Rate Index (CERI)',)])

    def test_get_fetch_multiple(self):
        """ Tests get_fetch function for multiple entries"""
        self.new_class = db_interactions()
        self.new_class.execute_query("SELECT type_of_currency FROM cnd_exchange_rate WHERE id > 3 AND id < 6")
        db_version = self.new_class.get_fetch()
        self.new_class.print_db()
        self.assertEqual(db_version, [('Canadian-Dollar Effective Exchange Rate Index (CERI)',),('Canadian-Dollar Effective Exchange Rate Index (CERI)',)])

    def test_list_tables(self):
        """ Tests list table function and function calls from within the program"""
        self.new_class = db_interactions()
        content = self.new_class.list_tables()
        self.assertEqual(content, [('cnd_exchange_rate',), ('stock_data',)])

    def test_list_columns(self): #this function completely works even through test only go through 1 expected column name
        """ Tests list table function and function calls from within the program"""
        self.new_class = db_interactions()
        content = self.new_class.list_columns("cnd_exchange_rate")
        self.assertIn(('uom_id',),content)

    def test_connection(self):
        """
        self.new_class = db_interactions()
        self.cur.execute('SELECT version()')
        db_version = self.cur.fetchone() 
        self.assertEqual(db_version, "('PostgreSQL 12.1, compiled by Visual C++ build 1914, 64-bit',)")
        self.conn.close()


        """

if __name__ == '__main__':
    unittest.main()
