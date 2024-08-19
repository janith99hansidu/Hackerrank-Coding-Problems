def biggerIsGreater(w):
    # Write your code here
    l = list(w)

    # i is the pivot
    i = len(w) - 2
    while i >= 0 and l[i] > l[i + 1]:
        i -= 1

    # if i = -1 there is no answer
    if i == -1:
        return "no answer"

    # swap the last element
    j = len(w) - 1
    while l[j] <= l[i]:
        j -= 1

    l[i], l[j] = l[j], l[i]

    # reverse in between elements
    l = l[:i + 1] + l[i + 1:][::-1]  # [::-1] this will reverse the letters

    return ''.join(l)


if __name__ == '__main__':
    biggerIsGreater("hefg")
