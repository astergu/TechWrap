#ifndef _GRAPH_H_
#define _GRAPH_H_

#include <list>
#include <unordered_set>
using namespace std;

namespace self {

class Graph {
public:
    Graph(int V);

    void addEdge(int v, int w);

    void bfs(int s);
    void dfs(int s);
    void printGraph();
    int getV() const { return V; }
    list<int>* getEdges() const { return adj; }

private:
    void dfsUtil(int s, vector<bool>& visited);

private:
    int V;
    list<int> *adj;
};


class GraphUsingSet {
public:
    GraphUsingSet(int V);
    void addEdge(int src, int dest);
    void searchEdge(int src, int dest);
    void printGraph();

public:
    int V;
    unordered_set<int>* adjList;
};

}

#endif
