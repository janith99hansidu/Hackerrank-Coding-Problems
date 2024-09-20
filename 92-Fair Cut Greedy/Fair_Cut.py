# greedy approach not DP
def fairCut(k, arr):

    # sort the array
    listarr = list(sorted(arr))
    # current unfairness
    current_sum = 0
    # set of k element in the list
    k_list = []

    for i in range(k):
        mid = len(listarr) // 2

        # remove the element from the listarr
        removed_elem = listarr.pop(mid)

        # add to the k list
        k_list.append(removed_elem)

        # difference between remove element and the others in arr
        for elem in listarr:
            current_sum += abs(elem - removed_elem)

        # if the k_list is not empty add the unwnted parts to the current sum
        if len(k_list) != 0:
            for elem in k_list:
                current_sum -= abs(removed_elem - elem)

    return current_sum


if __name__ == '__main__':
    fairCut(2, [4, 3, 1, 2])