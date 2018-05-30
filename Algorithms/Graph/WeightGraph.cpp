#include "WeightedGraph.h"
#include <iostream>
using namespace std;


WeightedGraph::WeightedGraph(int V) {
    this->V = V;
    adj = new vector<std::pair<int, float> >[V];
}


void WeightedGraph::addEdge(int v, int w, float weight) {
    adj[v].push_back(std::make_pair(w, weight));
}

void WeightedGraph::printGraph() {
    for (int i = 0; i < V; ++i) {
        cout << i << endl;
        vector<std::pair<int, float> >::iterator it = adj[i].begin();
        for (; it != adj[i].end(); ++it) {
            cout << "\t(" << it->first << ", " << it->second << ")" << endl;
        }
    }
}
