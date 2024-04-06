#!/usr/bin/python3
"""
MRU Caching.
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Uses MRU algorithm for caching.
    """
    def __init__(self):
        super().__init__()
        self.checker = {}
        self.age = 0

    def put(self, key, item):
        """
        Inputs the key item pair to the cache_data dictionary.
        """
        if key and item:
            limit = len(self.cache_data) == self.MAX_ITEMS
            if limit and key not in self.cache_data:
                most_recent = max(sorted(self.checker,
                                         key=lambda k: self.checker[k]),
                                  key=lambda k: self.checker[k])
                self.cache_data.pop(most_recent)
                self.checker.pop(most_recent)
                print(f"DISCARD: {most_recent}")
            self.cache_data[key] = item
            self.age += 1
            self.checker[key] = self.age

    def get(self, key):
        """
        Gets the item at key in the cache_data dictionary.
        """
        if key in self.cache_data:
            self.age += 1
            self.checker[key] = self.age
        return self.cache_data.get(key, None)
