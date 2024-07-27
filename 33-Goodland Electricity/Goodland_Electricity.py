def pylons(k, arr):
    # initialize the variables to the code
    plants = 0
    n = len(arr)
    i = 0  # Start from the first city

    while i < n:
        plant_position = -1
        # Iterate from the rightmost possible position to the leftmost possible position
        for j in range(min(n - 1, i + k - 1), max(-1, i - (k - 1)) - 1, -1):
            if arr[j] == 1:
                plant_position = j
                break

        # if plant position is equal to still -1
        # there is no place to put the plant
        if plant_position == -1:
            return -1

        # increase the number of plants
        plants += 1

        # Move to the next segment to cover
        i = plant_position + k

    return plants

if __name__ == '__main__':
    print(pylons(2, [0, 1, 1, 1, 1, 0]))
