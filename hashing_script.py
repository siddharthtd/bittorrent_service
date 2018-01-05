import hashlib

def hashing_script(test):
    opened = open(test)
    readfile = opened.read()

    hash = hashlib.sha1(readfile)
    sha1hashed = hash.hexdigest()

    print ("File Name: {}".format(test))
    print ("SHA1: {}".format(sha1hashed))
    opened.close()
    return sha1hashed
