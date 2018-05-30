
#ifndef _WEIGHTED_GRAPH_H_
#define _WEIGHTED_GRAPH_H_

#include <vector>
using namespace std;


class WeightedGraph {
public:
    WeightedGraph(int V);

    void addEdge(int v, int w, float weight);

    void bfs(int s);
    void dfs(int s);
    void printGraph();

private:
    void dfsUtil(int s, vector<bool>& visited);

private:
    int V;
    vector<std::pair<int, float> > *adj;
};

#endif
