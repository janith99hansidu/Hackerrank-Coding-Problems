def climbingLeaderboard(ranked, player):
    # make sorted set list
    sorted_set = sorted(set(ranked), reverse=True)

    # get the current position as last
    current_position = len(sorted_set) - 1

    # place list
    place = []

    for marks in player:
        while current_position >= 0 and marks >= sorted_set[current_position]:
            # if the marks are equal or greater 
            current_position -= 1

        place.append(current_position+2)

    return place



if __name__ == '__main__':
    print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))