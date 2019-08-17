/**
 * You are given a list of non-negative integers and you start at the left-most integer in this list. After that you need to perform the following step:

    Given that the number at the position where you are now is P you need to jump P positions to the right in the list. For example, if you are at position 6 and the number at position 6 has the value 3, you need to jump to position 6 + 3 = 9. Repeat this operation until you reach beyond the right-side border of the list.

Your program must return the number of jumps that it needs to perform following this logic. Note that the list may contain the number 0, which mean that you can get stuck at a this position forever. In such cases you must return the number -1.

The length N of the input list will be in the range [1, 1000].
 *
 *
 */

#include <vector>
#include <iostream>
using namespace std;

int jump_over_numbers(const vector<int>& list) {
    int i = 0;
    int count = 0;
    while (i < list.size()) {
        if (list[i] == 0) {
            return -1;
        }
        i += list[i];
        count++;
    }
    return count;
}

int main() {
    vector<int> list = {3, 4, 1, 2, 5, 6, 9, 0, 1, 2, 3, 1};
    int count = jump_over_numbers(list);
    cout << "ret: " << count << endl;
    return 0;
}
