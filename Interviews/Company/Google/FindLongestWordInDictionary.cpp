/**
 * Given a string S and a set of words D, find the longest word in D that is a subsequence of S.

Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W, without reordering the remaining characters.

Note: D can appear in any format (list, hash table, prefix tree, etc.

For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", "kangaroo"} the correct output would be "apple"


 */


#include <string>
#include <iostream>
#include <vector>
using namespace std;

bool isSubstring(string s, string w) {
    int i = 0;
    int j = 0;
    while (i < s.length() && j < w.length()) {
        if (s[i] == w[j]) {
            i++;
            j++;
        } else {
            i++;
        }
    }
    if (j == w.length()) {
        return true;
    }

    return false;
}

string longestWord(string s, vector<string> dictionary) {
    int longest = 0;
    string ret = "";
    for (int i = 0; i < dictionary.size(); i++) {
        if (isSubstring(s, dictionary[i])) {
            if (dictionary[i].length() > longest) {
                ret = dictionary[i];
                longest = dictionary[i].length();
            }
        }
    }
    return ret;
}

int main() {
    string s = "abppplee";
    vector<string> dictionary = {"able", "ale", "apple", "bale", "kangaroo"};

    string ret = longestWord(s, dictionary);
    cout << ret << endl;
    return 0;
}
