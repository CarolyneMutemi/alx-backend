#!/usr/bin/python3
"""
LRU Caching.
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Caching system that uses LRU caching.
    """
    def __init__(self):
        super().__init__()
        self.check_age = {}
        self.age = 0

    def put(self, key, item):
        """
        Inputs the key item pair to the cache_data dictionary.
        """
        if key and item:
            sorted_keys = sorted(self.check_age,
                                 key=lambda k: self.check_age[k])
            len_dict = len(self.cache_data)
            if len_dict == self.MAX_ITEMS and key not in self.cache_data:
                k = sorted_keys[0]
                self.cache_data.pop(k)
                self.check_age.pop(k)
                print(f"DISCARD: {k}")
            self.cache_data[key] = item
            self.age += 1
            self.check_age[key] = self.age

    def get(self, key):
        """
        Gets the item started at key in the cache_data dictionary.
        """
        if key in self.cache_data:
            self.age += 1
            self.check_age[key] = self.age
        return self.cache_data.get(key, None)
