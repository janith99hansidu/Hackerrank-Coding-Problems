def uniquePathsWithObstacles(obstacleGrid) -> int:
    
    # recursion + memorization approach
    # recursive function to travel to the each cell from the given obstacle grid
    n_r = len(obstacleGrid)
    n_c = len(obstacleGrid[0])
    memo = {}
    directions = [(0, 1), (1, 0)]
    
    def step(r,c):
        # this function recursively go to each cell and return 1 path is feasible  

        # end condition    
        if r == n_r-1 and c == n_c-1:
            return 1
        
        # if the path is available in memory return it
        if (r, c) in memo.keys():
            return memo[(r, c)]
        
        num_paths = 0
        # calculate the next position of the grid
        for step_r, step_c in directions:
            next_r, next_c = r + step_r , c + step_c
            # check the 
            if next_c > -1 and next_c < n_c and next_r > -1 and next_r < n_r and obstacleGrid[next_r][next_c] != 1:
                num_paths += step(next_r,next_c)

        # add to the memory 
        memo[(r,c)] = num_paths
        # return the value
        return num_paths 
    
    # call the recursive function
    return step(0, 0)

if __name__ == "__main__":
    # input the given obstacle list 
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    # find the unique paths
    print(uniquePathsWithObstacles(obstacleGrid))