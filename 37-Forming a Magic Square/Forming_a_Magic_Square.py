def formingMagicSquare(s):
    all_possible = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    ]

    min_cost = float('inf')
    for magicSquare in all_possible:
        current_cost = 0
        # travers through all possible magic square and get the difference
        for i in range(3):
            for j in range(3):
                current_cost += abs(magicSquare[i][j] - s[i][j])

        if current_cost < min_cost:
            min_cost = current_cost

    return min_cost


if __name__ == '__main__':
    formingMagicSquare([[4, 8, 2], [4, 5, 7], [6, 1, 6]])
