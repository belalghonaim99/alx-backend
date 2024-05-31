#!/usr/bin/env python3
"""
LFU caching module
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Defines and utilizes a LFU caching system.
    """
    def __init__(self):
        """
        Initializes the LFU caching object.
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys = []

    def __reorder_items(self, mru_key):
        """
        Reorders the keys_freq list to reflect the
        """
        max_pos = []
        mru = 0
        mruPos = 0
        position = 0
        for i, key in enumerate(self.keys):
            if key[0] == mru_key:
                mru = key[1] + 1
                mruPos = i
                break
            elif len(max_pos) == 0:
                max_pos.append(i)
            elif key[1] < self.keys[max_pos[-1]][1]:
                max_pos.append(i)
        max_pos.reverse()
        for pos in max_pos:
            if self.keys[pos][1] > mru:
                break
            position = pos
        self.keys.pop(mruPos)
        self.keys.insert(position, [mru_key, mru])

    def put(self, key, item):
        """
        Adds an item to the cache.
        """
        if key is None or item is None:
            return None
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.keys[-1]
                self.cache_data.pop(lfu_key)
                self.keys.pop()
                print("DISCARD:", lfu_key)
            self.cache_data[key] = item
            index = len(self.keys)
            for i, key_freq in enumerate(self.keys):
                if key_freq[1] == 0:
                    index = i
                    break
            self.keys.insert(index, [key, 0])
        else:
            self.cache_data[key] = item
            self.__reorder_items(key)

    def get(self, key):
        """
        Retrieves an item from the cache.
        """
        if key is not None and key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)
