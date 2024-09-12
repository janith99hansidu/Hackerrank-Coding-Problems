from collections import deque


MOD = 10**9 + 7
def summingPieces(arr):
    # Initialize the deque with an empty list
    dp_arr = deque()

    # Add the first element
    dp_arr.append([arr[0], 1, arr[0]])  # (last piece value, length of last piece, total value of the list)

    for i in range(len(arr)-1):

        # Perform the operation for 2 ** i times
        for j in range(2 ** i):
            piece_val, len_piece, tot_val = dp_arr.popleft()

            # Make the next element with the last
            n_piece_val = piece_val + arr[i+1]
            n_len_piece = len_piece + 1
            n_tot_val = tot_val - piece_val * len_piece + n_piece_val * n_len_piece

            dp_arr.append((n_piece_val%MOD, n_len_piece, n_tot_val%MOD))

            # Make the next element without the last
            n_piece_val = arr[i+1]
            n_len_piece = 1
            n_tot_val = tot_val + n_piece_val

            dp_arr.append((n_piece_val%MOD, n_len_piece, n_tot_val%MOD))

    # You can return or print the result here for debugging or further use
    # For now, let's print the deque for debugging
    total = 0
    for element in dp_arr:
        total += element[2]
        total = total%MOD

    return total


if __name__ == '__main__':
    summingPieces([4, 2, 9, 10, 1])
    arr = [
        477, 392, 161, 421, 245, 50, 530, 889, 750, 16, 545, 303, 898, 785, 162,
        279, 677, 664, 126, 149, 814, 360, 334, 681, 473, 293, 267, 120, 825, 21,
        267, 301, 413, 779, 73, 657, 181, 602, 897, 930, 969, 441, 232, 218, 577,
        745, 848, 253
    ]
    summingPieces(arr)
