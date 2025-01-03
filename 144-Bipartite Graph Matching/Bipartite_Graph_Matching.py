"""There are N students and M projects. Each student can work on a specific subset of projects. 
Write a program that finds the maximum number of students that can be assigned to projects 
such that no project is assigned to more than one student. 
Implement the solution using the Edmonds-Karp algorithm for finding maximum flow in a flow network.
"""
from collections import deque

def bfs(graph, start, end, parents):
    # do not traverse again visited nodes
    visited = set()
    visited.add(start)
    # queue to keep track of the 
    queue = deque([start])  
    
    while queue:
        # get the current node from the queue
        current_node = queue.popleft()
        # find the neighbors
        for idx, edge in enumerate(graph[current_node]):
            if edge and idx not in visited:
                # add to the visited node
                visited.add(idx)
                # add to the queue
                queue.append(idx)
                # correct the parent node
                parents[idx] = current_node
                # if the node is destination 
                if idx == end:
                    return True
    
    # if there is no path in 
    return False

def maximum_projects(graph, start, end):
    # residual graph is same as the normal graph
    max_flow = 0
    # get the parent node to reconstruct the edges in graph
    parents = {}
    
    # print(bfs(graph, start, end, parents)) # debug the bfs
    
    while bfs(graph,start, end, parents):
        # if there is a path maxflow ++
        max_flow += 1
        
        # reverse the edges in graph in residual connections
        u = end
        while u != start:
            v = parents[u]
            # update the graph
            # remove the edge
            graph[v][u] = 0
            # add the edge 
            graph[u][v] = 1
            # going backward by one 
            u = v
             
    return max_flow

if __name__ == "__main__":
    # get the number of students and projects
    n, m = map(int, input().split())
    
    # get the inputs of the each student and preferred projects
    projects = []
    for _ in range(n):
        _, *project = map(int, input().split())
        projects.append(project)
    
    # make the graph 1-n for the students and others for the projects
    # start node 0 and end node is n+m+2 - 1
    # make graph as adjacency matrix because of the memory optimization
    graph = [[0]*(n+m+2) for _ in range(n+m+2)]
    
    # get each project and match the relevant node
    for student, projects in enumerate(projects):
        for project in projects:
            # make connection between student and project
            # project index should be project + n
            project_idx = project + n
            graph[student + 1][project_idx] = 1
            
            # make connection between start node and student
            graph[0][student + 1] = 1
            
            # make the connection each project and end node
            graph[project_idx][n + m + 1] = 1
    
    # graph is constructed with adjacency matrix that is easier to residual graph with the max flow every time is one 
    # no need to track flow amount because every time is one
    
    # call the function with start = 0 end = n+m+1
    max_flow = maximum_projects(graph, 0, n+m+1)
    print(max_flow)
            
    
            
    
    
