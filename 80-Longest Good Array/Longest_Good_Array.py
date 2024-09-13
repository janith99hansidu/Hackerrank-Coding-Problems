import math

def longestGoodArray(l, r):
    # Solve for the maximum k using the quadratic equation approach
    max_diff = r - l  # The maximum allowable difference between r and l
    k = int((-1 + math.sqrt(1 + 8 * max_diff)) // 2)  # Using the quadratic formula

    # Calculate the total value of the sum at the maximum k
    last_term = l + (k * (k + 1)) // 2

    # Check if the last term exceeds r
    if last_term > r:
        k -= 1  # Adjust k if we overshot

    return k + 1  # Return k + 1 as the number of terms


if __name__ == '__main__':
    # Read the number of test cases
    t = int(input().strip())

    # Store results for each test case
    results = []

    # Loop over the number of test cases
    for _ in range(t):
        l, r = map(int, input().strip().split())  # Read l and r
        results.append(str(longestGoodArray(l, r)))

    # Output the results, one per line
    print("\n".join(results))
