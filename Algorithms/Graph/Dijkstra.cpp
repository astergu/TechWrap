/**
 * Dijkstra algorithm.
 */

#include <iostream>
#include <limits>
using namespace std;

int minDistance(int dist[], bool sptSet[], int V) {
    int minValue = std::numeric_limits<int>::max();
    int minIdx = 0;
    for (int v = 0; v < V; v++) {
        if (!sptSet[v] && dist[v] <= minValue) {
            minValue = dist[v];
            minIdx = v;
        }
    }
    return minIdx;
}

void printSolution(int dist[], int V) {
    cout << "Print Distance of Vertex: " << endl;
    for (int i = 0; i < V; i++) {
        cout << dist[i] << endl;
    }
}

void dijkstra(int graph[][9], int V, int src) {
    int dist[V]; // dist[i] will hold the shortest distance from src to i
    bool sptSet[V];  // sptSet[i] will be true if vertex i is included
                     // in shortest path tree

    // initialize the arrays
    for (int i = 0; i < V; ++i) {
        dist[i] = std::numeric_limits<int>::max();
        sptSet[i] = false;
    }

    dist[src] = 0;
    for (int c = 0; c < V - 1; c++) {
        int u = minDistance(dist, sptSet, V);
        sptSet[u] = true;
        for (int v = 0; v < V; v++) {
            if (!sptSet[v] && graph[u][v] && dist[u] != std::numeric_limits<int>::max() && dist[u] + graph[u][v] < dist[v]) {
                dist[v] = dist[u] + graph[u][v];
            }
        }
    }

    printSolution(dist, V);
}

int main()
{
   /* Let us create the example graph discussed above */
   int graph[][9] = {{0, 4, 0, 0, 0, 0, 0, 8, 0},
                      {4, 0, 8, 0, 0, 0, 0, 11, 0},
                      {0, 8, 0, 7, 0, 4, 0, 0, 2},
                      {0, 0, 7, 0, 9, 14, 0, 0, 0},
                      {0, 0, 0, 9, 0, 10, 0, 0, 0},
                      {0, 0, 4, 14, 10, 0, 2, 0, 0},
                      {0, 0, 0, 0, 0, 2, 0, 1, 6},
                      {8, 11, 0, 0, 0, 0, 1, 0, 7},
                      {0, 0, 2, 0, 0, 0, 6, 7, 0}
                     };

    dijkstra(graph, 9, 0);

    return 0;
}
