## Practical Tips
- A string can be viewed as a special kind og array, namely one made out of characters.
- You should know how strings are represented in memory, and understand basic operations on strings such as comparison, copying, joining, splitting, matching, etc. Advanced string processing algorithms often use *hash tables* and *dynamic programming*.
- Similar to arrays, string problems often have simple brute-force solutions that use *O(n)* space solution,
but subtler solutions that use the string itself to **reduce space complexity** to *O(1)*.
- Understand the **implications** of a string type which is **immutable**, e.g., the need to allocate a new string
when concatenating immutable strings. Know **alternative** to immutable strings, e.g., a list in Python.
- Updating a mutable string from the front is slow, so see if it's possible to **write values from the back**.
- **is palindromic string**
    ```python
    def is_palindromic(s):
        return all(s[i] == s[-i] for i in range(len(s) // 2))
    ```
    The time complexity is *O(n)* and the space complexity is *O(1)*, where *n* is the length of the string.
- **Implement a string/integer inter-conversion functions**.
```python
def int_to_string(x):
    is_negative = False
    if x < 0:
        x, is_negative = -x, True
    
    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break

    # Adds the negative sign back if is_negative
    return ('-' if is_negative else '') + ''.join(revereed(s))

def string_to_int(s):
    return functools.reduce(lambda running_sum,
                            c: running_sum * 10 + string.digits.index(c),
                            s[s[0] == '-',
                            0) * (-1 if s[0] == '-' else 1)
```
- **Base Conversion**
```python
def convert_base(num_as_string, b1, b2):
    def construct_from_base(num_as_int, base):
        return ('' if num_as_int == 0 else
                construct_from_base(num_as_int // base, base) +
                string.hexdigits[num_as_int % base].upper())

        is_negative = num_as_string[0] == '-'
        num_as_int = functools.reduce(
            lambda x, c: x * b1 + string.hexdigits.index(c.lower()),
            num_as_string[is_negative:], 0)
        return ('-' if is_negative else '') + '0' if num_as_int == 0 else
                                            construct_from_base(num_as_int, b2))
```
The time complexity is *O(n(1 + log<sub>b<sub>2</sub></sub>b<sub>1</sub>))*, where *n* is the length of *s*.

## Basic Questions

### Substring Match

KMP算法

### Anagrams Substring Search / All Permutations

[https://www.geeksforgeeks.org/anagram-substring-search-search-permutations/](https://www.geeksforgeeks.org/anagram-substring-search-search-permutations/)




## Questions
- [x] [Minimum Windows Substring](MinimumWindowSubstring.py)
    - 涉及SlidingWindow算法、Hash Table、Two Pointers双指针等，比较有难度，大部分情况下会在onsite中出现。
    
- [] Next Permutation
    - link: [https://leetcode.com/problems/next-permutation/description/](https://leetcode.com/problems/next-permutation/description/)
- [x] [Longest Palindrome Substring](LongestPalindromeSubstring.py)
    - link: [https://leetcode.com/problems/longest-palindromic-substring/description/](https://leetcode.com/problems/longest-palindromic-substring/description/)
- [x] [Regular Expression Matching](RegularExpressionMatching.py)
    - link: [https://leetcode.com/problems/regular-expression-matching/description/](https://leetcode.com/problems/regular-expression-matching/description/)
- [x] [Find All Anagrams in a String](FindAllAnagramsInAString.py)
    - link: [https://leetcode.com/problems/find-all-anagrams-in-a-string/submissions/1](https://leetcode.com/problems/find-all-anagrams-in-a-string/submissions/1)
    - solution： Sliding Windows Solution
- [] [Permutation in String](PermutationInString.py)
    - link: [https://leetcode.com/problems/permutation-in-string/description/](https://leetcode.com/problems/permutation-in-string/description/)
    - solution: 
- [x] [Implement Atoi](ImplementAtoI.py)
    - link: [https://leetcode.com/problems/string-to-integer-atoi/description/](https://leetcode.com/problems/string-to-integer-atoi/description/)
- [] [Implement strStr]()

## Classical Algorithms 经典算法

### Knuth-Morris-Pratt Algorithm (KMP, Knuth-Morris-Pratt字符串查找算法)
- 目标：在一个主文本字符串*s*中查找一个词*w*的出现位置。
- 方法：此算法通过运用对这个词在不匹配时本身就包含足够的信息来确定下一个匹配将在
       哪里开始的发现，从而避免重新检查先前匹配的字符。

### Sliding Window Algorithm (滑动窗口算法)

可以解决一系列substring searching problem，基本思想是利用双指针，以及map数据结构，维护一个
不断扩展、伸缩的窗口，在窗口内探测记录感兴趣的结果。


### Aho-Corasick Algorithm
