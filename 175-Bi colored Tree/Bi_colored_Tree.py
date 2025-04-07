import heapq

def dijkstra(graph: dict, start, end):
    # calculate the shortest distance to one node to another node
    # initialize the variables 
    distance = {key:float('inf') for key in graph.keys()}
    distance[start] = 0
    priority_queue = [(0,start)]
    parents = {key: None for key in graph.keys()}

    while priority_queue:
        # if pop distance is smaller than the current distance
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_node == end:
            break
        
        # traverse the next nodes
        for neighbor in graph[current_node].keys():
            next_node, next_distance = neighbor, graph[current_node][neighbor]

            # calculate the next value
            next_cal_distance = current_distance + next_distance
            
            # put to the next value
            if next_cal_distance < distance[next_node]:
                # update the distance
                distance[next_node] = next_cal_distance

                # update the parent 
                parents[next_node] = current_node

                # add to the queue
                heapq.heappush(priority_queue,(next_cal_distance, next_node))
    
    return distance, parents

if __name__ =="__main__":
    graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'D': 4, 'C':2},
    'C': {'A': 1, 'D': 7, 'B':2},
    'D': {'B': 4, 'C': 7}
    }
    colors = {'A':1,'B':1,'C':0,'D':0}

    start = 'A'
    end = 'D'
    # call the function 
    _, parents = dijkstra(graph,'A','D')

    # traverse back ward and calculate the number of blue colored 
    total = 0
    i = end
    while parents[i] != None:
        total += colors[i]
        i = parents[i]
    total += colors[start]

    # total blue colored nodes to start to end
    print(total)

