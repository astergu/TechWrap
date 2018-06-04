/**
 * Given a graph with N nodes and M directed edges. Your task is to complete the function kosaraju which returns an integer denoting the no of strongly connected components in the graph.

Input:
The first line of input contains an integer T. Then T test cases follow. Each test case contains two integers N and M . In the next line are N space separated values u,v denoting an edge from u to v.

Output:
For each test case in a new line output will an integer denoting the no of strongly connected components present in the graph.
 */

#include <iostream>
#include <vector>
#include <stack>
using namespace std;

#define MAX 10001

void dfs(vector<int> g[], int N, vector<bool>& visited, int s, stack<int>& nstak);
vector<int>* getTranspose(vector<int> graph[], int N, int M);

    
void printGraph(vector<int> g[], int N) {
    cout << "____________ Graph ___________" << endl;
    for (int i = 0; i < N; ++i) {
        cout << i;
        for (int j = 0; j < g[i].size(); ++j) {
            cout << "->" << g[i][j];
        }
        cout << endl;
    }
}

int kosaraju(vector<int> g[MAX], int N, int M)
{
    // Your code here
    stack<int> nstack;
    vector<bool> visited(N + 1, false);
    
    // fill the stack
    for (int i = 1; i <= N; ++i) {
        if (!visited[i]) {
            dfs(g, N, visited, i, nstack);
        }
    }


    vector<int>* tgraph = getTranspose(g, N, M); 
    for (int i = 1; i <= N; ++i) {
        visited[i] = false;
    }

    cout << "Find SCCs" << endl;
    // print the stack
    //cout << "_____ stack _____ " << endl;
    //while (!nstack.empty()) {
    //    cout << nstack.top() << endl;
    //    nstack.pop();
    //}
    int sccCount = 0;
    while (!nstack.empty()) {
        int v = nstack.top();
        nstack.pop();
        if (!visited[v]) {
            cout << v << " not visited, incre SCC" << endl;
            sccCount++;
            dfs(tgraph, N, visited, v, nstack);
        }
    }
    
    cout << "SCC Count: " << sccCount << endl;
    return sccCount;
}

void dfs(vector<int> g[], int N, vector<bool>& visited, int s, stack<int>& nstack) {
    visited[s] = true;
    for (vector<int>::iterator it = g[s].begin(); it != g[s].end(); ++it) {
        if (!visited[*it]) {
            dfs(g, N, visited, *it, nstack);
        }
    }
    nstack.push(s);
}

vector<int>* getTranspose(vector<int> graph[], int N, int M) {
    vector<int> *tgraph = new vector<int>[N + 1];

    for (int i = 1; i < N + 1; ++i) {
        for (int j = 0; j < graph[i].size(); ++j) {
            int dest = graph[i][j];
            tgraph[dest].push_back(i);
        }
    }
    return tgraph;
}


int main() {
    int T;
    cin >> T;
    while (T--) {
        int n, m;
        cin >> n >> m;
        vector<int> g[10001];

        for (int i = 0; i < m; ++i) {
            int a, b;
            cin >> a >> b;
            g[a].push_back(b);
        }

        kosaraju(g, n, m);
        //cout << "-----------Strongly connected components----------\n" << kosaraju(g, n, m) << endl;
    }

    return 0;
}
