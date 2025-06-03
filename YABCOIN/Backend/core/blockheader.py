from YABCOIN.Backend.util.util import hash256
class BlockHeader:
    def __init__(self, version, previousblockhash, timestamp, bits):
        self.version=version
        self.previousblockhash=previousblockhash
        self.timestamp=timestamp
        self.bits=bits
        self.Nonce=0
        self.blockhash=''
print('Block run successfully')

def miner(self):
    while (self.blockhash[0:4]) != '0000':
        self.blockhash=hash256(str(self.version) + self.previoushash +str(self.timestamp)
                               + str(self.Nonce).encode()).hex()