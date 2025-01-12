from collections import deque

def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    # get the rows and columns
    n_r = len(grid)
    n_c = len(grid[0])
    visited = [[False] * n_c for _ in range(n_r)]
    total_islands = 0
    
    # perform dfs and mark the visited nodes as true
    def dfs(grid, visited, r, c):
        # add the first node to the stack
        stack = deque([(r, c)])
        
        while stack:
            cur_r, cur_c = stack.pop()
            visited[cur_r][cur_c] = True
            
            # find the possible paths
            if cur_c + 1 < n_c and grid[cur_r][cur_c+1] == '1' and not visited[cur_r][cur_c+1]:
                # add to the stack for traversal
                stack.append((cur_r, cur_c+1))
                
            if cur_c - 1 > -1 and grid[cur_r][cur_c-1] == '1' and not visited[cur_r][cur_c-1]:
                # add to the stack for traversal
                stack.append((cur_r, cur_c-1))
                
            if cur_r + 1 < n_r and grid[cur_r+1][cur_c] == '1' and not visited[cur_r+1][cur_c]:
                # add to the stack for traversal
                stack.append((cur_r+1, cur_c))
                
            if cur_r - 1 > -1 and grid[cur_r-1][cur_c] == '1' and not visited[cur_r-1][cur_c]:
                # add to the stack for traversal
                stack.append((cur_r-1, cur_c))
    
    # traverse each island and if the found a city not visited before 
    # perform dfs on that
    for row in range(n_r):
        for column in range(n_c):
            # if not visited 
            if grid[row][column] == '1' and not visited[row][column]:
                # perform dfs
                dfs(grid, visited, row, column)
                total_islands += 1

    return total_islands


if __name__ == "__main__":
    
    # input to the code 
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    
    # call the function
    print(numIslands(grid)) 