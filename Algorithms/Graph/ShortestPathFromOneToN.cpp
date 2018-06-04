/**
 * Consider a directed graph whose vertices are numbered from 1 to n. There is an edge from a vertex i to a vertex j iff either j = i + 1 or j = 3i. The task is to find the minimum number of edges in a path in G from vertex 1 to vertex n.

Input: 
    The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows.

    Each test case contains a value of n. 

Output: 
    Print the number of edges in the shortest path from 1 to n.

Constraints:
    1<=T<=30
    1<=n <=1000
 */

#include <iostream>
using namespace std;

int numberOfEdges(int n) {
    int curr = 1;
    if (n == 1) 
        return 0;
    if (n == 2)
        return 1;

    int steps[n + 1];
    steps[0] = 0;
    steps[1] = 0;
    steps[2] = 1;
    for (int i = 3; i <= n; ++i) {
        steps[i] = n + 1;
    }

    for (int i = 3; i <= n; ++i) {
        int divThree = i / 3;
        steps[i] = std::min(steps[i-1] + 1, steps[divThree] + (i - divThree * 3 + 1));
    }

    return steps[n];
}


#include <iostream>
using namespace std;

int main() {
	//code
	int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        int ret = numberOfEdges(n);
        cout << ret << endl;
    }

    return 0;
}
