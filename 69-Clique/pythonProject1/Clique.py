def computeMaxE(r, n):
    # Compute the maximum number of edges in a graph with no (r+1)-clique
    g1 = n % r
    g2 = r - g1
    sz1 = n // r + 1  # Size of larger partitions
    sz2 = n // r  # Size of smaller partitions

    # Calculate the number of edges
    ret = g1 * (g1 - 1) * sz1 * sz1 // 2 + g2 * (g2 - 1) * sz2 * sz2 // 2
    ret += g1 * sz1 * g2 * sz2
    return ret


def clique(N, E):
    low, high = 1, N + 1
    while high > low + 1:
        mid = (low + high) // 2  # Compute midpoint
        if computeMaxE(mid, N) < E:
            low = mid
        else:
            high = mid
    return high


if __name__ == '__main__':
    clique(3, 2)
    clique(4, 6)
