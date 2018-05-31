#include <stack>
#include <vector>
#include <iostream>
using namespace std;


void topoRoutine(vector<int> graph[], int curr, vector<bool>& visited, stack<int>* topoResult);

int* topoSort(vector<int> graph[], int N) {
    stack<int> topoResult;
    vector<bool> visited(N, false);
    for (int i = 0; i < N; ++i) {
        if (!visited[i]) {
            topoRoutine(graph, i, visited, &topoResult);
        }
    }

    int* result = new int[N];
    int i = 0;
    while (!topoResult.empty()) {
        result[i++] = topoResult.top();
        topoResult.pop();
    }
    return result;
}

void topoRoutine(vector<int> graph[], int curr, vector<bool>& visited, stack<int>* topoResult) {
    visited[curr] = true;
    for (vector<int>::iterator it = graph[curr].begin(); it != graph[curr].end(); ++it) {
        if (!visited[*it]) {
            topoRoutine(graph, *it, visited, topoResult);
        }
    }
    topoResult->push(curr);
}

int main() {
    vector<int> graph[6];
    graph[5].push_back(2);
    graph[5].push_back(0);
    graph[4].push_back(0);
    graph[4].push_back(1);
    graph[2].push_back(3);
    graph[3].push_back(1);

    cout << "Following is a Topological Sort of the given graph \n";
    int* result = topoSort(graph, 6);
    for (int i = 0; i < 6; ++i) {
        cout << result[i] << " ";
    }
    cout << endl;

    return 0;
}
