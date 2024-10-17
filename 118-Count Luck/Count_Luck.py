from collections import deque

def countLuck(matrix, k):
    # step 1: find the start and the end position of the matrix
    rows = len(matrix)
    columns = len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    start = end = None
    for r in range(rows):
        for c in range(columns):
            # if the position is M, it is the starting position
            if matrix[r][c] == 'M':
                start = (r, c)
            # if the position is *, it is the end/portkey
            elif matrix[r][c] == '*':
                end = (r, c)
    
    # step 2: make queue and do bfs
    guesses = 0  # number of guesses made 
    queue = deque([(start[0], start[1], guesses)]) 
    visited = [[False] * columns for _ in range(rows)]
    visited[start[0]][start[1]] = True  # Mark start as visited
    
    while queue:
        # pop the current left node from the queue
        current_r, current_c, current_guesses = queue.popleft()
        
        # end case: if we reach the portkey, check if the guesses match Ron's guess
        if (current_r, current_c) == end:
            return "Impressed" if current_guesses == k else "Oops!" 
        
        # find the possible paths 
        possible_paths = []
        
        # explore all possible directions
        for direct in directions:
            nr, nc = current_r + direct[0], current_c + direct[1]
            if 0 <= nr < rows and 0 <= nc < columns and not visited[nr][nc] and matrix[nr][nc] != "X":
                possible_paths.append((nr, nc))
        
        # if there are more than 1 possible path, Hermione has to make a decision (wave her wand)
        if len(possible_paths) > 1:
            current_guesses += 1
    
        # visit the nodes and add them to the queue
        for path in possible_paths:
            visited[path[0]][path[1]] = True  # Mark the path as visited
            queue.append((path[0], path[1], current_guesses))

if __name__ == "__main__":
    # Input parsing and handling multiple test cases
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        matrix = [input().strip() for _ in range(n)]
        k = int(input())
        print(countLuck(matrix, k))
