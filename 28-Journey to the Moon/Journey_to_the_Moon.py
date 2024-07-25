import math


def journeyToMoon(n, astronaut):
    # Write your code here
    astronautGroupNum = 0  # Group number of astronaut
    astronautDict = {}  # AstronautDict for each group
    totalPossible = 0  # Calculate the total possible without considering groups
    totalPossibleConsider = 0

    # Make the dict for each astronaut
    for i in range(n):
        astronautDict[i] = 0

    # Astronauts groups
    astronautGroup = {}

    # Traverse through the given astronauts list
    for asto in astronaut:
        # If both astronaut are not in a group
        if astronautDict[asto[0]] == 0 and astronautDict[asto[1]] == 0:
            astronautGroupNum += 1
            astronautDict[asto[0]] = astronautGroupNum
            astronautDict[asto[1]] = astronautGroupNum

            # Calculate the number of groups in astronaut each group
            astronautGroup[astronautGroupNum] = 2

        elif astronautDict[asto[0]] != 0 and astronautDict[asto[1]] != 0:

            # if both have groups
            astronautGroup[astronautDict[asto[0]]] += 2
        else:
            # if one has a group
            if astronautDict[asto[0]] != 0:
                astronautDict[asto[1]] = astronautDict[asto[0]]

                # add the group number +1
                astronautGroup[astronautDict[asto[0]]] += 1
            else:
                astronautDict[asto[0]] = astronautDict[asto[1]]

                # add the group number +1
                astronautGroup[astronautDict[asto[1]]] += 1

    # Add groups to not in the astronautGroup
    for nums in astronautDict:
        if astronautDict[nums] == 0:
            astronautGroupNum += 1

            # add to the dictionary
            astronautDict[astronautGroupNum] = 1

            # add to the groups
            astronautGroup[astronautGroupNum] = 1

    # Calculate total possible ways
    for i in astronautGroup:
        if astronautGroup[i] > 1:
            totalPossibleConsider += math.ceil(astronautGroup[i]*(astronautGroup[i]-1)/2)

    totalPossible = n * (n-1)/2

    return totalPossibleConsider - totalPossible


if __name__ == '__main__':
    journeyToMoon(6, [[0, 1], [2, 3], [0, 4]])
