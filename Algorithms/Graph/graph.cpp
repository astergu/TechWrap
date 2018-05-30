#include "Graph.h"
#include <queue>
#include <iostream>
using namespace std;


Graph::Graph(int V) {
    this->V = V;
    adj = new list<int>[V];
}

void Graph::addEdge(int v, int w) {
    adj[v].push_back(w);
}

void Graph::bfs(int s) {
    queue<int> nodes;
    vector<bool> visited(V, false);
    nodes.push(s);
    visited[s] = true;

    while (nodes.size() > 0) {
        int curr = nodes.front();
        cout << curr << endl;
        nodes.pop();
        for (list<int>::iterator i = adj[curr].begin(); i != adj[curr].end(); ++i) {
            if (!visited[*i]) {
                visited[*i] = true;
                nodes.push(*i);
            }
        }
    }
}

void Graph::dfs(int s) {
    vector<bool> visited(V, false);
    cout << s << endl;
    dfsUtil(s, visited);
}

void Graph::dfsUtil(int s, vector<bool>& visited) {
    visited[s] = true;
    for (list<int>::iterator it = adj[s].begin(); it != adj[s].end(); ++it) {
        if (!visited[*it]) {
            cout << *it << endl; 
            dfsUtil(*it, visited);
        }
    }
}


void Graph::printGraph() {
    for (int i = 0; i < V; ++i) {
        cout << i;
        for (list<int>::iterator it = adj[i].begin(); it != adj[i].end(); ++it) {
            cout << "->" << *it;
        }
        cout << endl;
    }
}
