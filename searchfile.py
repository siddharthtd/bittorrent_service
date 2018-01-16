# search directory used by seeder to search for the file on the disk in a particular directory

import os

def findfile(name,path):
    for root,dirs ,files in os.walk(path):
        if name in files or name in dirs:

            filepos= os.path.join(root,name)


        else: return 'file not found'

    return
def fileprop(filepos):
    for files in dir:
        filepos= os.path.join(path,files)
        filesize=os.path.getsize(filepos)
        filesize= filesize/1023
        print filepos
        print filesize
        return filepos, filesize

#returns the postion of the file in the directory
findfile('Projects', 'C:\Users\Deepak\Google Drive')