#a temporary databse is created to check the functioning of db
"""TO BE DELETED AFTERWARDS"""
import sqlite3
import json
import peer_id_gen


con=sqlite3.connect(r'C:\Users\Deepak\PycharmProjects\bittorrent_service\Testfiles\serverdb\try14.db')
con.row_factory= lambda cursor,row:row[0]
cursor= con.cursor()
def createtable():
    cursor.execute("CREATE TABLE IF NOT EXISTS filedetails(peerid TEXT  , filename TEXT , filesize integer )")

def addvalues(fileprop):

        cursor.execute("INSERT OR REPLACE INTO filedetails(peerid,filename,filesize) VALUES (?, ?, ?)",[fileprop['peerid'],fileprop['name'],fileprop['size']])
        print 'value entry successful'
        con.commit()

def checkvalues(fileprop):
    con.row_factory= lambda cursor,row:row[0:1]
    data=cursor.execute('SELECT peerid AND filename FROM filedetails').fetchall()
    if fileprop['peerid'] and fileprop['name']in data:
        if fileprop['peerid'] in data:
            return True
    else:
        return False


createtable()