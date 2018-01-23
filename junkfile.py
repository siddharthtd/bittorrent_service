import os
import testdb
import peer_id_gen


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









