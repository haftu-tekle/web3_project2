from ..util.util import hash256
class BlockHeader:
    def __init__(self, version, previousblockhash, timestamp, bits):
        self.version=version
        self.previousblockhash=previousblockhash
        self.timestamp=timestamp
        self.bits=bits
        self.Nonce=0
        self.blockhash=''
    def miner():
        return('your are the ownter')
    miner()
        