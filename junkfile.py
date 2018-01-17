
#getting list of all the files in the directory and returning filename, path and size of the file in the disctionary format
#input : Path of file on the system. doesn't work with finding directory
#return: disctionary 'filedetails'

import os
import testdb

def filedetails(path):
    dir = os.listdir(path) #get list of all files from path
    fileprop={'name':'','path':'','size':''}

    for files in dir:
        filepos= os.path.join(path,files)
        filesize=os.path.getsize(filepos) #get file size
        filesize= filesize/1024 #convert into KB

        fileprop.update({'name':files,'path':filepos,'size':filesize})
        print fileprop
        testdb.addvalues(fileprop)
        print 'done'


    return




def main():
    path = r'C:\Users\Deepak\PycharmProjects\bittorrent_service\Testfiles'
    filedetails(path)

main()