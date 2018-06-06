#include <vector>
#include <unordered_map>
#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;


class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char, int> mp;
        int count = 0;
        for (auto task : tasks) {
            mp[task]++;
            count = max(count, mp[task]);
        }

        int ans = (count - 1) * (n + 1);  // the cpu time for the most frequent task
        for (auto e : mp) {
            if (e.second == count) {
                ans += 1;
            }
        }
        return std::max(ans, int(tasks.size()));
    }

};



int main() {
    vector<char> tasks = {'A', 'A', 'A', 'B', 'B', 'B'};
    Solution s;
    int n = 2;
    int ret = s.leastInterval(tasks, n);
    cout << ret << endl;
    return 0;
}
