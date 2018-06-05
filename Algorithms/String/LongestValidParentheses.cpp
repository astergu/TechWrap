/**
 * Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"


 */

#include <string>
#include <iostream>
#include <stack>
using namespace std;


class Solution {
public:
    int longestValidParentheses(string s) {
        int longest = 0;
        stack<int> cstack;
        cstack.push(-1);
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(') {
                cstack.push(i);
            } else {
                cstack.pop();
                if (!cstack.empty()) {
                    int l = cstack.top();
                    longest = max(i - l, longest);
                } else {
                    cstack.push(i);
                }
            }
        }
        return longest;
    }
};


int main() {
    //string s = "()(()";
    string s = "()(())";
    Solution sol;
    int ret = sol.longestValidParentheses(s);
    cout << ret << endl;
    return 0;
}
