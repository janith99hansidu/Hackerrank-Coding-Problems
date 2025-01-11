from collections import deque

def jeanisRoute(N, K, delivery, roads):
    # adjust delivery cities to zero based indexing
    # then it is easy to get the operations with list and array 
    # no offset operations is needed , computationally efficient
    delivery = set(city - 1 for city in delivery)
    
    # build the graph using adjacency list
    paths = [[] for _ in range(N)]
    for frm, to, d in roads:
        paths[frm - 1].append((to - 1, d))
        paths[to - 1].append((frm - 1, d)) 
    
    # select only the relevant paths and get the maximum distance
    # find parent relationships with BFS
    parent = [-1] * N
    root = next(iter(delivery))
    q = deque([root])
    
    while q:
        x = q.popleft()
        for neighbor, dist in paths[x]:
            if  neighbor != parent[x]:
                q.append(neighbor)
                parent[neighbor] = x

    # mark the cities to keep
    # only get the cities that are wanted to traverse to visit relevant cities
    keep = [False] * N
    for city in delivery:
        x = city
        while x != -1 and not keep[x]:
            keep[x] = True
            x = parent[x]
    
    # only get the relevant paths that are want to traverse 
    paths = [[(neighbor, dist) for neighbor, dist in paths[i] if keep[neighbor] and keep[i]] for i in range(N)]
    
    # function to find the furthest vertex
    def furthest_vertex(start):
        result = (start, 0)
        visited = [False] * N
        q = deque([result])
        while q:
            current, length = q.popleft()
            if length > result[1]:
                result = (current, length)
            visited[current] = True
            for neighbor, dist in paths[current]:
                if not visited[neighbor]:
                    q.append((neighbor, length + dist))
        return result
    
    # find the longest path from 2 bfs from any node
    start = next(i for i, neighbors in enumerate(paths) if neighbors)
    longest_path = furthest_vertex(furthest_vertex(start)[0])[1]
    
    # calculate the total distance of all paths
    total_distance = sum(sum(dist for _, dist in neighbors) for neighbors in paths)
    
    # minimum distance is total distance - longest path 
    return total_distance - longest_path

if __name__ == "__main__":
    
    # example path 
    N = 5 # number of cities
    K = 3 # number of k letters that should traverse 
    
    # delivery cities 
    delivery = [1, 3, 4]
    roads = [
        (1, 2, 1),
        (2, 3, 2),
        (2, 4, 2),
        (3, 5, 3)
    ]
    
    # find the minimum distance
    result = jeanisRoute(N, K, delivery, roads)
    