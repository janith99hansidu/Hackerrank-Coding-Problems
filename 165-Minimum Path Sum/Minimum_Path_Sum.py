def minPathSum(grid):
    # a dynamic programming problem can be solved using
    # recursive + memorization
    # make a dict for the save to the memorization 
    memo = {}
    m = len(grid)
    n = len(grid[0])
    directions = [(1,0), (0,1)]
    
    def recursive(pos):
        min_total = float('inf')
        # pos is a tuple for current pos of the grid
        # pos = (x, y)
        # if the minimum path is already exist
        if pos in memo.keys():
            return memo[pos]
        
        # end condition if the pos return to the end condition it return the 0
        if pos == (m-1, n-1):
            return grid[m-1][n-1]
    
        # go to the right and down recursively and record the minimum
        r, c = pos
        for dir in directions:
            n_r, n_c = dir
            next_r, next_c = n_r + r , n_c + c
            if  0 <= next_r < m and 0 <= next_c < n:
                # calculate the current position value
                current_val = grid[r][c] + recursive((next_r, next_c))
                min_total = min(current_val, min_total)

        return min_total   
    
    return recursive((0,0))
        
if __name__ == "__main__":
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(minPathSum(grid))

    grid = [[1,2,3],[4,5,6]]
    print(minPathSum(grid))