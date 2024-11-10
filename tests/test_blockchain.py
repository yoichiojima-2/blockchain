from blockchain.blockchain import Blockchain


def test_blockchain():
    blockchain = Blockchain()

    blockchain.add_block("First Block after Genesis")
    blockchain.add_block("Second Block after Genesis")
    blockchain.add_block("Third Block after Genesis")

    for block in blockchain.chain:
        print(f"Block {block.index}: {block.data}")
        print(f"Hash: {block.hash}")
        print(f"Previous Hash: {block.previous_hash}\n")

    assert blockchain.is_chain_valid()