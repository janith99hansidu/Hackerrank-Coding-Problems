from collections import deque

def Balancing_parentheses(s):
    # 1. if the string is empty return true
    # 2. if ( found put to the stack with False
    # 2. if :( found put to the stack with true [(, True]
    # 3. if the :) found get the pop the stack and mark as [(,True]
    # 4. if ) found pop the list if no element to pop return false
    # 4. get all remaining in stack and check the all are True if one is false return false
    
    def recursive(i, stack):
        # end of string
        if i == len(s):
            return len(stack) == 0

        ch = s[i]
        ok_with = ok_without = False

        if ch == '(':
            # treat as a real '('
            new_stack = stack.copy()
            new_stack.append('(')
            ok_with = recursive(i+1, new_stack)

            # or treat as part of ":(" emoticon
            if i > 0 and s[i-1] == ':':
                ok_without = recursive(i+1, stack.copy())

        elif ch == ')':
            # emoticon ":)"
            if i > 0 and s[i-1] == ':':
                ok_without = recursive(i+1, stack.copy())

            # or real ')'
            if stack:
                new_stack = stack.copy()
                new_stack.pop()
                ok_with = recursive(i+1, new_stack)

        else:
            # any other char, just skip
            ok_with = recursive(i+1, stack.copy())

        return ok_with or ok_without

    return recursive(0, deque())

    
if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        s = input()
        if Balancing_parentheses(s):
            print("YES")
        else:
            print("NO")
