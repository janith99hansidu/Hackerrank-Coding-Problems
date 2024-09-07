def square_root(x, epsilon=1e-6):

    # initialize the low and high to the 0 and x
    low, high = 0, x

    # while high - low > epsilon calculate mid and check for the **2 value
    while high - low > epsilon:
        mid = (high + low)/2

        if mid*mid > x:
            high = mid
        else:
            low = mid

    return (high + low) / 2


if __name__ == '__main__':
    print(square_root(5))
    print(square_root(16))
