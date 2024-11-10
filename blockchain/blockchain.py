import json
from pathlib import Path
from blockchain.block import Block


FILE = Path("data/blockchain.json")

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        previous_block = self.get_latest_block()
        new_block = Block(
            index=previous_block.index + 1, 
            previous_hash=previous_block.hash, 
            data=data
        )
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                print("Data has been tampered!")
                return False
            if current_block.previous_hash != previous_block.hash:
                print("Blockchain has been compromised!")
                return False
        return True

    def save_to_file(self, filename):
        FILE.write_text(json.dumps([block.to_dict() for block in self.chain]))

    @classmethod
    def load_from_file(cls, filename):
        chain_data = json.loads(FILE.read_text())
        blockchain = cls()
        blockchain.chain = [Block.from_dict(data) for data in chain_data]
        return blockchain
