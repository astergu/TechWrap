/**
 * Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
 *
 */

#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<vector<int> > subsets(vector<int>& nums) {
        vector<vector<int> > result;
        result.push_back(vector<int>());
        for (int n : nums) {
            int size = result.size();
            for (int i = 0; i < size; ++i) {
                vector<int> subset = vector<int>(result[i]);
                subset.push_back(n);
                result.push_back(subset);
            }
        }

        return result;
    }
};


int main() {
    vector<int> nums = {1, 2, 3};
    Solution s;
    vector<vector<int> > ret = s.subsets(nums);

    for (int i = 0; i < ret.size(); ++i) {
        cout << "[";
        for (int j = 0; j < ret[i].size(); j++) {
            cout << ret[i][j] << ", ";
        }
        cout << "]" << endl;
    }
    cout << endl;

    return 0;
}
