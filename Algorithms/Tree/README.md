```python
class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
```
- A *full binary tree* is a binary tree in which every node other than the leaves has two children. 
- A *perfect binary tree* is a full binary tree in which all leaves are at the 
same depth, and in which every parent has two children. 
- A *complete binary tree* is a binary tree in which every leve, except possibly the last, is complete filled, and all nodes are as far left as possible.
- A perfect binary tree of height *h* contains exactly 2<sup>h+1</sup> - 1 nodes, of which 2<sup>h</sup> are leaves. A complete binary tree on *n* nodes has height [logn]. 


## Practical Tips
- **Recursive algorithms** are well-suited to problems on trees. Remember to include space implicitly allocated on the function call stack when doing space complexity analysis.
- Some tree problems have simple brute-force solutions that use *O(n)* space solution, but subtler solutions that uses the **existing tree nodes** to reduce space complexity in *O(1)*.

## Base problems
- **Test If A Binary Tree is Height-balanced**
```python
# A binary tree is said to be height-balanced if for each node in the tree, the difference
in the height of its left and right subtrees is at most one.
def is_balanced_binary_tree(tree):
    BalancedStatusWithHeight = collections.namedtuple(
        'BalancedStatusWithHeight', ('balanced', 'height'))

    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(True, -1)  # Base case. 

        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            return BalancedStatusWithHeight(False, 0)
        
        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)
```
Time complexity *O(n)*, space complexity *O(h)*.
- **Variant**: Write a program that returns the size of the largest subtree that is complete.
- **Variant**: Define a node in a binary tree to be *k*-balanced if the difference in the number of nodes in its left and right subtrees is no more than *k*. Design an algorithm that takes as input a binary tree and positive integer *k*, and returns a node in the binary tree such that the node is not *k*-balanced, but all of its descentdants are *k*-balanced.

# Tree Traversal 树的遍历

## Binary Tree Preorder Traversal 前序遍历

Preoder Traversal **Recursive** vs. **Iterative** [Code](BinaryTreePreoderTraversal.py)

- **Recursive递归实现**
    - 时间复杂度O(n)，空间复杂度O(1)
- **Iterative用栈迭代实现**
    - 时间复杂度O(n)，空间复杂度O(n)
- **Morris先序遍历**
    - 时间复杂度O(n), 空间复杂度O(1)

### 迭代遍历的基本思想

前序遍历意味着父节点需要优先于子节点处理，获取到了根节点，也就知道了相应的子节点，根节点的信息已经访问过可以不需要再保存。因为存在先后顺序，因此用栈来维护这一顺序。首先在栈中放入根节点，从栈中弹出一个节点，对于这个节点，先在结果中放入该节点（父节点）的值，然后依次压入其子节点，由于需要先访问左边的子节点，因此先压入右节点。

## Binary Tree Inorder Traversal 中序遍历

Inorder Traversal **Recursive** vs. **Iterative** [Code](BinaryTreeInorderTraversal.py)

- **Recursive递归实现**
    - 时间复杂度O(n)，空间复杂度O(1)
- **Iterative用栈迭代实现**
    - 时间复杂度O(n)，空间复杂度O(n)
- **Morris先序遍历**
    - 时间复杂度O(n), 空间复杂度O(1)

### 迭代遍历的基本思想

中序遍历意味着左子节点优先于父节点访问，然后再是右子节点。因此父节点信息不能访问完就丢弃。假设我们有一个栈，那么它可以用来保存从根节点向左持续遍历经过的父节点，直到最左边的叶节点，然后访问栈，从栈顶弹出元素，在结果中加入该元素节点的值，然后在栈中压入该节点的右子节点。这样就实现了**左子节点-父节点-右子节点**的顺序。

## Binary Tree Postorder Traversal 后序遍历

Postorder Traversal **Recursive** vs. **Iterative** [Code](BinaryTreePostorderTraversal.py)

- **Recursive递归实现**
    - 时间复杂度O(n)，空间复杂度O(1)
- **Iterative用栈迭代实现**
    - 时间复杂度O(n)，空间复杂度O(n)
- **Morris先序遍历**
    - 时间复杂度O(n), 空间复杂度O(1)

### 迭代遍历的基本思想

后序遍历意味着左右子节点都优先于父节点访问，父节点信息需要经过两次访问，因此需要根据是否访问过而进行二次压栈。

## Trie Tree 字典树压缩

