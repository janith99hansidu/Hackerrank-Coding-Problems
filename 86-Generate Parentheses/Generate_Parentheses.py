def generate_parentheses(n):
    all_possibles = []

    def backtrack(current, open_parentheses, close_parentheses):
        # end condition to the possible ways
        if len(current) == 2 * n:
            all_possibles.append(current)
            return

        # generate with all possible ways
        if open_parentheses < n:
            backtrack(current + '(', open_parentheses + 1, close_parentheses)
        if open_parentheses > close_parentheses:
            backtrack(current + ')', open_parentheses, close_parentheses + 1)

    backtrack('', 0, 0)

    return all_possibles


if __name__ == '__main__':
    print(generate_parentheses(3))
