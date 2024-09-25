def findLongestChain(pairs):
    # sort the array based on second value of the pair so then always pick the smaller interval
    # that possibly makes the longest count
    pairs.sort(key=lambda x: x[1])

    current_end = float('inf')
    count = 0

    for pair in pairs:
        if current_end < pair[0]:
            current_end = pair[1]
            count += 1

    return count


if __name__ == '__main__':
    pairs = [[1, 2], [7, 8], [4, 5]]

    findLongestChain(pairs)
