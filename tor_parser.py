import bencode, sys, hashlib, binascii
def tor_parser(file_path):
    torr_file = open(file_path, "rb")
    try:
        content = bencode.bdecode(torr_file.read())
    except:
        print ("Read Failed, Please select a valid torrent file")
        sys.exit(torr_file)
    info = content['info']
    piece_length = info['piece length']
    pieces = info['pieces']
    announce = content['announce']
    if 'announce-list' in content:
        announce_list = content['announce-list']
    else:
        announce_list = None
    if 'name' in info:
        tor_name = info['name']
    else:
        tor_name = None
    if 'length' in info:
        length = info['length']
    else:
        length = None
    if 'files' in info:
        files = info['files']
    else:
        files = []
    infohash = hashlib.sha1(bencode.bencode(info)).hexdigest()
    piecehashes = [binascii.hexlify(pieces[i:i + 20]) for i in range(0, len(pieces), 20)]
    torrent_size = 0

    for i in files:
        torrent_size += i['length']
        for j in range(len(i['path'])):
            i['path'][j] = unicode(i['path'][j], "utf8")
    if torrent_size == 0:
        torrent_type = 'single file torrent'
        torrent_size = length
    else:
        torrent_type = 'multiple file torrent'
    last_piece_size = (len(piecehashes) * piece_length) - torrent_size
    last_piece_percent = '{:.1%}'.format(float(last_piece_size) / piece_length)
    print ("piece_length:{0}\n announce:{1}\n announce_list:{2}\n, tor_name:{3}\n, length:{4}\n, torrent_type:{5}\n, infohash:{6}\n, last_piece_percent:{7}\n".format(piece_length, announce, announce_list, tor_name, length, torrent_type, infohash, last_piece_percent))

tor_parser('/Users/leovince/PycharmProjects/bittorrent_service/The_Motivation.torrent')