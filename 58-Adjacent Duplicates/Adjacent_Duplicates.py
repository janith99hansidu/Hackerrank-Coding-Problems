def adjacent_duplicates(start_index, next_index, arr):
    # if the next index reach the end of the string return
    if next_index >= len(arr):
        return arr

    # if the next element and the start element are same remove from the string
    if arr[next_index] == arr[start_index]:
        arr = arr[:start_index] + arr[next_index + 1:]
    
    # if all above conditions call the next function
    arr = adjacent_duplicates(start_index + 1, next_index + 1, arr)

    return arr


if __name__ == '__main__':
    word = "geeksforgeek"
    print(adjacent_duplicates(0, 1, word))
