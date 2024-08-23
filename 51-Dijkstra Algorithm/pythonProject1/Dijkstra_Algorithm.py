import heapq


def dijkstra(graph, start_node):
    # create distances dictionary and make them inf distances
    distances = {node: float('inf') for node in graph}

    # initialize the first node as 0 distance
    distances[start_node] = 0

    priority_queue = [(0, start_node)]

    while priority_queue:
        # get the smallest possible distance and check for the other nodes
        current_distance, current_node = heapq.heappop(priority_queue)

        # if the current
        if current_distance > distances[current_node]:
            pass

        for neighbor, weight in graph[current_node]:
            # calculate the distance from the current node to his neighbour
            distance = current_distance + weight

            if distance < distances[neighbor]:
                # if the distance is less than current distance then update the distance
                distances[neighbor] = distance
                # add to the priority queue
                heapq.heappush(priority_queue, (distance, neighbor))

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
