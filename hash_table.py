"""
Module: hash_table
Purpose: Build a hash table. The hashing function will sum the Unicode values of each character in the key.

"""

__author__ = "Juliana Albertyn"
__email__ = "julie_albertyn@yahoo.com"
__status__ = "development"  # or testing or production
__date__ = "2026-01-07"


from typing import Any


class HashTable:
    """
    Build a hash table.

    Attributes:
    collection (dict) : the hash table
    """

    def __init__(self) -> None:
        """Initialises an instance of the hash table"""
        self.collection = dict()

    def hash(self, key: str) -> int:
        """Sum the Unicode values of each character in the key."""
        result = 0
        for c in key:
            result += ord(c)
        return result

    def add(self, key: str, value: Any) -> None:
        """Add a key:value pair to the hash table."""
        hashed_key = self.hash(key)
        if hashed_key not in self.collection:
            self.collection[hashed_key] = dict()
        self.collection[hashed_key][key] = value

    def remove(self, key: str) -> None:
        """Remove the hash table entry with the specified key."""
        hashed_key = self.hash(key)
        if hashed_key in self.collection.keys():
            self.collection[hashed_key].pop(key, None)

    def lookup(self, key: str) -> Any:
        """Look up the value for a key"""
        hashed_key = self.hash(key)
        if hashed_key in self.collection.keys():
            return self.collection[hashed_key].get(key, None)


if __name__ == "__main__":
    ht = HashTable()
    print(f'hash: {ht.hash("golf")}')
    ht.add("golf", "sport")
    print(ht.lookup("golf"))
    print(ht.collection)
    print(f'hash: {ht.hash("dear")}')
    ht.add("dear", "friend")
    print(f'hash: {ht.hash("read")}')
    ht.add("read", "book")
    print(ht.collection)
    ht.remove("dear")
    print(ht.collection)
    ht.remove("golf")
    print(ht.lookup("golf"))
    print(f'hash: {ht.hash("rose")}')
    ht.add("rose", "flower")
    ht.add("fcc", "coding")
    ht.add("cfc", "chemical")
    print(ht.collection)
