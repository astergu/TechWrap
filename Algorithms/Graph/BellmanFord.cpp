/**
 * Given a graph and a source vertex src in graph, find shortest paths from src to all vertices in the given graph. The graph may contain negative weight edges.
 *
 */

#include <iostream>
#include <limits>
using namespace std;

struct Edge {
    int src, dest, weight;
};

struct Graph {
    int V, E;
    struct Edge* edge;
};

struct Graph* createGraph(int V, int E) {
    struct Graph* graph = new Graph;
    graph->V = V;
    graph->E = E;
    graph->edge = new Edge[E];
    return graph;
}

void BellmanFord(struct Graph* graph, int src) {
    int V = graph->V;
    int E = graph->E;
    int dist[V];
    
    // step 1: initialize distances from src to all other vertices
    for (int i = 0; i < V; i++) {
        dist[i] = std::numeric_limits<int>::max();
    }
    dist[src] = 0;

    // step 2: relax all edges |V| - 1 times. A simple shortest
    // path from src to any other vertex can have at-most |V| - 1
    for (int i = 1; i <= V - 1; i++) {
        for (int j = 0; j < E; j++) {
            int u = graph->edge[j].src;
            int v = graph->edge[j].dest;
            int weight = graph->edge[j].weight;
            if (dist[u] != std::numeric_limits<int>::max() &&
                    dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
            }
        }
    }

    // step 3: check for negative-weight cycles. 
    // The above step guarantees shortest distance if graph
    // doesn't contain negative weight cycle. If we get
    // a shorter path, then there is a cycle.
    for (int i = 0; i < E; i++) {
        int u = graph->edge[i].src;
        int v = graph->edge[i].dest;
        int weight = graph->edge[i].weight;
        if (dist[u] != std::numeric_limits<int>::max() && dist[u] + weight < dist[v]) {
        cout << "Graph contains negative weight cycle" << endl;
        }
    }
}


int main() {
    return 0;
}

