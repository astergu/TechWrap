from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.left_visited = False
        self.right_visited = False
    
    def level_order_traversal(self):
        ans, level = [], [self]
        while self and level:
            ans.append([x.val if x else "null" for x in level])
            lr = [(x.left, x.right) for x in level if x]
            level = [leaf for x in lr for leaf in x]
        
        print("----------------------- Level Order Traversal -------------------------")
        for res in ans:
            print(res)


class TreeNodeGenerator:
    def __init__(self, vlist: List[str]):
        self._root = None
        self.Q = deque()
        for v in vlist:
            self.insert_node(v)
        
    def insert_node(self, val):
        new_node = TreeNode(int(val)) if val != "null" else None
        if self.Q:
            while not self.Q[0]:
                self.Q.popleft()
            parent = self.Q[0]
        if not self._root: # 创建根节点
            self._root = new_node
        elif not parent.left and not parent.left_visited:
            parent.left = new_node
            parent.left_visited = True
        elif not parent.right and not parent.right_visited:
            parent.right = new_node
            parent.right_visited = True
            self.Q.popleft()
        
        self.Q.append(new_node)
    
    def get_root(self):
        return self._root

    def level_order_traversal(self):
        ans, level = [], [self._root]
        while self._root and level:
            ans.append([x.val if x else "null" for x in level])
            lr = [(x.left, x.right) for x in level if x]
            level = [leaf for x in lr for leaf in x]
        
        print("----------------------- Level Order Traversal -------------------------")
        for res in ans:
            print(res)
     