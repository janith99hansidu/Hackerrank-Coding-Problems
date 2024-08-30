class UnionFind:
    def __init__(self, n):
        # make a root list for each node
        self.roots = list(range(n + 1))
        # make the rank of the graph
        self.rank = [0 for _ in range(n + 1)]

    def findRoot(self, node):
        # if the root and the node are equal return the root
        if node == self.roots[node]:
            return node

        # else call the findRoot function on the root[n]
        self.roots[node] = self.findRoot(self.roots[node])
        return self.roots[node]

    def union(self, node1, node2):
        root_node1 = self.findRoot(node1)
        root_node2 = self.findRoot(node2)

        if root_node1 != root_node2:

            if self.rank[root_node1] > self.rank[root_node2]:
                self.roots[root_node2] = root_node1
            elif self.rank[root_node1] < self.rank[root_node2]:
                self.roots[root_node1] = root_node2
            else:
                self.roots[root_node2] = root_node1
                self.rank[root_node1] += 1


def prims(n, edges, start):
    # sort the edge list to asc
    edges.sort(key=lambda x: x[2])

    # make the graph
    graph = UnionFind(n)

    # count the total value of prims subtree
    total_weight = 0
    for u, v, weight in edges:
        # when connecting edges search whether they have same roots
        if graph.findRoot(u) != graph.findRoot(v):
            graph.union(u, v)
            total_weight += weight

    print(total_weight)


if __name__ == '__main__':
    edges = [[1, 3, 3], [1, 2, 2], [2, 3, 2]]
    prims(3, edges, 1)
