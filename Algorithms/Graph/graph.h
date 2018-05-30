#ifndef _GRAPH_H_
#define _GRAPH_H_

#include <list>
using namespace std;


class Graph {
public:
    Graph(int V);

    void addEdge(int v, int w);

    void bfs(int s);
    void dfs(int s);
    void printGraph();

private:
    void dfsUtil(int s, vector<bool>& visited);

private:
    int V;
    list<int> *adj;
};

#endif
