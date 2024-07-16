def substrings(n):
    """
    :param n: Array of numbers that are substring
    :return: total number of sum of all possible substring
    """

    MOD = 10 ** 9 + 7
    length = len(n)
    total_sum = 0
    current_value = 0

    for i in range(length):
        current_value = (current_value * 10 + int(n[i]) * (i + 1)) % MOD
        total_sum = (total_sum + current_value) % MOD

    return total_sum


if __name__ == '__main__':
    print(substrings("123"))
