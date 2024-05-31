#!/usr/bin/env python3
""" 1-fifo_cache """

from collections import OrderedDict
from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Assign to the dictionary `self.cache_data` the `item` value
        """
        if key is None or item is None:
            return
        
        # Check if the cache already contains the key
        if key in self.cache_data:
            # Remove the old key to update its position later
            del self.cache_data[key]
        
        # If the cache is full, remove the first item
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            firstKey, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {firstKey}")
        
        # Add the new key-value pair to the cache
        self.cache_data[key] = item

    def get(self, key):
        """
        Return the value in `self.cache_data` linked to `key`
        """
        return self.cache_data.get(key, None)
