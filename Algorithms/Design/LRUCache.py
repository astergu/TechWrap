"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""

from collections import OrderedDict


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = OrderedDict()
        self._capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self._capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value


class LRUCache2(object):
    def __init__(self, capacity):
        self._capacity = capacity
        self.cache = dict()
        self.lst = []

    def get(self, key):
        if key not in self.cache:
            return -1
        self.lst.remove(key)
        self.lst.append(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.lst.remove(key)
            self.lst.append(key)
        else:
            if len(self.cache) == self._capacity:
                del_key = self.lst[0]
                self.lst = self.lst[1:]
                self.cache.pop(del_key)

            self.lst.append(key)
            self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
cache = LRUCache2(2)
cache.put(2, 1)
cache.put(2, 2)
print cache.get(2)       # returns 1
cache.put(1, 1)    # evicts key 2
cache.put(4, 1)    # evicts key 1
print cache.get(2)       # returns -1 (not found)
