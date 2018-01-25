"""Input 1: file directory path from where list of all files present are to be gathered"""
"""Input Link 1: Unique peer id from peer_id_gen to develop unique peer id """
"""Output Link 1: Output send to testdb.py to add data( peerid, name and size) to table , check for peerid duplicates.
    Output being fileprop(peerid,filename,filesize)"""
"""Main() module to be edited"""
import os
import testdb
import peer_id_gen

#filedetails method takes input directory path.crates a dictionary containing peerid,
# filename and filesize of each files in the directory.
#The dictinary is fowared to checkresults to chec whether the duplicate entry of perrid.
#The random peerid is generated in peer_id_gen class
def filedetails(path):
    dir= os.listdir(path)
    fileprop= {'name':'','peerid': '','size':''}
    result =testdb.checkvalues(fileprop)
    if (result== False):
        print 'generating new file details section'
        peerid= peer_id_gen.peer_id()
        print ' peer id gen method getting executed'
        for files in dir:
            filepos = os.path.join(path, files)
            filesize = os.path.getsize(filepos)  # get file size
            filesize = filesize / 1024  # convert into KB

            fileprop.update({'name': files, 'peerid': peerid, 'size': filesize})
            checkresult(fileprop,files)
    return

#this module checks for duplecate entry of peer id by comparing
#it with the peerid entries in the db . If duplicate entry found, generate a new peerid
#else send peerid , filename and filesize to database.
#testdb.checkvalues returns true if dupicate entry present in database. The code retrives true or false
# by calling testdb.checkvalues() module and stores data in db by calling testdb.checkvalues() module
def checkresult(fileprop,files):

            print ' check results executing'
            result = testdb.checkvalues(fileprop)
            while (result== False):
                print'new peer id accepted'
                testdb.addvalues(fileprop)
                return

            while (result== True):
                print ' new id to be created'
                peerid=peer_id_gen.peer_id()
                filesize=fileprop['size']
                fileprop.update({'name': files, 'peerid': peerid, 'size': filesize})
                testdb.checkvalues(fileprop)
                checkresult(fileprop,files)
                return




def  main():
    path = r'C:\Users\Deepak\PycharmProjects\bittorrent_service\Testfiles'
    filedetails(path)
main()



