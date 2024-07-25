from collections import deque, defaultdict


def journeyToMoon(n, astronaut):
    # create adjacency list of astronauts
    graph = defaultdict(list)


    # get the visited nodes in n astronauts
    visited = [False] * n

    # insert to the adjacency list
    for a, b in astronaut:
        graph[a].append(b)
        graph[b].append(a)

    # Function to perform BFS and find all astronauts
    def bfs(start):
        queue = deque([start])
        count = 0
        visited[start] = True

        while queue:
            node = queue.popleft()
            count += 1

            for neighbour in graph[node]:
                if not visited[neighbour]:
                    queue.append(neighbour)
                    visited[neighbour] = True

        return count

    # list of number of connected components
    counted_sizes = []

    # perform bfs to find connected counts
    for astronauts in range(n):
        if not visited[astronauts]:
            size = bfs(astronauts)
            counted_sizes.append(size)
    # Calculate the number of valid pairs
    total_pairs = 0
    sum_of_sizes = 0
    for size in counted_sizes:
        total_pairs += size * (n - sum_of_sizes - size)
        sum_of_sizes += size

    return total_pairs


if __name__ == '__main__':
    print(journeyToMoon(6, [[0, 1], [2, 3], [0, 4]]))

    # calculate the count of possible pair
    size = 0
    possible_pairs = 0
    pair = {1: 3, 2: 2, 3: 4, 4:1}
    total_number_elem = 10
    for i in pair:
        possible_pairs += pair[i]*(total_number_elem - size - pair[i])
        size += pair[i]
