from collections import deque, defaultdict


def bfs_graph(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()

        # get the left element of the queue and add to the visited set
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)

            # add the neighbors to the queue
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)


if __name__ == '__main__':
    # Example usage:
    graph = defaultdict(list)
    graph['A'].extend(['B', 'C'])
    graph['B'].extend(['D', 'E'])
    graph['C'].extend(['F'])
    graph['D'].extend([])
    graph['E'].extend(['F'])
    graph['F'].extend([])

    bfs_graph(graph, 'A')
