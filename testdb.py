#a temporary databse is created to check the functioning of db
"""TO BE DELETED AFTERWARDS"""
import sqlite3

con=sqlite3.connect(r'C:\Users\Deepak\PycharmProjects\bittorrent_service\Testfiles\serverdb\serve.db')
cursor= con.cursor()

def createtable():
    cursor.execute("CREATE TABLE IF NOT EXISTS filedetails(filename PRIMARY KEY NOT NULL, filepos TEXT NOT NULL, filesize integer )")

def addvalues(fileprop):
    cursor.execute("INSERT OR REPLACE INTO  filedetails(filename,filepos,filesize) VALUES (?, ?, ?)",[fileprop['name'],fileprop['path'],fileprop['size']])
    print 'value entry successful'

    con.commit()

createtable()
