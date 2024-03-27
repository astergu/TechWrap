/**
 * The Algorithm Design Manual
 * Chapter 5: Graph Traversal
 * 
*/
#define MAXV 1000  /* maximum number of vertices */

typedef struct {
    int y;              /* adjacency info */
    int weight;         /* edge weight, if any */
    struct edgenode *next;  /* next edge in list */
} edgenode;

typedef struct {
    edgenode *edges[MAXV + 1];  /* adjacency info */
    int degree[MAXV + 1];       /* outdegree of each vertex */
    int nvertices;              /* number of vertices in graph */
    int nedges;                 /* number of edges in graph */
    bool directed;              /* is the graph directed? */
} graph;


void initialize_graph(graph *g, bool directed) {
    int i;      /* counter */
    g->nvertices = 0;
    g->nedges = 0;
    g->directed = directed;

    for (int i = 1; i <= MAXV; i++) 
        g->degree[i] = 0;
    for (int i = 1; i < MAXV; i++)
        g->edges[i] = nullptr;
}