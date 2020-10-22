import mysql.connector as mysql

base_url = 'https://core.ac.uk:443/api-v2/'

class SQL_Base(object):
    def __init__(self, host, user, password, database):
        try:
            self.connection = mysql.connect(host, user, password, database)
        except mdb.Error as e:
            print("Init error %d: %s" % (e.args[0], e.args[1]))

    def __execute(self, query, parameters=[]):
        try:
            with self.connection:
                cursor = self.connection.cursor()
                cursor.execute(query, parameters)
                return cursor
        except mdb.Error as e:
            print("Execute error %d: %s" % (e.args[0], e.args[1]))
 
    def __select(self, query, parameters):
        return self.__execute(query, parameters)
   
    def execute(self, query, parameters=[]):
        return self.__execute(query, parameters).rowcount
 
    def select_all(self, query, parameters=[]):
        cursor = self.__select(query, parameters)
        return cursor.fetchall()
   
    def select_one(self, query, parameters=[]):
        cursor = self.__select(query, parameters)
        return cursor.fetchone()
   
    def dispose(self):
        if self.connection:
            self.connection.close()
