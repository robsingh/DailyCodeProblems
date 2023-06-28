"""
This problem was asked by Dropbox.

Given an undirected graph G, check whether it is bipartite. 
Recall that a graph is bipartite if its vertices can be divided into two independent sets, U and V, such that no edge connects vertices of the same set.
"""

"""
Thinking: 
We can use either BFS or DFS. 
Idea is to assign colors to the vertices of the graph in such a way that no two adjacent vertices have the same color.
If it is possible to color ALL the vertices of graph, then the graph is bipartite.
"""

from collections import deque

def is_bipartite(graph):
    # initialize an empty dictionary ro store the colors of vertices
    colors = {}

    # choose an abitrary vertex as the starting point
    start_vertex = list(graph.keys())[0]

    # assign the starting vertex color 1
    colors[start_vertex] = 1

    # create a queue for BFS and enqueue the starting index
    queue = deque([start_vertex])

    # perform BFS
    while queue:
        vertex = queue.popleft()

        for neighbour in graph[vertex]:
            if neighbour not in colors:
                # assign the opposite color to the neighbour
                colors[neighbour] = 3 - colors[vertex]
                queue.append(neighbour)
            elif colors[neighbour] == colors[vertex]:
                return False
            
    # if all vertices have been visited without conflicts, graph is bipartite
    return True


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

result = is_bipartite(graph)
print(result)


