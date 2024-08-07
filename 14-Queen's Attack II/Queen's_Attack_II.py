def queensAttack(n, k, r_q, c_q, obstacles):
    # number of positions that queen can move in board
    max_reach ={
        "up": n - r_q,
        "up_right": min(n-r_q, n-c_q),
        "right": n-c_q,
        "down_right": min(r_q-1,n-c_q),
        "down": r_q-1,
        "down_left": min(r_q-1, c_q-1),
        "left": c_q-1,
        "up_left": min(n-r_q, c_q-1)
    }

    # with the obstacle update the max reach
    for obs_r,obs_c in obstacles:
        row_dif = obs_r - r_q
        col_dif = obs_c - c_q

        if row_dif == 0:
            if col_dif > 0:
                max_reach["right"] = min(max_reach["right"], col_dif-1)
            else:
                max_reach["left"] = min(max_reach["left"], -col_dif-1)

        if col_dif == 0:
            if row_dif > 0:
                max_reach["up"] = min(max_reach["up"], row_dif-1)
            else:
                max_reach["down"] = min(max_reach["down"], -row_dif-1)

        elif abs(row_dif) == abs(col_dif):
            if row_dif > 0 and col_dif > 0:
                max_reach["up_right"] = min(max_reach["up_right"], row_dif - 1)
            elif row_dif > 0 > col_dif:
                max_reach["up_left"] = min(max_reach["up_left"], row_dif - 1)
            elif row_dif < 0 < col_dif:
                max_reach["down_right"] = min(max_reach["down_right"], -row_dif - 1)
            elif row_dif < 0 and col_dif < 0:
                max_reach["down_left"] = min(max_reach["down_left"], -row_dif - 1)

    return sum(max_reach.values())


if __name__ == '__main__':
    print(queensAttack(5, 3, 4, 3, [[5, 5], [4, 2], [2, 3]]))
