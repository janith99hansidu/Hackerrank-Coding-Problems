def minOperation(k):
    current_dict = {}

    def stepOne(current, steps):
        # if there is already a value in dict
        # memorization step
        if current in current_dict:
            return current_dict[current]

        # if the current is greater than k
        if current > k:
            return float('inf')
        if current == k:
            return steps

        # what is the minimum of adding one and multipy by 2
        current_dict[current] = min(stepOne(current + 1, steps + 1), stepOne(current * 2, steps + 1))

        # return minimum value to above sub problem
        return current_dict[current]

    # there is only a step to move forward in the problem from 0 - > 1 add one
    return stepOne(1, 1)


if __name__ == '__main__':
    print(minOperation(4))
