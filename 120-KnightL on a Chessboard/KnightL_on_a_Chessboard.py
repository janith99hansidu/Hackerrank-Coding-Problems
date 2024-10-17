from collections import deque

# Generate all 8 possible knight moves
def generate_knight_moves(base_move):
    dx, dy = base_move
    moves = [
        (dx, dy), (dx, -dy), (-dx, dy), (-dx, -dy),
        (dy, dx), (dy, -dx), (-dy, dx), (-dy, -dx)
    ]
    return moves

def knightlOnAChessboard(n):
    # To store the result for each knight's movement (r+1, c+1)
    result = [[-1] * (n - 1) for _ in range(n - 1)]
    
    # Iterate over all possible knight moves (r+1, c+1)
    for r in range(n - 1):
        for c in range(n - 1):
            directions = generate_knight_moves((r + 1, c + 1))
            
            # Initialize the grid with 'infinity', start at (n-1, n-1) with 0 moves
            grid = [[float('inf')] * n for _ in range(n)]
            grid[n - 1][n - 1] = 0
            
            # BFS to explore the board
            queue = deque([(n - 1, n - 1)])
            
            while queue:
                current_r, current_c = queue.popleft()
                grid_value = grid[current_r][current_c]
                
                for dr, dc in directions:
                    nr, nc = current_r + dr, current_c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > grid_value + 1:
                        grid[nr][nc] = grid_value + 1
                        queue.append((nr, nc))
            
            # If the top-left corner is reachable, store the result
            if grid[0][0] != float('inf'):
                result[r][c] = grid[0][0]
    
    return result

if __name__ == '__main__':
    n = int(input().strip())
    knightlOnAChessboard(n)
