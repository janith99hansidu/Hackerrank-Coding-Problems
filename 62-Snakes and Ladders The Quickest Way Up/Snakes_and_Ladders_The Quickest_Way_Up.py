from collections import deque


def quickestWayUp(ladders, snakes):
    # Write your code here
    # Initialize the board
    board = list(range(101))

    for start, end in ladders:
        board[start] = end
    for start, end in snakes:
        board[start] = end

    queue = deque([(1, 0)])
    visited = [False] * 101
    visited[1] = True

    while queue:
        position, roll = queue.popleft()

        # Try all possible dice rolls
        for i in range(1, 7):
            next_position = position + i

            if next_position <= 100:
                final_position = board[next_position]

                if final_position == 100:
                    return roll + 1

                if not visited[final_position]:
                    visited[final_position] = True
                    queue.append((final_position, roll + 1))

    return -1


if __name__ == '__main__':
    ladders1 = [[32, 62], [42, 68], [12, 98]]
    snakes1 = [[95, 13], [97, 25], [93, 37], [79, 27], [75, 19], [49, 47], [67, 17]]
    ladders2 = [[8, 52], [6, 80], [26, 42], [2, 72]]
    snakes2 = [[51, 19], [39, 11], [37, 29], [81, 3], [59, 5], [79, 23], [53, 7], [43, 33], [77, 21]]

    print(quickestWayUp(ladders1, snakes1))
    print(quickestWayUp(ladders2, snakes2))
