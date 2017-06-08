import unittest
from .. import block
from .. import block_params


class TestBlock(unittest.TestCase):

    def test_has_valid_index(self):
        prev_block = create_block(0, '0', 1, 'first_block')

        with self.subTest('valid index'):
            new_block = create_block(1, '0', 1, 'second block')
            self.assertTrue(new_block.has_valid_index(prev_block))

        with self.subTest('invalid index'):
            new_block = create_block(2, '0', 1, 'second block')
            self.assertFalse(new_block.has_valid_index(prev_block))

    def test_has_valid_previous_hash(self):
        prev_block = create_block(0, '0', 1, 'first_block')
        prev_hash = prev_block.hash

        with self.subTest('valid previous hash'):
            new_block = create_block(1, prev_hash, 1, 'second block')
            self.assertTrue(new_block.has_valid_previous_hash(prev_block))

        with self.subTest('invalid previous hash'):
            new_block = create_block(2, '0', 1, 'second block')
            self.assertFalse(new_block.has_valid_previous_hash(prev_block))

    def test_has_valid_hash(self):
        with self.subTest('valid hash'):
            new_block = create_block(1, '0', 1, 'second block')
            self.assertTrue(new_block.has_valid_hash())

        with self.subTest('invalid hash'):
            new_block = create_block(2, '0', 1, 'second block')
            new_block.hash = 'invalidhash'
            self.assertFalse(new_block.has_valid_hash())


def create_block(index, previous_hash, timestamp, data):
    params = block_params.BlockParams(
        index, previous_hash, timestamp, data)
    return block.Block(params)

if __name__ == '__main__':
    unittest.main()
