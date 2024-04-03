#!/usr/bin/env python3
"""
Basic caching.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Inherits from BaseCaching and it's a caching system.
    """
    def put(self, key, item):
        """
        Inputs the key item pair to the cache_data dictionary.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Gets the item started at key in the cache_data dictionary.
        """
        return self.cache_data.get(key, None)
