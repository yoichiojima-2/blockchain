import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None, hash=None):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp or time.time()
        self.data = data
        # Use provided hash or calculate it if it's a new block
        self.hash = hash or self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def to_dict(self):
        # Return a dictionary with only serializable data
        return {
            "index": self.index,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "data": self.data,
            "hash": self.hash
        }

    @classmethod
    def from_dict(cls, block_data):
        # Create a Block instance from a dictionary
        return cls(
            index=block_data["index"],
            previous_hash=block_data["previous_hash"],
            data=block_data["data"],
            timestamp=block_data["timestamp"],
            hash=block_data["hash"]
        )