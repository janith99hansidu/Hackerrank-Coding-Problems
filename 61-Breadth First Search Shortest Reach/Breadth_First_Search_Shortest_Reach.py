def bfs(n, m, edges, s):
    from collections import defaultdict, deque
    graph = defaultdict(list)

    # Build the graph from edges
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Initialize queue, total cost, and visited list
    n_queue = deque()
    total_cost = [-1] * n
    visited = [False] * n

    # Put the initial value in the queue
    n_queue.append((s, 0))  # (starting node, depth)
    visited[s - 1] = True  # Mark the start node as visited

    while n_queue:
        # Dequeue the node and get the depth
        node, depth = n_queue.popleft()  # Use popleft() instead of pop()

        # Update the depth (cost) of the node
        total_cost[node - 1] = depth * 6

        # Explore neighbors
        for neighbour in graph[node]:
            if not visited[neighbour - 1]:
                visited[neighbour - 1] = True
                n_queue.append((neighbour, depth + 1))

    # Remove the start node's cost from the list
    total_cost.pop(s - 1)

    return total_cost

if __name__ == '__main__':
    # [1,2], [1, 3], [3, 4]
    bfs(5, 3, [[1, 2], [1, 3], [3, 4]], 1)
