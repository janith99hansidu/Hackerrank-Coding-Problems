def previous_permutation(permutation):
    permutation_index = -1

    # Step 1: Find the largest index `i` such that permutation[i] > permutation[i + 1]
    for i in range(len(permutation) - 2, -1, -1):
        if permutation[i] > permutation[i + 1]:
            permutation_index = i
            break

    # If no such index exists, the permutation is the smallest (first permutation)
    if permutation_index == -1:
        return [-1]

    # Step 2: Find the largest index `j` such that permutation[j] < permutation[permutation_index]
    exchange_index = -1
    for j in range(len(permutation) - 1, permutation_index, -1):
        if permutation[j] < permutation[permutation_index]:
            exchange_index = j
            break

    # Step 3: Swap the values at `permutation_index` and `exchange_index`
    permutation[permutation_index], permutation[exchange_index] = permutation[exchange_index], permutation[permutation_index]

    # Step 4: Reverse the sublist after `permutation_index`
    permutation[permutation_index + 1:] = permutation[permutation_index + 1:][::-1]

    return permutation


if __name__ == '__main__':
    prev = previous_permutation(list([4, 1, 3, 2, 5]))
    print(prev)