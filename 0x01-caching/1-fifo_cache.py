#!/usr/bin/env python3
"""
FIFO caching.
"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """
    Caching system that implements FIFO system.
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_data = OrderedDict(self.cache_data)

    def put(self, key, item):
        """
        Inputs the key item pair to the cache_data dictionary.
        Discards the first inserted item if items exceed the MAX_ITEMS.
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                discarded = self.cache_data.popitem(last=False)[0]
                print(f"DISCARD: {discarded}")

    def get(self, key):
        """
        Gets the item started at key in the cache_data dictionary.
        """
        return self.cache_data.get(key, None)
