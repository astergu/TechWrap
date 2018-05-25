/**
 * LCS Problem Statement: Given two sequences, find the length of longest subsequence present in both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”. So a string of length n has 2^n different possible subsequences.
 *
 * Examples:
 *  LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
 *  LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.
 *
 *
 * Input:
    First line of the input contains no of test cases  T,the T test cases follow.
    Each test case consist of 2 space separated integers A and B denoting the size of string str1 and str2 respectively
    The next two lines contains the 2 string str1 and str2 .
    
 *  Output:
    For each test case print the length of longest  common subsequence of the two strings .

 * Constraints:
        1<=T<=200
        1<=size(str1),size(str2)<=100
*/

#include <iostream>
#include <string>
using namespace std;

int LCS(string s1, string s2, int m, int n) {
    // naive implementation: O(2^n)
    if (m == 0 || n == 0) {
        return 0;
    }
    if (s1[m-1] == s2[n-1]) {
        return LCS(s1, s2, m - 1, n - 1) + 1;
    } else {
        return std::max(LCS(s1, s2, m, n-1), LCS(s1, s2, m-1, n));
    }
}

int longestCommonSubsequence(string s1, string s2, int m, int n) {
    int result[m+1][n+1];
    for (int i = 0; i <= m; ++i) {
        for (int j = 0; j <= n; ++j) {
            if (i == 0 || j == 0) {
                result[i][j] = 0;
            } else {
                if (s1[i-1] == s2[j-1]) {
                    result[i][j] = result[i-1][j-1] + 1;
                } else {
                    result[i][j] = max(result[i][j-1], result[i-1][j]);
                }
            }
        }
    }
    return result[m][n];
}


int main() {
	int T = 0;
    cin >> T;
    int la, lb;
    string sa, sb;
    while (T > 0) {
        cin >> la >> lb;
        cin >> sa >> sb;
        int l1 = sa.length();
        int l2 = sb.length();
        int res = longestCommonSubsequence(sa, sb, l1, l2);
        cout << res << endl;
        T--;
    }

	return 0;
}
