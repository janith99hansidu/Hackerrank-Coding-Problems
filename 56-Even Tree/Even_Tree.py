def evenForest(t_nodes, t_edges, t_from, t_to):
    # import the default dict to create adjacency list of graph
    from collections import defaultdict

    # make a default dict of list type
    tree = defaultdict(list)
    for u, v in zip(t_from, t_to):
        # add u in the key of v
        tree[v].append(u)
        # add v in the key of u
        tree[u].append(v)

    # initialize variables
    visited = [False] * (t_nodes + 1)
    subtree_size = [0] * (t_nodes + 1)
    removable_edges = 0

    # preform depth first search
    def dfs(node):
        nonlocal removable_edges
        visited[node] = True
        subtree_size[node] = 1

        # traverse each subtree and fill the subtree size table for each subtree with root of node
        for neighbour in tree[node]:
            if not visited[neighbour]:
                subtree_size[node] += dfs(neighbour)

        # add if the subtree size in divide by 2
        if node != 1 and subtree_size[node] % 2 == 0:
            removable_edges += 1

        return subtree_size[node]

    # start with node 1
    dfs(1)

    # Return the total number of removable edges
    return removable_edges


if __name__ == '__main__':
    # sample input
    t_nodes = 10
    t_edges = 9
    t_from = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    t_to = [1, 1, 3, 2, 1, 2, 6, 8, 8]

    print(evenForest(t_nodes, t_edges, t_from, t_to))  # Output: 2