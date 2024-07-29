def toys(w):
    # Write your code here
    sorted_arr = sorted(w)
    length_arr = len(w)

    starting_index = 0
    num_groups = 1

    for test_index in range(length_arr):
        if sorted_arr[test_index] > sorted_arr[starting_index] + 4:
            starting_index = test_index
            num_groups += 1

    return num_groups


if __name__ == '__main__':
    toys([1, 2, 3, 21, 7, 12, 14, 21])
