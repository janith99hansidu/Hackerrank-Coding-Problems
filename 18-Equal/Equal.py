def equal(arr):
    # Write your code here
    min_chocolates = min(arr)
    operations_count = float('inf')

    for base in range(5):
        target = min_chocolates - base
        current_operations = 0

        for chocolates in arr:
            delta = chocolates - target
            current_operations += delta // 5 + delta % 5 // 2 + delta % 5 % 2

        operations_count = min(operations_count, current_operations)

    return operations_count

if __name__ == '__main__':
    # [2, 2, 3, 7]
    equal([2, 2, 3, 7])