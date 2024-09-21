from collections import defaultdict
import heapq


def dijkstra(src, budget, flights, destinations):
    graph = defaultdict(list)
    cities = set()

    # make the graph of given flights
    for u, v, cost in flights:
        graph[u].append((v, cost))
        cities.add(u)
        cities.add(v)

    # make cost list
    cost = {city: float('inf') for city in cities}
    cost[src] = 0

    # make priority queue and add the start element
    pq = [(0, src)]

    while pq:

        # get the first element of the pq
        current_cost, destination = heapq.heappop(pq)

        # if the destination distance is lower than current
        if cost[destination] < current_cost:
            continue

        # otherwise put their neighbours to the queue
        for neighbor, flight_cost in graph[destination]:
            new_cost = current_cost + flight_cost

            # if cheaper path found put it to the graph
            if new_cost < cost[neighbor]:
                cost[neighbor] = new_cost

                # add to the heapq
                heapq.heappush(pq, (new_cost, neighbor))

    # print if the destination cost is larger than given budget
    for destination in destinations:
        if destination in cost and cost[destination] <= budget:
            print(cost[destination])
        else:
            print("NONE")


if __name__ == '__main__':
    # get the input of first line
    n, src, budget = input().split()
    n = int(n)
    budget = int(budget)

    # make a list of flights
    flights = []

    for _ in range(n):
        # Each line has: starting city, destination city, cost
        u, v, cost = input().split()
        cost = int(cost)

        flights.append((u, v, cost))

    destinations = []

    # Number of queries
    q = int(input())

    for _ in range(q):
        destination = input().strip()
        destinations.append(destination)

    dijkstra(src, budget, flights, destinations)
