def count_contained_intervals(intervals):
    # sort the given tuples with the min in the first index and maximum in the second index
    intervals.sort(key=lambda x: (x['x'], -x['y']))

    # initialize the variable to the starting values
    count = 0
    max_end = float('-inf')

    # traverse through the sorted list
    for interval in intervals:
        start, end = interval['x'], interval['y']
        if end <= max_end:
            count += 1
        else:
            max_end = end

    return count


if __name__ == '__main__':
    count_contained_intervals([{'x': 1, 'y': 6}, {'x': 1, 'y': 3}, {'x': 4, 'y': 10}, {'x': 4, 'y': 6}, {'x': 5, 'y': 6}])