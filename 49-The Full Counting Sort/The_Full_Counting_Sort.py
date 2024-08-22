def countSort(arr):
    # Determine the maximum value in arr to size the count array
    max_val = max(int(x[0]) for x in arr)

    # Initialize count array with empty lists
    count = [[] for _ in range(max_val + 1)]

    # First half of the array is to be replaced with '-'
    half_length = len(arr) // 2

    # Populate the count array
    for i, (num, string) in enumerate(arr):
        if i < half_length:
            count[int(num)].append('-')
        else:
            count[int(num)].append(string)

    # Flatten the count array into the final sorted list
    final_arr = []
    for sublist in count:
        final_arr.extend(sublist)

    # Print the result as a space-separated string
    print(' '.join(final_arr))


if __name__ == '__main__':
    countSort([['0', 'ab'], ['6', 'cd'], ['0', 'ef'], ['6', 'gh'], ['4', 'ij'], ['0', 'ab'], ['6', 'cd'], ['0', 'ef'],
               ['6', 'gh'], ['0', 'ij'], ['4', 'that'], ['3', 'be'], ['0', 'to'], ['1', 'be'], ['5', 'question'],
               ['1', 'or'], ['2', 'not'], ['4', 'is'], ['2', 'to'], ['4', 'the']])
