import os



#********************************************************************************************************************
#SPLIT FILE
#input required : filepos, chunksize

# A basic model of splitting a file is drawn which would be later updated as per reqirement
#split a file into a set of portions which will be used by p2p application to determine which parts to be sent.
#These file once recived will be joint back to the original format



def splitfile():#filepos, destpos,chunksize):
    filepos = raw_input('enter the postion of file to be split: ')
    destpos = '/home/deepak/PycharmProjects/bittorrent_service/splits'
    data_size = os.path.getsize(filepos)  # geet size of data at file to be split
    chunksize = data_size / 4  # split file into 5 pieces

    try:
        partnum = 0
        input = open(filepos, 'rb')  # use binary read mode to open the file
        while 1:
            chunk = input.read(chunksize)  # read only the chunksized amount of data in chunk variable
            if not chunk: break
            partnum = partnum + 1  # increment partnum by 1 everytime a chunk is updated
            filename = os.path.join(destpos, ('part%0d' % partnum))  # create a binary file called filename at destination directory
            fileobj = open(filename, 'wb')  # open the file 'filename' in binary write mode
            fileobj.write(chunk)  # writh chunk data in the file
            fileobj.close()
        input.close()

        print ' split finished in: ', partnum, ' parts'
        return

    except:
        print' error splitting'
        return

#*********************************************************************************************************************


#JOIN FILE
#INPUTS REQUIRED: FILENAME TO BE JOINT

#a basic model of joining a multiple splitted file back to the original format
def joinfile():#destfile):
    fromdir = '/home/deepak/PycharmProjects/bittorrent_service/splits'
    filename = 'filename'
    destfile = '{0}.zip'.format(filename)
    try:
        readsize = 1023  # set readsize to 1byte
        outputfile = open(destfile, 'wb')  # open a file with desired name in binary write mocde
        parts = os.listdir(fromdir)  # get the list of all files from the directory to be joint
        parts.sort()  # and sort them in correect order
        for filename in parts:
            filepath = os.path.join(fromdir, filename)  # create a directory
            fileobj = open(filepath, 'rb')  # open the file in that directory in biinary read mode
            while 1:
                filesizebytes = fileobj.read(readsize)  # read data from  the parts at 1023 bits per read. This is done to prevent memory congestion
                if not filesizebytes: break
                outputfile.write(filesizebytes)  # write the data in the named file
            fileobj.close()
        outputfile.close()
    except:
        print'join failed'
    else:
        print 'join complete'


    #deleting the split files created during the file sharing after joining them.
    fileList = os.listdir(fromdir)
    for fileName in fileList:
        os.remove(fromdir + "/" + fileName)
    print' directory deleted'

    return

#*****************************************************************************************************************