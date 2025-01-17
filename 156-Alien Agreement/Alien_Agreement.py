from collections import deque

def bfs(parent, source, sink, graph):
    # create variables visited and make a queue
    visited = [False] * (sink + 1)
    # insert the sink node to the queue
    queue = deque([source])
    visited[source] = True

    while queue:
        # get the node from the queue
        node = queue.popleft()

        # get the neighbors 
        for neighbor in range(source + sink + 1):
            if graph[node][neighbor] and not visited[neighbor]:
                # add to the queue and parent change
                queue.append(neighbor)
                visited[neighbor] = True
                parent[neighbor] = node

                # if traverse to the sink node
                if neighbor == sink:
                    return True
    
    return False


def edmonds_karp(graph, source, sink):
    
    # while bfs get the parent and augment the paths while there is a available path do the traversal
    parents = {u:None for u in range(n+m+2)}
    # mark as total maximum 
    max_flow = 0

    while bfs(parents, source, sink, graph):
        # revese the possible edges
        u = sink
        
        while parents[u] != None:
            # traverse backward to the starting node
            v = parents[u]
            graph[v][u] = 0
            graph[u][v] = 1
            u = v
        
        # increase the maxflow count
        max_flow += 1

    return max_flow 


if __name__ == "__main__":
    
    # number of nodes in s(n) and nuber of nodes in 
    n,m = 3,3
    source_node = 0
    sink_node = n+m+1
    # list of edges in biparatie graph
    edges = [(1, 4), (2, 5), (3, 5), (3, 6)] 
    
    # make the graph with given edges as adjacency matrix
    graph = [[0]* (n+m+2) for _ in range(m+n+2)]
    for u, v in edges:
        graph[u][v] = 1
    
    # link first half to the source and next to the sink
    for i in range(1, n+1):
        graph[source_node][i] = 1
    
    for i in range(n+1, n+m+2):
        graph[i][sink_node] = 1 

    # call the function in the graph
    print(edmonds_karp(graph, source_node, sink_node))