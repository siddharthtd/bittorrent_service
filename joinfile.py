#a basic model of joining a multiple splitted file back to the original format


import os

def joinfile(fromdir,destfile):
     readsize=1023 #set readsize to 1byte
     outputfile=open(destfile, 'wb') #open a file with desired name in binary write mocde
     parts= os.listdir(fromdir) #get the list of all files from the directory to be joint
     parts.sort() # and sort them in correect order
     for filename in parts:
         filepath= os.path.join(fromdir,filename) #create a directory
         fileobj= open(filepath,'rb') #open the file in that directory in biinary read mode
         while 1:
             filesizebytes=fileobj.read(readsize) #read data from  the parts at 1023 bits per read. This is done to prevent memory congestion
             if not filesizebytes: break
             outputfile.write(filesizebytes) #write the data in the named file
         fileobj.close()
     outputfile.close()

def main():
    fromdir= raw_input('enter the directory from where file has to be joined: ')
    destfile=raw_input('name of the file to be created: ')
    try: joinfile(fromdir,destfile)
    except: print'join failed'
    else: print 'join complete'

main()

