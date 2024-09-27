def find_longest_suffix(s, p):
    # Initialize pointers at the end of both s and p
    i, j = len(s) - 1, len(p) - 1
    suffix_len = 0

    # Traverse `s` from the end to the beginning
    while i >= 0 and j >= 0:
        if s[i] == p[j]:
            # If characters match, move both pointers
            suffix_len += 1
            j -= 1
        # Always move the pointer for `s`
        i -= 1

    # Return the length of the longest suffix of p that is a subsequence of s
    return suffix_len


if __name__ == '__main__':
    # Read the input
    s = input().strip()
    q = int(input().strip())

    # result
    result = []
    # Process each query
    for _ in range(q):
        p = input().strip()
        # Find the longest suffix of p that is a subsequence of s
        result.append(find_longest_suffix(s, p))

    for elem in result:
        print(elem)
