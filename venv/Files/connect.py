#!/usr/bin/python


import mysql.connector
from mysql.connector import MySQLConnection, CMySQLConnection, errorcode

cnx = mysql.connector.connect(user='root', password='123',
 host='127.0.0.1',
 database='baufuchs')

cnx.close()

try:
    cnx = mysql.connector.connect(user='root', host='127.0.0.1',
                                  password='123', database='baufuchs')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()
