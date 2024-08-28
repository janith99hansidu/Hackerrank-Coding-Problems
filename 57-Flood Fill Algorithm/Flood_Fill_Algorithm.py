def dfs(img, x, y, prev_clr, new_clr):

    # edge case for ending the recursion
    # if the image prev_clr != new_clr
    if img[x][y] != prev_clr:
        return

    # if the prev_color is same as now color change the clor
    img[x][y] = new_clr

    m = len(img)
    n = len(img[0])
    
    # traverse to the other cells with the order
    if x - 1 >= 0:
        dfs(img, x - 1, y, prev_clr, new_clr)
    if y + 1 < m:
        dfs(img, x, y + 1, prev_clr, new_clr)
    if y - 1 >= 0:
        dfs(img, x, y - 1, prev_clr, new_clr)
    if x + 1 < n:
        dfs(img, x + 1, y, prev_clr, new_clr)


if __name__ == '__main__':
    # Image array
    img = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]
    ]

    # Starting position of the image
    x = 1
    y = 1

    # New color that has to be filled
    new_clr = 3
    prev_clr = 1
    dfs(img, x, y, prev_clr, new_clr)
    print(img)