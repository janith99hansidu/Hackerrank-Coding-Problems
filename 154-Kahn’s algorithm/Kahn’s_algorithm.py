# Kahn’s algorithm is used to find the topological order in given directed graph
# Algorithm keep track of the in degree of a node
# if node is 0 degree then it push to the queue
# pop a node from queue and for its neighbors decrease the in degree from that node
from collections import deque

def topological_sort(graph, n):
    # make a degree list to comparison
    in_degree = [0] * n
    
    for list_nodes in graph:
        # fill the in degree 
        for vertex in list_nodes:
            in_degree[vertex] += 1
    
    # get only the zero in_degree
    queue = deque([])
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)
    
    result = []
    while queue:
        # pop out a node from queue
        node = queue.popleft()
        result.append(node)
        
        # for its neighbors decrease the in_degree
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result


if __name__ == "__main__":
    # number of nodes 
    n = 6  

    # edges in graph
    edges = [[0, 1], [1, 2], [2, 3], [4, 5], [5, 1], [5, 2]]

    # graph represented as an adjacency list
    adj = [[] for _ in range(n)]

    # constructing adjacency list
    for edge in edges:
        adj[edge[0]].append(edge[1])

    # performing topological sort
    print("Topological sorting of the graph:", end=" ")
    result = topological_sort(adj, n)
    print(result)