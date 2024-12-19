from collections import defaultdict
import heapq

def beautifulPath(edges, A, B):
    # build the graph
    graph = defaultdict(list)
    for a, b, cost in edges:
        graph[a].append((b, cost))
        graph[b].append((a, cost))
    
    # priority queue for Dijkstra-like traversal
    heap = [(0, A)]  # (current penalty, current node)
    visited = set()  # set to track visited nodes with a specific penalty

    while heap:
        current_penalty, node = heapq.heappop(heap)

        # if we reached the destination, return the penalty
        if node == B:
            return current_penalty

        # avoid revisiting the same state (node, penalty)
        if (node, current_penalty) in visited:
            continue
        visited.add((node, current_penalty))

        # explore neighbors
        for neighbor, edge_penalty in graph[node]:
            new_penalty = current_penalty | edge_penalty
            heapq.heappush(heap, (new_penalty, neighbor))

    # if no path exists
    return -1

        
if __name__ == '__main__':
    
    # handle the inputs
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    second_multiple_input = input().rstrip().split()

    A = int(second_multiple_input[0])

    B = int(second_multiple_input[1])

    result = beautifulPath(edges, A, B)
    
    print(result)
