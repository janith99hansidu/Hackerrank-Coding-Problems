def floyd_warshall(graph):
    # check the graph by going from another intermediate vertex
    v = len(graph)
    
    # 1. copy from the given graph
    distances = [row[:] for row in graph]

    # 2. going through a intermediate node
    for k in range(v):
        for i in range(v):
            for j in range(v):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
    
    return distances

if __name__ == "__main__":
    # sample input 
    INF = float('inf')
    graph = [
        [0, 1, 10, INF],  
        [INF, 0, 3, INF],  
        [INF, INF, 0, 2],  
        [INF, INF, INF, 0]
    ]

    # calculate the shortest path 
    floyd_warshall(graph)