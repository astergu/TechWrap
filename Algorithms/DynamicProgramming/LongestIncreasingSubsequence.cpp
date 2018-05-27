/**
 *
 *Given a list of N integers find the longest increasing subsequence in this list.
Example

If the list is [16, 3, 5, 19, 10, 14, 12, 0, 15] one possible answer is the subsequence [3, 5, 10, 12, 15], another is [3, 5, 10, 14, 15].

If the list has only one integer, for example: [14], the correct answer is [14].

One more example: [10, 8, 6, 4, 2, 0], a possible correct answer is [8].
 *
 */

#include <vector>
using namespace std;

int longest_increasing_subsequence(vector<int> sequence) {
    return 0;
}

vector<int> longest_increasing_subsequence(vector<int> sequence) {
    size_t size = sequence.size();
    vector<int> result = new vector<int>(size + 1);
    for (size_t i = 0; i < size; ++i) {
        result[i] = 1;
    }

    for (size_t i = 0; i < size; ++i) {
        for (size_t j = 0; j < i; ++j) {
            if (sequence[i] > sequence[j]) {
                result[i] = max(result[i], result[j] + 1);
            }
        }
    }
}
