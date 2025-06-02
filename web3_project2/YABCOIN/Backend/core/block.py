class Block:
    def __init__(self, height, blocksize,blockheader, txs, txscount):
        self.height=height
        self.blocksize=blocksize
        self.blockheader=blockheader
        self.txs=txs
        self.txscount=txscount