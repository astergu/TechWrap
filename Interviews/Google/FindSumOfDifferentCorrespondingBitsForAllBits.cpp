/**
 * We define f (X, Y) as number of different corresponding bits in binary representation of X and Y. For example, f (2, 7) = 2, since binary representation of 2 and 7 are 010 and 111, respectively. The first and the third bit differ, so f (2, 7) = 2.

You are given an array of N integers, A1, A2 ,…, AN. Find sum of f(Ai, Aj) for all pairs (i, j) such that 1 ≤ i, j ≤ N. Return the answer modulo 109+7. 
 */

#include <iostream>
#include <vector>
using namespace std;

int numOfDifferentBits(int A, int B) {
    int C = A ^ B;
    int res = 0;
    for (int i = 0; i < 32; ++i) {
        res += C & 1;
        C = C >> 1;
    }
    return res;
}

int bitSum(vector<int> nums) {
    int res = 0;
    for (size_t i = 0; i < nums.size(); ++i) {
        for (size_t j = 0; j < i; ++j) {
            res += numOfDifferentBits(nums[i], nums[j]);
        }
    }
    return (res * 2) % (100000007);
}

int main() {
	//code
    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        vector<int> nums;
        int num;
        while (n--) {
            cin >> num;
            nums.push_back(num);
        }
        int ret = bitSum(nums);
        cout << ret << endl;
    }

	return 0;
}
