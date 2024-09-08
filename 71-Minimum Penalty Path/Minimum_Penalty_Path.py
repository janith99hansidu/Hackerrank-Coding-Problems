from collections import deque, defaultdict
import heapq


def beautifulPath(edges, A, B):
    # make the graph from the edges
    graph = defaultdict(list)
    for u, v, p in edges:
        graph[u].append((v, p))
        graph[v].append((u, p))

    # make the priority queue and get from that according to less cost
    pq = [(0, A)]  # penalty, node
    visited = set()

    while pq:
        penalty, node = heapq.heappop(pq)

        # if reach the node B
        if node == B:
            return penalty

        if node in visited:
            continue

        visited.add(node)

        for neighbor, edge_penalty in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (penalty | edge_penalty, neighbor))

    return -1


if __name__ == '__main__':
    edges = [
        (1, 2, 1),
        (1, 2, 1000),
        (2, 3, 3),
        (1, 3, 100)
    ]

    A, B = 1, 3
    print(beautifulPath(edges, A, B))
