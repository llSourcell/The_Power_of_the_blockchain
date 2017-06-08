import hashlib
from . import block_params


class Block():

    def __init__(self, params):
        self.index = params.index
        self.previous_hash = params.previous_hash
        self.timestamp = params.timestamp
        self.data = params.data
        self.hash = self.calc_hash()

    def params(self):
        return block_params.BlockParams(
            self.index,
            self.previous_hash,
            self.timestamp,
            self.data
        )

    @classmethod
    def genesis_block(cls):
        params = block_params.BlockParams.genesis_params()
        return cls(params)

    def calc_hash(self):
        return hashlib.sha256(str(self.params()).encode()).hexdigest()

    def has_valid_index(self, previous_block):
        return self.index == previous_block.index + 1

    def has_valid_previous_hash(self, previous_block):
        return self.previous_hash == previous_block.hash

    def has_valid_hash(self):
        return self.calc_hash() == self.hash
