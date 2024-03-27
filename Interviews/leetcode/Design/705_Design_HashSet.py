'''
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

    void add(key) Inserts the value key into the HashSet.
    bool contains(key) Returns whether the value key exists in the HashSet or not.
    void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

'''

class MyHashSet:

    def __init__(self):
        self.hs = {}

    def add(self, key: int) -> None:
        self.hs[key] = True 

    def remove(self, key: int) -> None:
        if key in self.hs:
            self.hs.popitem(key)        

    def contains(self, key: int) -> bool:
        return key in self.hs        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)