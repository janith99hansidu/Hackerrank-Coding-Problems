def maximumMissionPoints(n, d_lat, d_long, cities):
    
    # 1. sort the cities with the first element of the latitiude
    cities.sort(key = lambda city: city[2])
    
    # 2. make a memory to store values
    memo = [-1] * n
    
    # 3. recursive function search from start city 
    def searchMax(city):
        
        # 4. if the value is in the memory get it from that memory 
        if memo[city] != -1:
            return memo[city]
        
        # 5. current max is equal to the current value of points
        current_max = cities[city][3]
        
        # city is the start index of the city
        for i in range(city + 1, n):
            if abs(cities[i][0] - cities[city][0]) <= d_lat and abs(cities[i][1] - cities[city][1]) <= d_long and cities[i][2] > cities[city][2]:
                current_max = max(current_max, cities[city][3] + searchMax(i))            

        # 6. return the max possible points
        # save the memory to value
        memo[city] = current_max
        
        return current_max
        
        
        
    overall_max_points = 0
    for city in range(len(cities)):
        # city is the index of the start city index in the cities array
        overall_max_points = max(overall_max_points, searchMax(city))
    
    print(overall_max_points) 

if __name__ == '__main__':
    # hadle the inputs
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d_lat = int(first_multiple_input[1])

    d_long = int(first_multiple_input[2])

    # total number of cities to traverse
    cities = []
    
    for n_itr in range(n):
        second_multiple_input = input().rstrip().split()

        latitude = int(second_multiple_input[0])

        longitude = int(second_multiple_input[1])

        height = int(second_multiple_input[2])

        points = int(second_multiple_input[3])

        cities.append((latitude, longitude, height, points))

    maximumMissionPoints(n, d_lat, d_long, cities)

