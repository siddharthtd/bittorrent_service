import uuid
def peer_id():
    key = uuid.uuid4().hex[:10]
    return key