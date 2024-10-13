def connectedCell(matrix):
    def dfs(matrix, visited, r, c, directions):
        stack = [(r, c)]
        visited[r][c] = True
        size = 0
        
        while stack:
            row, column = stack.pop()
            size += 1
            
            # Check all 8 directions
            for up, right in directions:
                new_r, new_c = row + up, column + right
                
                if 0 <= new_r < len(matrix) and 0 <= new_c < len(matrix[0]) and not visited[new_r][new_c] and matrix[new_r][new_c] == 1:
                    stack.append((new_r, new_c))
                    visited[new_r][new_c] = True
            
        return size
        
    # directions of all possible connects
    directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
   
    # get the diamentions of the connected edges
    n = len(matrix)
    m = len(matrix[0])
   
    visited = [[False] * m for _ in range(n)]
    max_connected_cells = 0
   
    for r in range(n):
        for c in range(m):
            # if the matrix is 1 and not visited node go and do depth first search
            if matrix[r][c] == 1 and not visited[r][c]:       
                connected_cells = dfs(matrix, visited, r, c, directions)
                max_connected_cells = max(max_connected_cells, connected_cells)
        
    
    return max_connected_cells

if __name__ == '__main__':
    
    n = int(input().strip())

    m = int(input().strip())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)
    
    print(result)