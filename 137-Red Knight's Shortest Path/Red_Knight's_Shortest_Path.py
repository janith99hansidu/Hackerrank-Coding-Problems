from collections import deque
def printShortestPath(n, i_start, j_start, i_end, j_end):
    # make a sample grid with possible (step, direction) 
    # step : number of steps to given position
    # direction : direction that came to that given cell
    
    # there is a priority order for traversal
    # direction: (direction, row step, col step)
    directions = [("UL", -2, -1), ("UR", -2, 1), ("R", 0, 2), ("LR", 2, -1), ("LL", 2, 1), ("L", 0, -2)]
    
    # make the grid filled with none
    grid = [[(float('inf'),'')]*n for _ in range(n)]
    
    # fill the grid with possible 
    queue = deque([])
    # step, i_start, j_start 
    queue.append((0 ,i_start, j_start))
    # initialize the starting cell with 0
    grid[i_start][j_start] = (0, '')
    
    while queue:
        # pop the left value and check
        step, i, j = queue.popleft()
        
        # calculate the remaining positions and check whether they can fill
        for direct in directions:
            way, x, y = direct
            current_i = i + x
            current_j = j + y
            
            if current_i < n and current_i >= 0 and current_j < n and current_j >= 0 and grid[current_i][current_j][0] > step + 1:
                grid[current_i][current_j] = (step+1, way)
                queue.append((step+1, current_i, current_j))
    
    # check if destination is reachable
    if grid[i_end][j_end][0] == float('inf'):
        print("Impossible")
        return
    
    # otherwise back track the path
    path = []
    i, j = i_end, j_end

    while (i, j) != (i_start, j_start):
        step, direction = grid[i][j]
        path.append(direction)
        
        # find previous position based on direction
        for way, x, y in directions:
            if way == direction:
                i -= x
                j -= y
                break
    
    # print the path
    print(len(path))
    print(" ".join(reversed(path)))
    

if __name__ == '__main__':
    n = int(input().strip())

    first_multiple_input = input().rstrip().split()

    i_start = int(first_multiple_input[0])

    j_start = int(first_multiple_input[1])

    i_end = int(first_multiple_input[2])

    j_end = int(first_multiple_input[3])

    printShortestPath(n, i_start, j_start, i_end, j_end)