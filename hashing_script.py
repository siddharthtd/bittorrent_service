import hashlib
def hashing_script(path):
    opened = open(path)
    readfile = opened.read()
    hash = hashlib.sha1(readfile)
    sha = hash.hexdigest()
    print ("File Name: {}".format(path))
    print ("SHA1: {}".format(sha))
    opened.close()
    return sha
