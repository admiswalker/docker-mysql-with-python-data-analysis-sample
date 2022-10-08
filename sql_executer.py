import sys
import mysql.connector as mydb
import pandas as pd


class sql_executor:
    
    def __init__(self):
        pass
    
    def __del__(self):
        pass

    def connect(self, host_in, port_in, user_in, password_in, database_in):
        try:
            self.conn = mydb.connect(
                host=host_in,
                port=port_in,
                user=user_in,
                password=password_in,
                database=database_in
            )
        except Exception as err:
            print('sql_excutor: connect() is failed:', err, file=sys.stderr)
            return False
        
        self.conn.ping(reconnect=True)
        return True

    def is_connected(self):
        try:
            res = self.conn.is_connected()
        except Exception as err:
            print('sql_excutor: is_connected() is failed:', err, file=sys.stderr)
            return False
        
        return res

    def execute(self, sql_query):

        # normal
        '''
        cur = self.conn.cursor()
        
        try:
            cur.execute(sql_query)
            res = cur.fetchall()
        except Exception as err_msg:
            print('[Table Create Error]', err_msg, file=sys.stderr)
            return False, str(err_msg) # convert 'mysql.connector.errors.ProgrammingError' type to str() type
        '''
        
        # when requiring pandas dataframe for the output
        df_read = pd.read_sql(sql_query, self.conn)
        res = df_read.head()
        
        return True, res

