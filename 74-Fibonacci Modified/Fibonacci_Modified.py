import sys

sys.set_int_max_str_digits(1000000)


def fibonacciModified(t1, t2, n):
    n_2 = t1
    n_1 = t2

    if n == 1:
        return n_2

    if n == 2:
        return n_1

    for i in range(3, n + 1):
        # calculate the next element
        next_num = n_2 + n_1 ** 2
        n_2 = n_1  # save n-1 value to n-2 value
        n_1 = next_num  # save n-1 value to next value

    return next_num


if __name__ == '__main__':
    fibonacciModified(0, 1, 5)
