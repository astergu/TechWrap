# 数学问题

- **Basic Calculator** [[leet]](https://leetcode.com/problems/basic-calculator/description/)
    - 题意：实现一个简单的计算器，输入为字符串，字符串中允许存在空格。
    - 分析：用**stack**来实现。
- **Perfect Squares** [[leet]](https://leetcode.com/problems/perfect-squares/description/)
    - 分析：[[python]](Math/PerfectSquares.py)
        - **动态规划**: 从1到n，记录最少的square数目，时间复杂度O(n*sqrt(n))。

# 数组 Array

## 网格问题

- **Island Perimeter** [[leet]](https://leetcode.com/problems/island-perimeter/description/)
    - 题意：计算二维网格里填充为1的格子的总周长。
    - 分析：每个格子的周长为4。如果两个相邻的格子都为1，那么其总周长需要减去它们共享的两条边，即减去2。发现一个新的格子，最多可与三个格子相邻，即减去三条边乘以2的长度。最简单的，检查周边相邻的格子的状态。直接检查周边的邻居。[[python]](Math/IslandPerimeter.py)
- **Search a 2D Matrix II** [[leet]](https://leetcode.com/problems/search-a-2d-matrix-ii/description/)
    - 题意：在一个二维整数矩阵里搜索一个整数。矩阵的组成从上到下递增，从左到右递增。
    - 分析：用**DFS**算法递归。


## 最大问题 Max

- **Maximum XOR of Two Numbers in an Array** [[leet]](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description/)
    - 题意：求数组里的任意两个数的异或的最大值。
    - 分析：最intuitived的方法就是依次算全部数的异或，并且取最大值。这样的时间复杂度是O(N<sup>2</sup>)，这样就会超出运行时限制。题目要求的复杂度是O(n)。 [[python]](Math/MaximumXOROfTwoNumbersInAnArray.py)
- **Burst Balloons** [[leet]](Math/BurstBalloons.py)    
    - 题意：按照一定顺序刺破气球，使得获得的总值最大。
    - 分析：初步直觉是**分治**或**动态规划**。动态规划的思路可以是：如果j-i<3，那么dp[i][j] = dp[i] * ... * dp[j]，如果j - i >= 3, 那么dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j]). [[python]](Array/BurstBalloons.py)   
    
    
## 最小问题 Min

- **Coin Change** [[leet]](https://leetcode.com/problems/coin-change/description/) **动态规划**
    - 题意：给定一组硬币可能的取值，比如[1, 2, 5], 和需要拿出的总共的钱，求最少需要的硬币数量。如果不存在，返回-1.
    - 分析：直观反应是贪心算法，先尽可能拿最大面值的硬币，直到不能拿了再取次大的硬币，实际上行不通，因为原本有答案的可能会没有答案。因此这题应该采用**动态规划**，从0到需要达到的总钱数，子结构为dp[i] = min(dp[i-coins[j]) + 1, dp[i])，两层循环，内层是coins的枚举。[python](DynamicProgramming/CoinChange.py)
- **Meeting Rooms II** [[leet]](https://leetcode.com/problems/meeting-rooms-ii/description/)
    - 题意：给出一组会议的起止时间，求最少需要的会议室数目。
    - 分析：[[python]](Array/MeetingRoomsII.py)
        - **扫描线方法**：适合一维算法问题的解决，涉及具有头尾节点的排序问题。对所有点进行标记，区分起始点和终止点，对所有点进行排序，依次遍历每个店，遇到起始点+1，遇到终止点-1，并更新记录最大值。
        - **堆方法**


## 排列合并问题 Permutation

- **Next Permutation** [[leet]](https://leetcode.com/problems/next-permutation/description/)
    - 题意：找出当前数字排列的下一个字典序比它大的数字，原地排列。
    - 分析：借助举例来让问题更清晰，比如123->132, 213->231, 321->123，首先需要找到需要开始变化的位置，观察一下，123从倒数第二位开始变化，321从第一位开始变化，规律是从后往前找出第一个符合数字增序的索引i，比如123就是2, 213就是2，321就是0。接下去要做的是，从后往前，把第一个大于i-1的数字位的数字和i-1位进行交换. [python](String/NextPermutation.py) 
- **Flatten Nested List Itrator** [[leet]](https://leetcode.com/problems/flatten-nested-list-iterator/description/) 
    - 分析：使用栈对数据进行准备。[[python]](Array/FlattenNestedListIterator.py)
- **Merge Intervals** [[leet]](https://leetcode.com/problems/merge-intervals/description/)
    - 分析：利用排序。

## 元素之和

- **3Sum三数之和** [[geeks]](https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/) [[leet]](https://leetcode.com/problems/3sum/description/) ** 利用排序减少搜索范围**
    - 题意：给定一个整数数组，寻找是否存在三个元素a,b,c，使得a,b,c相加之和等于某个给定值x？要求返回符合要求的a,b,c组合。
    - 分析：
        - **Extra memory**：最简单可以用一个map来记录已经遇到过的元素a及其index，再用两层loop来查看(x-b-c)是否在map中，如果有，则加入结果。时间复杂度O(N<sup>2</sup>)，空间复杂度O(N).
        - **Sorting**: 对数组进行排序，固定a的位置（从0到arr.size - 2），在循环内部，由后往前向内夹逼b和c。时间复杂度O(N^2)，空间复杂度O(1). [python](Array/3Sum.py)
- **Summary Ranges** [[leet]](https://leetcode.com/problems/summary-ranges/description/)
    - 题意：给定一组已排序的整数数组，内部元素没有重复，返回其数的范围。
    - 分析：依序遍历元素。[[python]](Array/SummaryRanges.py)
    

## 字符串 String

- **Longest Palindromic Substring最长回文子串** [[leet]](https://leetcode.com/problems/longest-palindromic-substring/description/) [[geeks1]](https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/) [[geeks2]](https://www.geeksforgeeks.org/longest-palindromic-substring-set-2/)
    - 题意：在字符串s中找出最长的回文子串。
    - 分析：采用**动态规划**，最短回文子串为1。初始化一个二维bool数组dp为false，即记录的是s[i,j]是否是一个回文串。子结构为：1）dp[i][i]=true; 2）如果s[i]==s[j] and dp[i+1][j-1]=true or j - i小于2，那么dp[i][j]=true, 同时更新最长回文子串的起止位置。[python](String/LongestPalindromicSubstring.py)
- **Encode String with Shortest Length 字符串压缩** [[leet]](https://leetcode.com/problems/encode-string-with-shortest-length/description/)
    - 题意：用长度来指代字符串中字母的重复次数，求最短压缩的长度。
    - 分析：因为必须得知道两边的状态，所以比较适合用**动态规划Dynamic Programming**。 [[python]](String/EncodeStringWithShortestLength.py)
        - 检查条件1): encode之后，至少增加3个字符，所以超过5个字符才值得做encode。
        - 检查条件2): 什么时候可以做encode？即相邻的一组子字符串相同。子字符串内部可以各不相同。
        - 时间复杂度O(n<sup>3</sup>).
- **Decode String** [[leet]](https://leetcode.com/problems/decode-string/description/) [[techdev]](https://techdevguide.withgoogle.com/paths/advanced/compress-decompression#!)
    - 题意：把用数字编码压缩的字符串解压。其中数字压缩的字符串可嵌套。
    - 分析：由于压缩内容可以嵌套，
- **Reverse Vowels of a String** [[leet]](https://leetcode.com/problems/reverse-vowels-of-a-string/description/)
    - 题意：把原字符串中的元音倒序排列。
    - 分析：最naive的方法就是找到原字符串中元音的index，然后对这些元音的index上的内容进行交换。时间复杂度O(N * 10)，N是字符串的长度，10是元音的个数。*[Time Limit Exceeded]*
        - 优化方法：比线性复杂度更好的就是logN，因为需要交换两个同是元音的元素，所以考虑从两端向中间遍历，可以达到log的复杂度。 [[python]](String/ReverseVowelsOfString.py)
- **Count of strings that can be formed using a, b and c**[[python]](CountOfStringsThatCanBeFormedUsingABC.py)    
- **Remove Duplicate Letters** [[leet]](https://leetcode.com/problems/remove-duplicate-letters/description/)
    - 题意：移除重复的字母使得字符串里的同一字母只出现一次，并且需要确保返回的结果是所有可能的结果里字典序里最小的。
    - 分析：
        - **naive**: 可以采用**贪心算法**，时间复杂度O(k*n)，其中k为字符串中唯一字符的个数，n为字符串的长度。枚举字符串前缀，直到遇到首个唯一字符为止，从前缀中挑选初最小的字符作为首字符。然后从剩余字符串中移除所有与首字母相同的字母。重复此过程，直到选出所有唯一字符为止。
        - **优化**: 使用**stack**数据结构对上述算法进行优化，可以使时间复杂度缩减为O(n)。首先计算字符串中每个字符出现的次数，得到字典counter，遍历字符串s，记当前字符为c，将counter[c] - 1。如果c已经在stack中，继续遍历。将字符c与栈顶元素top进行比较，若top > c并且counter[top]>0则弹栈，重复此过程，将c入栈。[[python]](String/RemoveDuplicateLetters.py)
- **Word Break II** [[leet]](https://leetcode.com/problems/word-break-ii/description/)
    - 题意：根据词典对句子进行分词，给出全部分词可能性的集合。词典里的词可重用。
    - 分析：采用**DFS**算法，每个字符串分为两部分，当前位置往前的部分prefix和当前位置往后的部分suffix。prefix匹配上即对剩余的字符串suffix进行词典匹配，否则中止尝试。对DFS进行剪枝的方式就是使用一个词典记录。[[python]](String/WordBreakII.py)
- **Longest Absolute File Path** [[leet]](https://leetcode.com/problems/longest-absolute-file-path/description/)
    - 题意：根据文件路径字符串来找出最长的绝对路径。
    - 分析：用空行切割，深度用tab来记录。[[python]](String/LongestAbsoluteFilePath.py)


## 链表 Linked List

- **Add Two Numbers** [[leet]](https://leetcode.com/problems/add-two-numbers/description/)
    - 题意：两个非负整数是用两个链表来表示的，数据是reverse order存储的，每个节点包含一个数字，把这两个数相加并且以链表返回。
    - 分析：实现问题，用一个carry记录进位. [python](LinkedList/AddTwoNumbers.py)

## Searching and Sorting 搜索和排序 

### Binary Search 二分查找

- **Guess Number Higher or Lower** [[leet]](https://leetcode.com/problems/guess-number-higher-or-lower/description/)  **二分查找**[[python]](GuessNumberHigherOrLower.py)


### Sorting 排序

- **Wiggle Sort** [[leet]](https://leetcode.com/problems/wiggle-sort/description/)
    - 题意：给定一个未排序的数组nums，原地排序使得nums[0] <= nums[1] >= nums[2]...
    - 分析：要造成这样wiggle的效果，应该是正常排序以后，再依次交换相邻的两个元素就可以达到，比如交换正常排完序的结果1，2，3，4等即可。[[python]](Sorting/WiggleSort.py)

## 预计算

- [Subarray Sum Equals K](Array/SubarraySumEqualsK.py)
    - 题目：找出一个数组中的连续元素之和等于K的子数组的个数。

## DFS/BFS

- **Number of Islands**: [Python](Graph/NumberOfIslands.py), [C++](Graph/NumberOfIslands.cpp)

# Backtracking 回溯算法
- [Permutations in a given string](String/PermutationsOfAGivenString.py)
- [Permutations of an array](Array/Permutations.py)
- [Permutations of an array with duplicates](Array/PermutationsII.py)

# Sliding Windows 滑动窗口算法

# Dynamic Programming 动态规划算法
- [Longest Palindrome Substring](String/LongestPalindromeSubstring.py)

# 应用题
- **The Skyline problem** [[leet]](https://leetcode.com/problems/the-skyline-problem/description/)
    - 题意：确定城市的轮廓线。
    - 分析：其实本质上是确定边界的问题。
- **Task Scheduler**
- **Meeting Rooms** [[leet]](https://leetcode.com/problems/meeting-rooms/description/)
    - **分析**: 有重叠即不可参加。排序即可。 

# 系统设计问题

- **LRUCache** [[leet]](https://leetcode.com/problems/lru-cache/description/) [[geeks]]https://www.geeksforgeeks.org/lru-cache-implementation/)
    - 题意：设计一个LRU（最近最少使用）缓存机制。
- **Encode and Decode TinyURL** [[leet]](https://leetcode.com/problems/encode-and-decode-tinyurl/description/)
    - 题意：
