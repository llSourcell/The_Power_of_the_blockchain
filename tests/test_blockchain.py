import unittest
from unittest.mock import MagicMock
from .. import blockchain


class TestBlockChain(unittest.TestCase):

    def test_generate_new_block(self):
        bc = blockchain.BlockChain()
        old_bc_length = len(bc.blockchain_store)

        data = 'this is new block'

        with self.subTest('add new block to blockchain'):
            bc.generate_next_block(data)
            self.assertEqual(len(bc.blockchain_store) - old_bc_length, 1)
            self.assertEqual(bc.latest_block().data, data)

    def test_receive_blockchain(self):
        bc = blockchain.BlockChain()
        old_bc_lengh = len(bc.blockchain_store)

        prev_block = MagicMock()
        new_block = MagicMock()
        with self.subTest('valid block should be added to blockchain'):
            new_block.has_valid_index = MagicMock(return_value=True)
            new_block.has_valid_previous_hash = MagicMock(return_value=True)
            new_block.has_valid_hash = MagicMock(return_value=True)

            bc.blockchain_store = [prev_block]
            bc.receive_new_block(new_block)
            self.assertEqual(len(bc.blockchain_store) - old_bc_lengh, 1)

        with self.subTest('invalid block shoud not be added to blockchain'):
            new_block.has_valid_index = MagicMock(return_value=False)
            new_block.has_valid_previous_hash = MagicMock(return_value=False)
            new_block.has_valid_hash = MagicMock(return_value=False)

            bc.blockchain_store = [prev_block]
            bc.receive_new_block(new_block)
            self.assertEqual(len(bc.blockchain_store) - old_bc_lengh, 0)



