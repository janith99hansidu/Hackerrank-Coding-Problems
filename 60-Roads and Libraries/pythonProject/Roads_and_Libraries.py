class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def findRoot(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.findRoot(self.parent[n])  # Path compression
        return self.parent[n]

    def union(self, u, v):
        u_root = self.findRoot(u)
        v_root = self.findRoot(v)

        if u_root != v_root:
            if self.rank[u] > self.rank[v]:
                self.parent[v] = u
            elif self.rank[u] < self.rank[v]:
                self.parent[u] = v
            else:
                self.parent[v] = u
                self.rank[u] += 1


def roadsAndLibraries(n, c_lib, c_road, cities):
    # Initialize the Union-Find structure
    graph = UnionFind(n)

    # initialize total cost
    total_cost = 0

    if c_lib > c_road:
        # total paths of the connected graph
        total_paths = 0

        for u, v in cities:
            u -= 1  # Convert to 0-based index
            v -= 1
            if graph.findRoot(u) != graph.findRoot(v):
                graph.union(u, v)
                total_paths += 1

        # Find distinct roots in graph.parent
        distinct_roots = len(set(graph.findRoot(i) for i in range(n)))

        total_cost = total_paths * c_road + distinct_roots * c_lib

    else:
        total_cost = n * c_lib

    return total_cost


if __name__ == '__main__':
    cities = [[1, 2], [3, 1], [2, 3]]
    print(roadsAndLibraries(3, 2, 1, cities))
    print(roadsAndLibraries(6, 2, 5, [[1, 3], [3, 4], [2, 4], [1, 2], [2, 3], [5, 6]]))
