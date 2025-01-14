from collections import defaultdict, deque
# partially correct use the kahn's algorithm for topological sorting 

def findOrder(numCourses, prerequisites):
    # make the graph from the given prerequisites
    graph = defaultdict(list)
    for n_to, n_from in prerequisites:
        graph[n_from].append(n_to)
    
    # do the bfs
    visited = [False] * numCourses
    queue = deque([0])
    visited[0] = True
    order = []
    
    while queue:
        # get a node from a list 
        current_node = queue.popleft()
        order.append(current_node)
        
        for neighbor in graph[current_node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    if len(order) == numCourses:
        return order
    else:
        return []
    
if __name__ == "__main__":
    # enter inputs
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    
    # call the function 
    print(findOrder(numCourses, prerequisites))