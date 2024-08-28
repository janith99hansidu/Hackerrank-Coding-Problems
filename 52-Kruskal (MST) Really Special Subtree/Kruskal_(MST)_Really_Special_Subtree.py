# output the total weight of the MST
class UnionFind:
    def __init__(self, n):
        # find the connected nodes by the parent
        # if two edges has same parent they are connected
        self.parent = list(range(n))
        # During the union operation different root set are found
        # set with the lower rank is attached under the root of the set with the higher rank
        self.rank = [0] * n

    # if the nodes are in   [1, 2, 3, 4]
    # if the parent list is [1, 1, 2, 3]
    # parent of the 3 is 2 so go to 2 and get the parent.
    # parent of the 2 is node 1 and go to node 1 and return 1, so it change all the nodes to parent 1
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[u] > self.rank[u]:
                self.parent[root_v] = root_u
            elif self.rank[v] < self.rank[u]:
                self.parent[root_u] = root_v
            else:
                # any other direction make the connection
                self.parent[root_v] = root_u
                # add one to connected root as it increase by one
                self.rank[root_u] += 1


def kruskals(g_nodes, g_from, g_to, g_weight):

    # make tuples of g_weight, g_from, g_to
    edges = sorted(zip(g_weight, g_from, g_to))

    # init the graph class and make an object
    uf = UnionFind(g_nodes)
    mst_weight = 0

    # union the nodes that has not same parent
    for weight, u, v in edges:
        # 0 based indexes
        u -= 1
        v -= 1
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_weight += weight

    return mst_weight


if __name__ == '__main__':
    g_nodes = 4
    g_weight = [5, 3, 6, 7, 4, 5]
    g_from = [1, 1, 4, 2, 3, 3]
    g_to = [2, 3, 1, 4, 2, 4]

    res = kruskals(g_nodes, g_from, g_to, g_weight)
    print(res)
