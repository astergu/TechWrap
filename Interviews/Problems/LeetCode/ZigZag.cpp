/**
 * http://community.topcoder.com/stat?c=problem_statement&pm=1259&rd=4493
 *
 * Constraints:
 *  - sequence contains between 1 and 50 elements, inclusive.
 *  - Each element of sequence is between 1 and 1000, inclusive.
 *
 * Examples:
 *  0) { 1, 7, 4, 9, 2, 5 }
 *      Returns: 6
 *      The entire sequence is a zig-zag sequence.
 *
 *  1) { 1, 17, 5, 10, 13, 15, 10, 5, 16, 8 }
 *      Returns: 7
 *      There are several subsequences that achieve this length. One is 1,17,10,13,10,16,8.		
 *
 *
 * Ideas:
 *  (1) Dynamic Programming
 *   
 */


#include <vector>
#include <iostream>
using namespace std;

class ZigZag {
public:
    int dp(vector<int> sequence, int idx) {
        return 0;
    }

    int longestZigZag(vector<int>& sequence) {
        vector<int>* result = new vector<int>(sequence.size() + 1);
        for (size_t i = 0; i < sequence.size(); ++i) {
            dp(sequence, i);
        }

        return 0;
    };
};


int main() {
    ZigZag* zz = new ZigZag();
    vector<int> sequence = {1, 7, 4, 9, 2, 5};
    int ret = zz->longestZigZag(sequence);
    cout << "ret: " << ret << endl;
    return 0;
}
