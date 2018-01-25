#a temporary databse is created to check the functioning of db
#input: fileprop from listfilersPeer.py
#output: table
#DB store location to be altered according to needs
import sqlite3

con=sqlite3.connect(r'C:\Users\Deepak\PycharmProjects\bittorrent_service\Testfiles\serverdb\try41.db')
con.row_factory= lambda cursor,row:row[0]
cursor= con.cursor()
def createtable():
    cursor.execute("CREATE TABLE IF NOT EXISTS filedetails(peerid TEXT, filename TEXT NOT NULL UNIQUE , filesize integer )")

def addvalues(fileprop):
        cursor.execute("INSERT OR IGNORE INTO filedetails(peerid,filename,filesize) VALUES (?, ?, ?)",[fileprop['peerid'],fileprop['name'],fileprop['size']])
        print 'value entry successful'
        print ''
        print ''
        con.commit()

def checkvalues(fileprop):
    data=cursor.execute('SELECT peerid FROM filedetails').fetchall()

    if fileprop['peerid'] in data:
        print' peerid  present'
        return True
    else:
        return False

createtable()