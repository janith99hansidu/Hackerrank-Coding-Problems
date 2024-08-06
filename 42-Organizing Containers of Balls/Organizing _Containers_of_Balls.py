def organizingContainers(container):

    # get the total sum of each container
    container_sum = [sum(con) for con in container]

    # get the total sum of each type
    type_sum = [sum(col) for col in zip(*container)]

    if sorted(container_sum) == sorted(type_sum):
        return "Possible"
    else:
        return "Impossible"


if __name__ == '__main__':
    containers_example = [
        [1, 3, 1],
        [2, 1, 2],
        [3, 3, 3]
    ]

    print(organizingContainers(containers_example))
