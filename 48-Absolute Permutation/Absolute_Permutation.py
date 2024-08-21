def absolutePermutation(n, k):
    # if k = 0 return the same list
    if k == 0:
        return list(range(1, n + 1))

    # we can not form a permutation if the n % k*2 != 0
    # we can not form 2 groups more than k and less k

    if n % (k * 2) != 0:
        return [-1]

    # make the array to return
    add = True
    result = []

    for i in range(1, n + 1):
        if add:
            result.append(i + k)
        else:
            result.append(i - k)

        if i % k == 0:
            add = not add

    return result


if __name__ == '__main__':
    print(absolutePermutation(2, 1))
