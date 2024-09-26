def checkRecord(n):
    """
    :type n: int
    :rtype: int
    """
    memo = {}

    # helper function to recursively check all possibilities
    def helper(current_n, consecutive_late, total_absents):
        # End case for exceeding the allowed consecutive late days or absences
        if consecutive_late == 3 or total_absents == 2:
            return 0

        # Base case: all days are processed
        if current_n == n:
            return 1

        # if the n, consecutive_late, total_absents is the state
        if (n, consecutive_late, total_absents) in memo:
            return memo[(n, consecutive_late, total_absents)]

        # Recursive calls for all possible records
        total = (helper(current_n + 1, 0, total_absents)  # 'P': Present
                 + helper(current_n + 1, consecutive_late + 1, total_absents)  # 'L': Late
                 + helper(current_n + 1, 0, total_absents + 1))  # 'A': Absent

        # calculate the value and store in the memory
        memo[(n, consecutive_late, total_absents)] = total

        return total

    return helper(0, 0, 0)


if __name__ == '__main__':
    n = 2
    print(checkRecord(n))
