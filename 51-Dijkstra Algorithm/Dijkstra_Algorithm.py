import heapq


def dijkstra(graph, start_node):
    # first initialize the distances as inf in the dict
    distances = {node: float('inf') for node in graph}

    # initialize the starting node to distance of 0
    distances[start_node] = 0
    # add the first node to the priority queue
    priority_queue = [(0, start_node)]

    while priority_queue:
        # pop back the priority_queue
        current_dist, current_node = heapq.heappop(priority_queue)

        # if current distance is greater than previously stored distance
        # ignore that value and pass it
        if current_dist > distances[current_node]:
            pass

        # if not, get the neighbours and put them in priority_queue
        for neighbour, weight in graph[current_node]:
            # calculate the distance from the current node
            distance = current_dist + weight

            if distance < distances[neighbour]:
                # save the current minimum to the distance dict
                distances[neighbour] = distance
                # add to the priority queue for later retrieval
                heapq.heappush(priority_queue, (distance, neighbour))

    return distances


if __name__ == '__main__':
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }

    start_node = 'A'
    distances = dijkstra(graph, start_node)
    print(distances)
