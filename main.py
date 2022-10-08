import mysql.connector as mydb
#import sql_executer as sql_ec
import sqlalchemy as sa
import pandas as pd


def main():
    host='localhost'
    port='3306'
    user='root'
    password='rootpass'
    database='test'

    url = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8'
    engine = sa.create_engine(url, echo=False)
    
    sql_query = "select * from user_body_temperature;"
    df = pd.read_sql(sql_query, con=engine)
    print(df)
    
    '''
    ec=sql_ec.sql_executor()
    tf = ec.connect(host, port, user, password, database)
    
    sql_query='show databases;'
    tf, ret = ec.execute(sql_query)
    print(ret)
    print('')

    sql_query = 'select * from test.user_body_temperature;'
    tf, ret = ec.execute(sql_query)
    print(ret)
    print('')
    '''
    
    """
    print('hello')
    conn = mydb.connect(
        host='localhost',
        port='3306',
        user='root',
        password='rootpass',
        database='test'
    )
    cur = conn.cursor()

    sql_query = 'show tables;'
    ret = cur.execute(sql_query)
    print(ret)
    print('')
    
    #sql_query = 'show databases;'
    #sql_query = 'select * from test.user_body_temperature;'
    #ret = cur.execute(sql_query)
    sql_query='show databases;'
    ret = cur.execute(sql_query)
    print(ret)
    print('')
    """
    

main()
