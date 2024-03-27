'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

'''

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ""
        curr_num = 0
        
        for c in s:
            print(c)
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)
            elif c == "[":
                stack.append(curr_num)
                stack.append(curr_str)
                curr_num = 0
                curr_str = ""
            elif c == "]":
                prev_str = stack.pop()
                prev_num = stack.pop()
                curr_str = prev_str + curr_str * prev_num
            else:
                curr_str += c
            
            print("[curr_str]: {}, [curr_num]: {}, [stack]: {}".format(curr_str, curr_num, stack))
        
        while stack:
            curr_str = stack.pop() + curr_str
        
        return curr_str


if __name__ == '__main__':
    sol = Solution()
    s = "3[a2[c]]"
    print(sol.decodeString(s))