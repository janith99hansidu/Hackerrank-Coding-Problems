# if a node found explore the node
# until the end
def dfs(graph, node):
    # make variables to track the progress
    visited = {n: False for n in graph.keys()}
    # make a stack to append the visited nodes
    stack = [node]

    while stack:
        current_node = stack.pop()
        # mark as visit and print out
        visited[current_node] = True
        print(current_node)

        for neighbor in reversed(graph[current_node]):
            # if the current neighbor not visited add to the stack
            if not visited[neighbor]:
                stack.append(neighbor)

    return

if __name__ == "__main__":
    # Example graph represented as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    print("DFS Traversal:")
    dfs(graph, 'A') 