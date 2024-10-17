from collections import defaultdict

def cutTheTree(data, edges):
    # Step 1: Build the graph from the given edges
    graph = defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    # Step 2: Create a dictionary to store the subtree sum for each node
    reslt_dict = {}  # This will hold the total sum of the subtree rooted at each node
    visited = [False] * (len(data) + 1)  # Track visited nodes, adjusted for 1-based indexing

    # Step 3: Define DFS function
    def dfs(node):
        # Mark the node as visited
        visited[node] = True
        # Start with the current node's value
        result = data[node - 1]  # Node values are 1-based, so data[node - 1]
        
        # Visit all its neighbors
        for neighbour in graph[node]:
            if not visited[neighbour]:
                result += dfs(neighbour)
        
        # Store the result in the reslt_dict for the current node
        reslt_dict[node] = result
        return result

    # Start DFS from any node, for example, node 1 (you can start from any node because it's a tree)
    dfs(1)
    
    total_sum = sum(data)  # Total sum of all the nodes
    min_diff = float('inf')  # Initialize the minimum difference
    
    # Step 4: Calculate the minimum difference
    for node in range(1, len(data) + 1):
        subtree_sum = reslt_dict[node]
        diff = abs(total_sum - 2 * subtree_sum)  # Difference between two parts when cut
        min_diff = min(min_diff, diff)
    
    return min_diff

if __name__ == '__main__':
    # Input parsing and handling
    n = int(input().strip())  # Number of nodes

    data = list(map(int, input().rstrip().split()))  # Values of the nodes

    edges = []
    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))  # Edges of the tree

    result = cutTheTree(data, edges)
    print(result)
