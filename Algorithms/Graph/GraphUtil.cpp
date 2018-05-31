#include "Graph.h"
#include <stack>
#include <vector>
#include <iostream>
using namespace std;

void transposeGraph(const self::Graph& graph,  self::Graph* tgraph) {
    int V = graph.getV();
    tgraph = new self::Graph(V);
    list<int>* edges = graph.getEdges();
    for (int i = 0; i < V; ++i) {
        for (list<int>::iterator it = edges[i].begin(); it != edges[i].end(); ++i) {
            tgraph->addEdge(*it, i);
        }
    }
}

// iterative implementation of dfs
void dfsIterative(const self::Graph& graph, int s) {
    int V = graph.getV();
    vector<bool> visited(V, false);
    list<int>* edges = graph.getEdges();
    stack<int> nodes;
    nodes.push(s);

    while (!nodes.empty()) {
        s = nodes.top();
        nodes.pop();
        cout << s << endl;
        visited[s] = true;

        for (list<int>::iterator it = edges[s].begin(); it != edges[s].end(); ++it) {
            if (!visited[*it]) {
                nodes.push(*it);
            }
        }
    }
}


int main() {
    self::Graph g(5); // Total 5 vertices in graph
    g.addEdge(1, 0);
    g.addEdge(0, 2);
    g.addEdge(2, 1);
    g.addEdge(0, 3);
    g.addEdge(1, 4);

    dfsIterative(g, 0);
    return 0;
}
