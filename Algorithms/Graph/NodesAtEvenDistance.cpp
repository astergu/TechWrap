/**
 * https://practice.geeksforgeeks.org/problems/nodes-at-even-distance/0
 *
 * Given a connected acyclic graph with N nodes and N-1 edges, find out the pair of nodes that are at even distance from each other.

Input:

The first line of input contains an integer T denoting the number of test cases.

First line of each test case contains a single integer N denoting the number of nodes in graph.

Second line of each test case contains N-1 pair of nodes xi , yi denoting that there is an edges between them.


Output:

For each test case output a single integer denoting the pair of nodes which are at even distance.

* Constraints:

        1<=T<=10
        1<=N<=10000
        1<=xi,yi<=N
*/


#include <iostream>
#include <tuple>
#include <vector>
#include <list>
using namespace std;

int numberOfPairs(vector< tuple<int, int> > edges, int n) {
    list<int> *adj = new list<int>(n);
    for (int i = 0; i < edges.size(); ++i) {
        int v = get<0>(edges[i]);
        int w = get<1>(edges[i]);
        adj[v].push_back(w);
    }

    vector<bool> visited(n, false);
    // dfs
    for (list<int>::iterator it = adj->begin(); it != adj->end(); ++it) {
    }
    
    return 0;
}

void dfs(const list<int> *adj, int i, vector<bool>& visited) {

}


int main() {
	//code
    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        vector< tuple<int, int> > edges;
        for (int i = 0; i < n - 1; ++i) {
            int a, b;
            cin >> a >> b;
            edges.push_back(std::make_tuple(a, b));
        }

        numberOfPairs(edges, n);
        //for (int i = 0; i < edges.size(); ++i) {
        //    cout << "(" << get<0>(edges[i]) << ", " << get<1>(edges[i]) << ")" << endl;
        //}
    }

	return 0;
}

