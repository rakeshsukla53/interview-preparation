__author__ = 'rakesh'

from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        """
        :rtype: int
        """
        if self.cache.has_key(key):
            val = self.cache[key]
            del self.cache[key]
            self.cache[key] = val
            return val
        return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if self.cache.has_key(key):
            del self.cache[key]
            self.cache[key] = value
        else:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
                self.cache[key] = value
            else:
                self.cache[key] = value


testLru = LRUCache(2)
print testLru.get(2)
print testLru.set(2, 6)
print testLru.get(1)
print testLru.set(1, 5)
print testLru.set(1, 2)
print testLru.get(1)
print testLru.get(2)

