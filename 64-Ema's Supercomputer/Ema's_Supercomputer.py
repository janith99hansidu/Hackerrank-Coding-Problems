def twoPluses(grid):
    rows = len(grid)
    columns = len(grid[0])

    # Helper function to calculate the maximum size of a plus at a given cell (i, j)
    def get_max_plus_size(i, j):
        size = 0
        while (i - size >= 0 and i + size < rows and j - size >= 0 and j + size < columns and
               grid[i - size][j] == 'G' and grid[i + size][j] == 'G' and
               grid[i][j - size] == 'G' and grid[i][j + size] == 'G'):
            size += 1
        return size - 1

    # Create a list of all possible pluses with their size and center coordinates
    pluses = []
    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 'G':
                max_size = get_max_plus_size(i, j)
                for size in range(max_size + 1):
                    pluses.append((i, j, size))

    max_product = 0

    # Helper function to check if two pluses overlap
    def pluses_overlap(p1, p2):
        (x1, y1, size1) = p1
        (x2, y2, size2) = p2

        plus1_coords = set()
        plus2_coords = set()

        for d in range(-size1, size1 + 1):
            plus1_coords.add((x1 + d, y1))
            plus1_coords.add((x1, y1 + d))

        for d in range(-size2, size2 + 1):
            plus2_coords.add((x2 + d, y2))
            plus2_coords.add((x2, y2 + d))

        # Check for any common coordinates (overlap)
        return not plus1_coords.isdisjoint(plus2_coords)

    # Compare every pair of pluses and calculate the product of their areas if they don't overlap
    for i in range(len(pluses)):
        for j in range(i + 1, len(pluses)):
            plus1 = pluses[i]
            plus2 = pluses[j]
            if not pluses_overlap(plus1, plus2):
                area1 = 4 * plus1[2] + 1
                area2 = 4 * plus2[2] + 1
                max_product = max(max_product, area1 * area2)

    return max_product

if __name__ == '__main__':
    grid = [
        "GGGGGG",
        "GBBBGB",
        "GGGGGG",
        "GGBBGB",
        "GGGGGG"
    ]
    result = twoPluses(grid)
    print(result)
