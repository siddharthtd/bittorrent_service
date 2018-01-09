# A basic model of splitting a file is drawn which would be later updated as per reqirement
#split a file into a set of portions which will be used by p2p application to determine which parts to be sent.
#These file once recived will be joint back to the original format



import os

def split(filepos, destpos,chunksize):
    partnum=0
    input = open(filepos, 'rb')         #use binary read mode to open the file
    while 1:
        chunk= input.read(chunksize)    #read only the chunksized amount of data in chunk variable
        if not chunk: break
        partnum=partnum+1               #increment partnum by 1 everytime a chunk is updated
        filename= os.path.join(destpos,('part%0d'% partnum)) #create a binary file called filename at destination directory
        fileobj=open(filename,'wb')     #open the file 'filename' in binary write mode
        fileobj.write(chunk)            #writh chunk data in the file
        fileobj.close()
    input.close()
    return partnum                       #return the number of parts that were generated

def main():

    filepos= raw_input('enter the postion of file to be split: ')
    destpos= raw_input('enter the position of destination folder: ')
    data_size = os.path.getsize(filepos) #geet size of data at file to be split
    chunksize = data_size / 4 #split file into 5 pieces

    try: parts= split(filepos,destpos,chunksize)
    except: print' error splitting'
    else: print ' split finished in: ', parts,' parts'

main()





