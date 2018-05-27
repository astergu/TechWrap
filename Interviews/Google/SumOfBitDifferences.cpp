/**
 * https://practice.geeksforgeeks.org/problems/sum-of-bit-differences/0
 *
 * Write a program to find the sum of bit differences in all pairs that can be formed from array elements n.
 */

#include <iostream>
#include <vector>
using namespace std;

int numberOfOneBits(int num) {
    int res = 0;
    for (int i = 0; i < 4; ++i) {
        res += num & 1;
        num = num >> 1;
    }
    return res;
}

int sumOfBitDifferences(const vector<int>& array) {
    int res = 0;
    for (int i = 0; i < array.size(); ++i) {
        for (int j = 0; j < i; ++j) {
            res += numberOfOneBits(array[i] ^ array[j]);
        }
    }
    return res * 2;
}

int main() {
	//code
    int T;
    cin >> T;
    int n;
    while (T > 0) {
        cin >> n;
        vector<int> input(n);
        // read the array
        for (int i = 0; i < n; ++i) {
            cin >> input[i];
        }
        int ret = sumOfBitDifferences(input);
        cout << ret << endl;
        T--;
    }

	return 0;
}
