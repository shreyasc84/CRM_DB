import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Shresql'
)

cursorobject = database.cursor()

cursorobject.execute('CREATE DATABASE crmdb')

print('Done!')