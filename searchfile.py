# search directory used by seeder to search for the file on the disk in a particular directory

import os

def findfile(name,path):
    for root,dirs ,files in os.walk(path):
        if name in files or name in dirs:

            filepos= os.path.join(root,name)
            print'file found'
            return filepos
        else: return 'file not found'

    return


#returns the postion of the file in the directory

