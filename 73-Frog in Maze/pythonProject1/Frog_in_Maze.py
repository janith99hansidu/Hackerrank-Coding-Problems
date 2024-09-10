from collections import defaultdict, deque

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def frog_maze(n, m, maze, tunnels):
    # make tunnel dictionary to find tunnel connections
    # make hashmap to find
    tunnel_map = {}
    for r1, c1, r2, c2 in tunnels:
        tunnel_map[(r1 - 1, c1 - 1)] = (r2 - 1, c2 - 1)
        tunnel_map[(r2 - 1, c2 - 1)] = (r1 - 1, c1 - 1)

    # start variable is the start node of the graph
    start = None
    graph = defaultdict(list)
    # make a graph with the given input
    for row in range(n):
        for column in range(m):

            if maze[row][column] == "A":
                start = (row, column)

            # if there is # cannot move
            if maze[row][column] != "#":
                # dr Direction row and dc Direction column
                for dr, dc in DIRECTIONS:
                    nr = row + dr
                    nc = column + dc

                    if 0 <= nr < n and 0 <= nc < m and maze[nr][nc] != "#":
                        graph[(row, column)].append((nr, nc))

                # if the row and column in the tunnel map add them
                if (row, column) in tunnel_map:
                    graph[(row, column)].append(tunnel_map[(row, column)])

    # traverse and calculate the probability to reach the end
    queue = deque([(start, 1.0)])
    visited = set()
    total_escape_prob = 0

    while queue:
        # trverse all the nodes and calculate the probability to go to end
        (r, c), prob = queue.popleft()

        # if already visited continue
        if (r, c) in visited:
            continue
        visited.add((r, c))

        # if mine cell continue
        if maze[r][c] == '*':
            continue
        elif maze[r][c] == '%':
            total_escape_prob += prob
            continue

        # calculate the probability of adjacency list
        adj_cells = graph[(r, c)]
        move_prob = prob / len(adj_cells)

        for nr, nc in adj_cells:
            if (nr, nc) not in visited:
                queue.append(((nr, nc), move_prob))

    return total_escape_prob


if __name__ == '__main__':
    n = 3
    m = 6
    maze = [
        "###*OO",
        "O#OA%O",
        "###*OO"
    ]
    tunnels = [
        (2, 3, 2, 1)
    ]

    print(frog_maze(n, m, maze, tunnels))
