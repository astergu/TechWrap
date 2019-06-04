#include <vector>
#include <unordered_map>
#include <iostream>
using namespace std;


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> hash;
        
        for (int i = 0; i < nums.size(); ++i) {
            std::unordered_map<int, int>::iterator key = hash.find(target - nums[i]);
            if (key != hash.end()) {
                return {key->second, i};
            } else {
                hash.emplace(nums[i], i);
            }
           
        }
        throw std::invalid_argument("No TwoSum solution!");
    }
    
};


int main(int argc, char* argv[]) {
    int temp[] = {3, 2, 4};
    vector<int> nums;
    nums.insert(nums.begin(), temp, temp+3);

    int target = 6;

    Solution s = Solution();
    vector<int> result = s.twoSum(nums, target);

    for (vector<int>::iterator iter = result.begin(); iter < result.end(); iter++) {
        std::cout << *iter << std::endl;
    }

    return 0;
}