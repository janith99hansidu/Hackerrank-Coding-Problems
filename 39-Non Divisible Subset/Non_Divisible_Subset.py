def nonDivisibleSubset(k, s):
    remainder_sum = [0] * k

    # fill the remainder_sum table
    for i in s:
        remainder_sum[i % k] += 1

    # maximum subset initialization
    max_subset = 0

    # if there is 0 in the remainder_sum add one
    if remainder_sum[0] > 0:
        max_subset += 1

    # go through the remainders and add the maximum number
    for number in range(1, (k//2)+1):
        if number != k-number:
            max_subset += max(remainder_sum[number], remainder_sum[k-number])
        else:
            max_subset += 1 if remainder_sum[number] > 0 else 0

    return max_subset


if __name__ == '__main__':
    print(nonDivisibleSubset(3, [1, 7, 2, 4]))