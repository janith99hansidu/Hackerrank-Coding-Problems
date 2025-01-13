import heapq

def minimumEffortPath(heights):
    # use dijkstra algorithm to find the minimum effort path explore the minimum first
    
    # initialize the variables
    rows, columns = len(heights), len(heights[0])
    # (effort, r, c)
    heap = [(0, 0, 0)]
    # in this dijkstra algorithm instead of mark as visited it only put the nodes that are current effort is less than
    # previous effort so it only look after new nodes not traverse back and forward
    effort = [[float('inf')] * columns for _ in range(rows)]
    effort[0][0] = 0
    
    # traversal directions in the graph
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while heap:
        # get the minimum effort node
        current_effort, current_r, current_c = heapq.heappop(heap)
        
        # check whether the current node destination 
        if current_r == rows - 1 and current_c == columns - 1:
            return current_effort
        
        # find the next step from the current node
        for dr, dc in directions:
            new_row, new_col = current_r + dr, current_c + dc

            if 0 <= new_row < rows and 0 <= new_col < columns:
                next_effort = max(current_effort, abs(heights[new_row][new_col] - heights[current_r][current_c]))
                
                if next_effort < effort[new_row][new_col]:
                    effort[new_row][new_col] = next_effort
                    heapq.heappush(heap, (next_effort, new_row, new_col))
                    
    return effort[rows - 1][columns - 1]
        