class Graph:
    def __init__(self):
        # initialize the empty dictionary to store adjacency list
        self.adjacencyList = {}

    # make the nodes with the adjacency list ex: 1: [] 2:[1,3]
    def addNode(self, node):
        # add node to the graph
        if node not in self.adjacencyList:
            self.adjacencyList[node] = []

    # make the edge between the graph
    def makeEdge(self, node1, node2):
        # if not nodes are created,create the node
        if node1 not in self.adjacencyList:
            self.addNode(node1)
        if node2 not in self.adjacencyList:
            self.addNode(node2)

        # get the node adjacency list and add it to the list
        self.adjacencyList[node1].append[node2]
        self.adjacencyList[node2].append[node1]

    # remove the edge between nodes
    def removeEdge(self, node1, node2):
        # if node1 in the list and node2 in the list node1
        if node1 in self.adjacencyList and node2 in self.adjacencyList[node1]:
            self.adjacencyList[node1].remove(node2)

        if node2 in self.adjacencyList and node1 in self.adjacencyList[node2]:
            self.adjacencyList[node2].remove(node1)

    def removeNode(self, node):
        # remove all adjacencyList connected nodes
        if node in self.adjacencyList:
            for nodes in self.adjacencyList[node]:
                self.adjacencyList[node].remove(nodes)

        # the delete the node itself
        del self.adjacencyList[node]

    # get the neighbors
    def getNeighbors(self, node):
        return self.adjacencyList.get(node, [])

    # make the string representation of the graph
    def __str__(self):
        return '\n'.join(f'{node}: {neighbors}' for node, neighbors in self.adjacencyList.items())
