/**
 * Design an algorithm to determine if a circular array of relative indices has only one single, complete cycle.
 */

#include <vector>
#include <iostream>
#include <unordered_set> // unordered_set is implemented using hash table
using namespace std;

bool hasOneCompleteCycle(const vector<int>& array) {
    unordered_set<int> cache;
    int idx = 0; 
    
    unordered_set<int>::const_iterator it = cache.find(array[idx]);
    do {
        if (it != cache.end()) {
            return false;
        }
        cache.insert(idx);
        idx = (idx + array[idx]) % array.size();
    } while (idx != 0);

    return true;
}

bool hasOneCompleteCycleWithNoExtraMemory(const vector<int>& array) {
    int N = array.size();
    int curr = 0;
    for (int i = 0; i < N; ++i) {
        curr = (curr + array[curr]) % N;
        if (curr < 0) {
            curr += N;
        }
        if (curr == 0 && i < N - 1) {
            return false;
        }
    }
    return true; // should only return to 0 after N steps
}


int main() {
    vector<int> array = {2, 2, -1};
    cout << "hasOneCompleteCycle: " << std::boolalpha << hasOneCompleteCycle(array) << endl;
    cout << "hasOneCompleteCycle: " << std::boolalpha << hasOneCompleteCycleWithNoExtraMemory(array) << endl;
    return 0;
}
