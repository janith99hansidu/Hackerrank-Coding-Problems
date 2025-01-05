from collections import defaultdict
import heapq
# use dijkstra algorithm to get the minimum 
# instead of adding the path value use given logic to solve the problem 

def getCost(g_nodes, g_from, g_to, g_weight):
    # Print your answer within the function and return nothing
    
    # make the graph
    graph = defaultdict(list)
    for u, v, cost in zip(g_from, g_to, g_weight):
        graph[u].append((v, cost))
        graph[v].append((u, cost))
    # print(graph)
    
    # do the altered dijkstra to find the answer
    # initialize the shortest paths variables 
    shortest_paths = {x: float("inf") for x in range(1, g_nodes+1) }
    start = 1
    end = g_nodes
    
    shortest_paths[start] = 0
    
    # make a heap to always get the shortest
    # add start node to the heap
    # heap save the data as (cost, node)
    heap = [(0, start)]
    visited = set()
    
    while heap:
        # get the current shortest distance node from given heap
        current_cost, current_node = heapq.heappop(heap)
        # mark as visited
        visited.add(current_node)
        
        # for his neighbors check the condition and update the distance
        for neighbors in graph[current_node]:
            
            # unpack the variables
            neighbor, neighbor_cost = neighbors
            
            # check the neighbor is not visited
            if neighbor not in visited:
                
                # check the maximum path cost is new node or previous node
                if neighbor_cost > current_cost and neighbor_cost < shortest_paths[neighbor]:
                    shortest_paths[neighbor] = neighbor_cost
                elif neighbor_cost < shortest_paths[neighbor]:
                    shortest_paths[neighbor] = current_cost

                # add to the heapq
                heapq.heappush(heap, (shortest_paths[neighbor], neighbor))
                
    print(shortest_paths[end])
    return
    
if __name__ == '__main__':
    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    getCost(g_nodes, g_from, g_to, g_weight)
    