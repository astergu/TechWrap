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

