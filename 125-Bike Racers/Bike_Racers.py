import os
import math

def canMatchInTime(bikers, bikes, k, timeLimit):
    len_bikes = len(bikes)
    len_bikers = len(bikers)
    
    # 1. make a graph with given biker and the possible bikes he can get
    # initialize the array with bicker size
    graph = [[] for _ in range(len_bikers)]
    # fill the graph with the possible bikes for each bicker
    for i in range(len_bikers):
        for j in range(len_bikes):
            # if the bike can be reachable
            dist_squared = (bikers[i][0] - bikes[j][0]) ** 2 + (bikers[i][1] - bikes[j][1]) ** 2
            if dist_squared <= timeLimit:
                graph[i].append(j)
    
    assigned = [-1] * len_bikers
    visited = [False] * len_bikes
    # 2. dfs like function to check and assigned bikes
    def dfs(biker):
        # start: start bike of the dfs search
        for bike in graph[biker]:
            # if the bike is already visited
            if visited[bike]:
                continue
            
            # mark the bike visited
            visited[bike] = True
            
            # check the bike is unassined or can be assinged using recursion if either true 
            if assigned[bike] == -1 or dfs(assigned[bike]):
                # if either true that bike can be assign to the biker
                assigned[bike] = biker
                return True
        
        return False
    
    # 3. check for each bicker to assign to a bike
    match_count = 0
    for biker in range(len_bikers):
        # make the visited bikes back to false for each bike
        visited = [False] * len_bikes
        if dfs(biker):
            match_count += 1
        if match_count >= k:
            return True
    
    return False

# do binary search for relevant time limit mach with the k possible maches 
def bikeRacers(bikers, bikes, k):
    low = 0
    high = 10 ** 14
    
    while low < high:
        mid = (low + high) // 2
        if canMatchInTime(bikers, bikes, k, mid):
            high = mid
        else:
            low = mid + 1

    return low

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    k = int(first_multiple_input[2])

    bikers = []
    for _ in range(n):
        bikers.append(list(map(int, input().rstrip().split())))

    bikes = []
    for _ in range(m):
        bikes.append(list(map(int, input().rstrip().split())))

    result = bikeRacers(bikers, bikes, k)
    
    print(result)
