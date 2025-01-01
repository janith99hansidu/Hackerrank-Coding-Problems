"""There are N students and M projects. Each student can work on a specific subset of projects. 
Write a program that finds the maximum number of students that can be assigned to projects 
such that no project is assigned to more than one student. 
Implement the solution using the Edmonds-Karp algorithm for finding maximum flow in a flow network.
"""
def maximum_projects(graph, start, end):
    # make residual graph
    
    return

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
    graph = {}
    for i in range(n+m+2):
        graph[i] = {}
    
    # initialize the graph
    for student, p in enumerate(projects):
        for project in p:
            # update the graph with size of 1
            project_idx = n + project + 1
            graph[student + 1][project_idx] = 1
    
    # connect start node to the all the student with size of 1
    # connect projects to the end node with the size of 1
    for i in range(n):
        graph[0][i+1] = 1
    
    for i in range(n+1, n+m+1):
        graph[i][n+m+1] = 1
        
    
            
    
    
