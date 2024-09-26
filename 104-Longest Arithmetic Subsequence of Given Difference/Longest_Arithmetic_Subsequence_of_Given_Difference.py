def longestSubsequence(arr, difference):
    # make a dictionary of elements with the
    # key: number
    # value: position arr
    num_dict = {}
    for i, num in enumerate(arr):
        if num in num_dict:
            # Append the index to the list if the key exists
            num_dict[num].append(i)
        else:
            # Initialize the list with the current index if the key doesn't exist
            num_dict[num] = [i]

    # make helper function to traverse each element
    # num: the current number of the array
    # position: the current position of the number
    def helper(num, position):

        # Initialize the length of subsequence starting from this element as 1
        longest = 1

        # if it is in the num_dict and the position is greater than the current element
        if num + difference in num_dict:
            # next positions of the number occurrences
            next_positions = num_dict[num + difference]

            # the next position of the number that can search for the next valid difference
            next_position = -1
            for i in next_positions:
                if i > position:
                    next_position = i
                    break  # You need to break to get the first valid next position

            # recursive call for the next element
            if next_position != -1:
                longest = 1 + helper(num + difference, next_position)

        return longest

    max_length = 0

    # Iterate over all elements and find the longest subsequence starting from each element
    for i in range(len(arr)):
        max_length = max(max_length, helper(arr[i], i))

    return max_length


if __name__ == '__main__':
    arr = [1, 5, 7, 8, 5, 3, 4, 2, 1]
    difference = -2

    print(longestSubsequence(arr, difference))
