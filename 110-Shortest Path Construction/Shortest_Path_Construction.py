import heapq

# get the shortest path by dijkstra algorithm
def dijkstra(graph, start, end):
    
    # make a dict to store shortest path
    shortest_path_dict = {node: float('inf') for node in graph.keys()}
    shortest_path_dict[start] = 0
    
    # make a dict to store the path of prev taversed element
    prev = {node: None for node in graph.keys()}
    
    # make a priority queue and put the start node
    pq = [(0, start)]

    while pq:
        # get the less distance at first
        distance, node = heapq.heappop(pq)
        
        # if the get node was the last
        if node == end:
            break
        
        # neighbours in graph update the distance if the distance is smaller than current distance 
        for neighbour in graph[node]:
            next_node, current_distance = neighbour
            
            # calculate the current_possible_distance
            current_possible_distance = current_distance + distance
            
            # if the total distance is less than the shortest_path_dict 
            if current_possible_distance < shortest_path_dict[next_node]:
                # update the shortest path
                shortest_path_dict[next_node] = current_possible_distance
                
                # updatet the prev table to store previous node that came from
                prev[next_node] = node 
                
                # add to the queue
                heapq.heappush(pq, (current_possible_distance, next_node))
                
    # reconstruct the path
    path = []
    current = end
    
    while current != None:
        # add to the path and back step to prev node
        path.append(current)
        # back traverse
        current = prev[current]
     
    return path[::-1], shortest_path_dict[end]

if __name__ == '__main__':
    
    # Define the roads as adjacency list
    roads = {
        "A": [("B", 10), ("C", 20)],
        "B": [("A", 10), ("C", 5), ("D", 10)],
        "C": [("B", 5), ("A", 20), ("D", 2)],
        "D": [("B", 10), ("C", 2)]
    }
    
    # define the start and end positions 
    start = "A"
    end = "D"
    shortest_path, cost = dijkstra(roads, start, end)
    
    print(shortest_path, cost)