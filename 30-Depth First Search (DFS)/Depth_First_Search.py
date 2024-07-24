from collections import deque, defaultdict


def dfs_graph(graph, start):
    visited = set()
    stack = deque([start])

    while stack:
        vertex = stack.pop()

        # if the vertex is not visited
        # mark as visited and add neighbors to the stack
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=" ")

            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)


if __name__ == '__main__':
    graph = defaultdict(list)
    graph['A'].extend(['B', 'C'])
    graph['B'].extend(['D', 'E'])
    graph['C'].extend(['F'])
    graph['D'].extend([])
    graph['E'].extend(['F'])
    graph['F'].extend([])

    dfs_graph(graph, 'A')
