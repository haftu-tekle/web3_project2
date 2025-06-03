import hashlib

def hash256(s):
    ''''make the SHA56 2 round '''
    return hashlib.sha256(hashlib.sha256(s).digest()).digest()

