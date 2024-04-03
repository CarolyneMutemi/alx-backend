#!/usr/bin/env python3
"""
LIFO caching.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Caching system that implements LIFO system.
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_data = OrderedDict(self.cache_data)

    def put(self, key, item):
        """
        Inputs the key item pair to the cache_data dictionary.
        Discards the last inserted item if items exceed the MAX_ITEMS.
        """
        if key and item:
            if len(self.cache_data) == self.MAX_ITEMS \
                    and key not in self.cache_data:
                discarded = self.cache_data.popitem()[0]
                print(f"DISCARD: {discarded}")
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)

    def get(self, key):
        """
        Gets the item started at key in the cache_data dictionary.
        """
        return self.cache_data.get(key, None)
