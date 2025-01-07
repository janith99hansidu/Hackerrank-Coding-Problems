from collections import defaultdict, deque

def find_farthest_node(start_node, tree):
    # make the relevant variables to bfs
    # track the visited nodes
    visited = set()
    visited.add(start_node)
    # make a queue to get one by one
    # queue is list of (node, depth)
    queue = deque([(start_node,0)])
    
    # save the maximum length 
    max_distance_node = None
    max_depth = 0
    
    while queue:
        # pop out the queue
        current_node, current_distance = queue.popleft()
        
        # check the current_distance is greater than the current 
        if current_distance > max_depth: 
            max_depth = current_distance
            max_distance_node = current_node
        
        # get the nodes from the its neighbors and put it in the queue
        for neighbor in tree[current_node]:
            if neighbor not in visited:
                # mark as visited
                visited.add(neighbor)
                # add to the queue
                queue.append((neighbor, current_distance + 1))
        
    
    return max_distance_node, max_depth

def tree_diameter(tree):
    # traverse from arbitrary node
    start_node, _ = find_farthest_node(1, tree)
    
    # again do bfs to get the farthest node diameter
    last_node, diameter = find_farthest_node(start_node, tree)
    
    return diameter, start_node, last_node

if __name__ == "__main__":
    # get the inputs from the node 
    tree = defaultdict(list)
    edges = [
        (1, 2),
        (1, 3),
        (2, 4),
        (2, 5)
    ]
    
    # add the edges to the graph
    for u,v in edges:
        tree[u].append(v)
        tree[v].append(u)
    
    # example call to the bfs search
    print(find_farthest_node(1, tree))
    
    # to find the diameter bfs from arbitrary node and then bfs from founded max depth node
    print(tree_diameter(tree))