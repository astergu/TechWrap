# 搜索

## Backtracking 回溯算法

Backtracking is a systematic way to iterate through all possible configurations of a seach space.


其实回溯算法和我们常说的 DFS 算法非常类似，本质上就是一种暴力穷举算法。回溯算法和 DFS 算法的细微差别是：回溯算法是在遍历「树枝」，DFS 算法是在遍历「节点」，本文就是简单提一下，你有个印象就行了。等你看了 手把手刷二叉树（纲领篇） 和 图论算法基础 之后就能深刻理解这句话的含义了。

抽象地说，解决一个回溯问题，实际上就是遍历一棵决策树的过程，树的每个叶子节点存放着一个合法答案。你把整棵树遍历一遍，把叶子节点上的答案都收集起来，就能得到所有的合法答案。

站在回溯树的一个节点上，你只需要思考 3 个问题：

1. 路径：也就是已经做出的选择。
2. 选择列表：也就是你当前可以做的选择。
3. 结束条件：也就是到达决策树底层，无法再做选择的条件。

### 回溯算法和DFS的区别

回溯算法关注的不是节点，而是树枝。

```java
// DFS 算法，关注点在节点
void traverse(TreeNode root) {
    if (root == null) return;
    printf("进入节点 %s", root);
    for (TreeNode child : root.children) {
        traverse(child);
    }
    printf("离开节点 %s", root);
}

// 回溯算法，关注点在树枝
void backtrack(TreeNode root) {
    if (root == null) return;
    for (TreeNode child : root.children) {
        // 做选择
        printf("从 %s 到 %s", root, child);
        backtrack(child);
        // 撤销选择
        printf("从 %s 到 %s", child, root);
    }
}
```

[回溯算法秒杀所有排列/组合/子集问题](https://labuladong.github.io/algo/di-san-zha-24031/bao-li-sou-96f79/hui-su-sua-56e11/)

```
无论是排列、组合还是子集问题，简单说无非就是让你从序列 nums 中以给定规则取若干元素，主要有以下几种变体：

- 形式一、元素无重不可复选，即 nums 中的元素都是唯一的，每个元素最多只能被使用一次，这也是最基本的形式。

以组合为例，如果输入 nums = [2,3,6,7]，和为 7 的组合应该只有 [7]。

- 形式二、元素可重不可复选，即 nums 中的元素可以存在重复，每个元素最多只能被使用一次。

以组合为例，如果输入 nums = [2,5,2,1,2]，和为 7 的组合应该有两种 [2,2,2,1] 和 [5,2]。

- 形式三、元素无重可复选，即 nums 中的元素都是唯一的，每个元素可以被使用若干次。

以组合为例，如果输入 nums = [2,3,6,7]，和为 7 的组合应该有两种 [2,2,3] 和 [7]。

当然，也可以说有第四种形式，即元素可重可复选。但既然元素可复选，那又何必存在重复元素呢？元素去重之后就等同于形式三，所以这种情况不用考虑。

上面用组合问题举的例子，但排列、组合、子集问题都可以有这三种基本形式，所以共有 9 种变化。

除此之外，题目也可以再添加各种限制条件，比如让你求和为 target 且元素个数为 k 的组合，那这么一来又可以衍生出一堆变体，怪不得面试笔试中经常考到排列组合这种基本题型。

但无论形式怎么变化，其本质就是穷举所有解，而这些解呈现树形结构，所以合理使用回溯算法框架，稍改代码框架即可把这些问题一网打尽。
```

首先，组合问题和子集问题其实是等价的，这个后面会讲；至于之前说的三种变化形式，无非是在这两棵树上剪掉或者增加一些树枝罢了。

#### 典型问题

##### 子集 Subsets （元素无重不可复选）

**Leetcode 78**

    输入一个无重复元素的数组 nums，其中每个元素最多使用一次，请你返回 nums 的所有子集。


```python
from typing import List

class Solution: 
    def __init__(self):
        self.res = []
        # 记录回溯算法的递归路径
        self.track = []

    # 主函数
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums, 0)
        return self.res
    
    # 回溯算法核心函数，遍历子集问题的回溯树
    def backtrack(self, nums: List[int], start: int) -> None:     
        # 前序位置，每个节点的值都是一个子集
        self.res.append(list(self.track))
        
        # 回溯算法标准框架
        for i in range(start, len(nums)):
            # 做选择
            self.track.append(nums[i])
            # 通过 start 参数控制树枝的遍历，避免产生重复的子集
            self.backtrack(nums, i + 1)
            # 撤销选择
            self.track.pop()
```

##### 组合 Combinations （元素无重不可复选）

**Leetcode 77**

    给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。这是标准的组合问题，但我给你翻译一下就变成子集问题了：给你输入一个数组 nums = [1,2..,n] 和一个正整数 k，请你生成所有大小为 k 的子集。

```python
from typing import List

class Solution:
    def __init__(self):
        self.res = []
        # 记录回溯算法的递归路径
        self.track = []

    # 主函数
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.backtrack(1, n, k)
        return self.res

    def backtrack(self, start: int, n: int, k: int) -> None:
        # base case
        if k == len(self.track):
            # 遍历到了第 k 层，收集当前节点的值
            self.res.append(self.track.copy())
            return
        
        # 回溯算法标准框架
        for i in range(start, n+1):
            # 选择
            self.track.append(i)
            # 通过 start 参数控制树枝的遍历，避免产生重复的子集
            self.backtrack(i + 1, n, k)
            # 撤销选择
            self.track.pop()
```

##### 排列 Permutations （元素无重不可复选）

**Leetcode 46**

    给定一个不含重复数字的数组 nums，返回其所有可能的全排列。

刚才讲的组合/子集问题使用 start 变量保证元素 nums[start] 之后只会出现 nums[start+1..] 中的元素，通过固定元素的相对位置保证不出现重复的子集。

但排列问题本身就是让你穷举元素的位置，nums[i] 之后也可以出现 nums[i] 左边的元素，所以之前的那一套玩不转了，需要额外使用 used 数组来标记哪些元素还可以被选择。

我们用`used`数组标记已经在路径上的元素避免重复选择，然后收集所有叶子节点上的值，就是所有全排列的结果：

```python
from typing import List

class Solution:
    res = []
    #记录回溯算法的递归路径
    track = []
    # track 中的元素会被标记为 true
    used = []

    # 主函数，输入一组不重复的数字，返回它们的全排列
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.used = [False] * len(nums)
        self.backtrack(nums)
        return self.res

    # 回溯算法核心函数
    def backtrack(self, nums):
        # base case，到达叶子节点
        if len(self.track) == len(nums):
            # 收集叶子节点上的值
            self.res.append(self.track[:])
            return

        # 回溯算法标准框架
        for i in range(len(nums)):
            # 已经存在 track 中的元素，不能重复选择
            if self.used[i]:
                continue
            # 做选择
            self.used[i] = True
            self.track.append(nums[i])
            # 进入下一层回溯树
            self.backtrack(nums)
            # 取消选择
            self.track.remove(nums[i])
            self.used[i] = False
```

但如果题目不让你算全排列，而是让你算元素个数为 k 的排列，怎么算？

也很简单，改下 backtrack 函数的 base case，仅收集第 k 层的节点值即可：

```python
# 回溯算法核心函数
def backtrack(nums: List[int], k: int) -> None:
    # base case，到达第 k 层，收集节点的值
    if len(track) == k:
        # 第 k 层节点的值就是大小为 k 的排列
        res.append(track[:])
        return

    # 回溯算法标准框架
    for i in range(len(nums)):
        # ...
        backtrack(nums, k)
        # ...
```

##### 子集/组合 Subsets（元素可重不可复选）

刚才讲的标准子集问题输入的 nums 是没有重复元素的，但如果存在重复元素，怎么处理呢？

**Leetcode 90**

    给你一个整数数组 nums，其中可能包含重复元素，请你返回该数组所有可能的子集。

需要先进行排序，让相同的元素靠在一起，如果发现 nums[i] == nums[i-1]，则跳过：


```cpp
// 注意：cpp 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
// 本代码不保证正确性，仅供参考。如有疑惑，可以参照我写的 java 代码对比查看。

class Solution {
    vector<vector<int>> res; // 输出结果
    vector<int> track; // 搜索路径
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end()); // 排序，让相同的元素靠在一起
        backtrack(nums, 0);
        return res; // 返回结果
    }

    void backtrack(vector<int>& nums, int start) { // start 为当前的枚举位置
        res.emplace_back(track); // 前序位置，每个节点的值都是一个子集
        for(int i = start; i < nums.size(); i++) {
            if (i > start && nums[i] == nums[i - 1]) { // 剪枝逻辑，值相同的相邻树枝，只遍历第一条
                continue;
            }
            track.emplace_back(nums[i]); // 添加至路径
            backtrack(nums, i + 1); // 进入下一层决策树
            track.pop_back(); // 回溯
        }
    }
};
```

这段代码和之前标准的子集问题的代码几乎相同，就是添加了排序和剪枝的逻辑。

至于为什么要这样剪枝，结合前面的图应该也很容易理解，这样带重复元素的子集问题也解决了。

我们说了组合问题和子集问题是等价的，所以我们直接看一道组合的题目吧。

**Leetcode 40**

    给你输入 candidates 和一个目标和 target，从 candidates 中找出中所有和为 target 的组合。candidates 可能存在重复元素，且其中的每个数字最多只能使用一次。

说这是一个组合问题，其实换个问法就变成子集问题了：请你计算 candidates 中所有和为 target 的子集。所以这题怎么做呢？

对比子集问题的解法，只要额外用一个 trackSum 变量记录回溯路径上的元素和，然后将 base case 改一改即可解决这道题：

```cpp
// 注意：cpp 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
// 本代码不保证正确性，仅供参考。如有疑惑，可以参照我写的 java 代码对比查看。

class Solution {
public:
    vector<vector<int>> res;
    //记录回溯的路径
    vector<int> track;
    //记录 track 中的元素之和
    int trackSum = 0;

    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        // 先排序，让相同的元素靠在一起
        sort(candidates.begin(), candidates.end());
        backtrack(candidates, 0, target);
        return res;
    }

    //回溯算法主函数
    void backtrack(vector<int>& nums, int start, int target) {
        //base case，达到目标和，找到符合条件的组合
        if(trackSum == target) {
            res.push_back(track);
            return;
        }
        //base case，超过目标和，直接结束
        if(trackSum > target) {
            return;
        }

        //回溯算法标准框架
        for(int i = start; i < nums.size(); i++) {
            //剪枝逻辑，值相同的树枝，只遍历第一条
            if(i > start && nums[i] == nums[i-1]) {
                continue;
            }
            //做选择
            track.push_back(nums[i]);
            trackSum += nums[i];
            //递归遍历下一层回溯树
            backtrack(nums, i+1, target);
            //撤销选择
            track.pop_back();
            trackSum -= nums[i];
        }
    }
};
```

##### 排列（元素可重不可复选）

排列问题的输入如果存在重复，比子集/组合问题稍微复杂一点。

**Leetcode 47**

    给你输入一个可包含重复数字的序列 nums，请你写一个算法，返回所有可能的全排列，函数签名如下：

```cpp
// 注意：cpp 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
// 本代码不保证正确性，仅供参考。如有疑惑，可以参照我写的 java 代码对比查看。

class Solution {
public:
    // 保存结果
    vector<vector<int>> res;
    // 记录当前位置的元素
    vector<int> track;
    // 记录元素是否被使用
    vector<bool> used;

    // 主函数
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        // 排序，让相同的元素靠在一起
        sort(nums.begin(), nums.end());
        // 初始化used数组
        used = vector<bool>(nums.size(), false);
        // 回溯
        backtrack(nums);
        // 返回结果
        return res;
    }

    // 回溯函数
    void backtrack(vector<int>& nums) {
        // 当长度相等时，将结果记录
        if (track.size() == nums.size()) {
            res.push_back(track);
            return;
        }

        // 遍历没有被使用过的元素
        for (int i = 0; i < nums.size(); i++) {
            if (used[i]) {
                continue;
            }
            // 新添加的剪枝逻辑，固定相同的元素在排列中的相对位置
            if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) {
                continue;
            }
            // 添加元素，标记为使用过
            track.push_back(nums[i]);
            used[i] = true;
            // 继续回溯
            backtrack(nums);
            // 回溯
            track.pop_back();
            used[i] = false;
        }
    }
};
```

你对比一下之前的标准全排列解法代码，这段解法代码只有两处不同：

1. 对 nums 进行了排序。

2. 添加了一句额外的剪枝逻辑。

类比输入包含重复元素的子集/组合问题，你大概应该理解这么做是为了防止出现重复结果。

但是注意排列问题的剪枝逻辑，和子集/组合问题的剪枝逻辑略有不同：新增了 !used[i - 1] 的逻辑判断。



# 图算法


有两种图遍历算法：BFS和DFS。区别在于探索节点的顺序。Queue-BFS，Stack-DFS。

[图论基础及遍历算法](https://labuladong.github.io/algo/di-yi-zhan-da78c/shou-ba-sh-03a72/tu-lun-ji--d55b2/)

## Depth-First Search 深度优先搜索  

DFS的应用 [The Algorithm Design Manual](The Algorithm Design Manual)

### Finding Circles 

Back edges are the key to finding a cycle in an undirected graph. If there is no back edge, all edges are tree edges, and no cycle exists in a tree.

```
process_edge(int x, int y) {
    if (parent[x] != y) { /* found back edge! */
        printf("Cycle from %d to %d", y, x);
        find_path(y, x, parent);
        finished = TRUE;
    }
}
```

### Articulation Vertices

A single vertex whose deletion disconnects a connected component of the graph. Such a vertex is called an *articulation vertex* or *cut-node*.

## Breadth-First Search 广度优先搜索

# 参考

1. The Algorithm Design Manual

