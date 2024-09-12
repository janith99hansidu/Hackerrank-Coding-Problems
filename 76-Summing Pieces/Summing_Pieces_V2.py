def summingPieces(A):
    MOD = 1000000007

    # Initialize power of 2 list
    twoPower = [1]
    for i in range(1, len(A) + 1):
        twoPower.append((2 * twoPower[-1]) % MOD)

    # Initialize storage with the first element
    storage = [[A[0], A[0], A[0]]]
    L = A[0]

    for i in range(1, len(A)):
        P = (storage[i - 1][1] + twoPower[i] * A[i]) % MOD
        Q = (storage[i - 1][2] + storage[i - 1][1] + (twoPower[i + 1] - 1) * A[i]) % MOD
        N = (L + Q) % MOD
        L = (L + N) % MOD
        storage.append([N, P, Q])

    return storage[-1][0]


# Example usage
arr = [
        477, 392, 161, 421, 245, 50, 530, 889, 750, 16, 545, 303, 898, 785, 162,
        279, 677, 664, 126, 149, 814, 360, 334, 681, 473, 293, 267, 120, 825, 21,
        267, 301, 413, 779, 73, 657, 181, 602, 897, 930, 969, 441, 232, 218, 577,
        745, 848, 253
    ]
result = summingPieces(arr)

print(result)
