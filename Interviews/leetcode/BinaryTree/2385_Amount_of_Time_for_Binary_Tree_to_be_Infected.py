'''
You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.

Each minute, a node becomes infected if:

The node is currently uninfected.
The node is adjacent to an infected node.
Return the number of minutes needed for the entire tree to be infected.

Input: root = [1,5,3,null,4,10,6,9,2], start = 3
Output: 4
Explanation: The following nodes are infected during:
- Minute 0: Node 3
- Minute 1: Nodes 1, 10 and 6
- Minute 2: Node 5
- Minute 3: Node 4
- Minute 4: Nodes 9 and 2
It takes 4 minutes for the whole tree to be infected so we return 4.
'''

from TreeNode import TreeNode, TreeNodeGenerator
from typing import Optional
from collections import defaultdict

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        """
        Time Limit Exceed!

        space: 
        time: 
        """
        def flatten(l):
            if isinstance(l[0], list):
                return list(set([x for xs in l for x in xs]))
            return l
        
        def dfs(node, parent):
            nonlocal connected
            if not node:
                return
            if parent:
                connected[node.val].append(parent.val)
                connected[parent.val].append(node.val)
            dfs(node.left, node)
            dfs(node.right, node)
        
        connected = defaultdict(list)            
        minutes = 0
        dfs(root, None)  # O(N)
        print(connected) 

        queue = connected.get(start)
        n, visited = len(connected), {start}
        while len(visited) < n:
            visited.update(queue)
            minutes += 1
            print("[Queue] {}, [visited] {}, [minutes] {}".format(queue, visited, minutes))
            queue = flatten([(connected.get(x)) for x in queue])

        return minutes

if __name__ == '__main__':
    sol = Solution()
    lst = ["1","5","3","null","4","10","6","9","2"]
    start = 3
    tng = TreeNodeGenerator(lst)
    print(sol.amountOfTime(tng.get_root(), start))