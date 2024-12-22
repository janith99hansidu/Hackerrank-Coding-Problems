from collections import deque

# check whether a path exist with source to sink with capacity more than > 0
# bfs guarantee to find the shortest path between source and sink
# because it get the first occurrence in depth 
def bfs(residual_graph, source, sink, parent):
    # check whether a path exist with in source to sink 
    # update each parent node
    # already visited nodes update 
    visited = set()
    # queue to traverse along bfs
    queue = deque([source])
    visited.add(source)
    
    while queue:
        node = queue.popleft()
        # traverse to the neighbors
        for neighbor, capacity in residual_graph[node].items():
            # if the capacity > 0 can add to the queue 
            if neighbor not in visited and capacity > 0:
                # only one node is visiting one time so there is no clash in parents
                parent[neighbor] = node
                if neighbor == sink:
                    return True
                # mark as visited
                visited.add(neighbor)
                queue.append(neighbor)
    
    return False

def ford_fulkerson(graph, start_node, end_node):
    # initialize the residual graph with dictionary 
    residual_graph = {u:{} for u in graph}
    # then initialize the graph with capacity 
    for u in graph:
        for neighbor, capacity in graph[u].items():
            residual_graph[u][neighbor] = capacity
            residual_graph[neighbor][u] = 0

    # initialize the maximum flow of the graph
    max_flow = 0
    parent = {}
    
    while bfs(residual_graph, start_node, end_node, parent):
        # find the bottle neck capacity
        path_flow = float('inf')
        s = end_node
        
        # back track along the shortest path
        while s != start_node:
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            # go to the backward
            s = parent[s]         

        # update the residual capacities
        v = end_node
        while v != start_node:
            u = parent[v]
            residual_graph[v][u] += path_flow
            residual_graph[u][v] -= path_flow
            # traverse backward
            v = parent[v]
        max_flow += path_flow  
    
    return max_flow      

if __name__ == "__main__":
    
    # forward graph
    graph = {
        'S': {'A': 10, 'B': 5},
        'A': {'B': 15, 'T': 10},
        'B': {'T': 10},
        'T': {}
    }

    print("Maximum Flow:", ford_fulkerson(graph, 'S', 'T'))