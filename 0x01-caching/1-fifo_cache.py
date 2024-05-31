#!/usr/bin/env python3
""" 1-fifo_cache 1-main  """


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
        assign to the dictionary `self.cache_data` the `item` value
        """

        if key is None or item is None:
            return None

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            firstKey, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {firstKey}\n")

        self.cache_data[key] = item

    def get(self, key):
        """
        return the value in `self.cache_data` linked to `key`
        """
        return self.cache_data.get(key, None)
