#!/usr/bin/python3
"""
LFU caching.
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Uses the LFU algorithm for caching.
    """
    def __init__(self):
        super().__init__()
        self.LRUChecker = {}
        self.frequency = {}
        self.age = 0

    def put(self, key, item):
        """
        Inputs the key item pair to the cache_data dictionary.
        In case limit is reached the least frequently used data
        is removed.
        In case more than one instance is found LRU algorithm is used
        to narrow that down to one.
        """
        if key and item:
            limit = len(self.cache_data) == self.MAX_ITEMS
            if limit and key not in self.cache_data:
                least = min(sorted(self.frequency,
                                       key=lambda k: self.frequency[k]),
                                key=lambda k: self.frequency[k])
                least_frequent = [k for k in self.frequency
                                  if self.frequency[k]
                                  == self.frequency[least]]
                least_recent = min(sorted(
                    {k:v for k, v in self.LRUChecker.items()
                     if k in least_frequent},
                     key=lambda k: self.LRUChecker[k]),
                     key=lambda k: self.LRUChecker[k])
                if len(least_frequent) > 1:
                    discard = least_recent
                else:
                    discard = least_frequent[0]
                self.LRUChecker.pop(discard)
                self.frequency.pop(discard)
                self.cache_data.pop(discard)
                print(f"DISCARD: {discard}")
            if key not in self.cache_data:
                self.frequency[key] = 1
            else:
                self.frequency[key] += 1
            self.age += 1
            self.LRUChecker[key] = self.age
            self.cache_data[key] = item

    def get(self, key):
        """
        Gets the item at key in the cache_data dictionary.
        """
        if key in self.cache_data:
            self.age += 1
            self.LRUChecker[key] = self.age
            self.frequency[key] += 1
        return self.cache_data.get(key, None)
