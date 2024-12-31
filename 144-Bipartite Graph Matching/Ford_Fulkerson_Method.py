from collections import deque

def bfs(source, sink, residual_graph, parent):
    # make queue and append the first node
    # mark as visited for the first node
    # get the first level visit them and put to the queue
    # repeat
    visited = set() 
    queue = deque([source])
    visited.add(source)
    
    while queue:
        # get a node from the queue
        next_node = queue.popleft()
        
        for neighbor, capacity in residual_graph[next_node].items():
            if capacity > 0 and neighbor not in visited:
                # mark as visited and update the parent
                parent[neighbor] = next_node
                visited.add(neighbor)
                
                # if the sink node found return true
                if neighbor == sink:
                    return True
    
    return False
    

def ford_fulkerson(graph, source, sink):
    
    # make the residual graph from the given graph
    residual_graph = {u: {} for u in graph.keys()}
    
    # fill the residual graph
    for node in graph:
        for u, capacity in graph[node].items():
            # update the forward path
            residual_graph[node][u] = capacity
            # update the backward path
            residual_graph[u][node] = capacity
    
    # accumulate flow
    max_flow = 0
    parent = {} 
    
    while bfs(source, sink, residual_graph, parent):
        # if a path found update get the bottle neck value of the path 
        # then update the residual graph
        # add to the max flow
        bottle_neck = float('inf')
        s = sink
        
        while s != source:
            bottle_neck = min(bottle_neck, residual_graph[parent[s]][s])
            s = parent[s]
        
        # update residual graph
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= bottle_neck
            residual_graph[v][u] += bottle_neck
            v = u

        max_flow += bottle_neck

    print(max_flow)
    return 

if __name__ == "__main__":
    
    # make the graph 
    graph = {
        'S': {'A': 10, 'B': 5},
        'A': {'B': 15, 'T': 10},
        'B': {'T': 10},
        'T': {}
    }
    
    # call the function 
    ford_fulkerson(graph, "S", "T")