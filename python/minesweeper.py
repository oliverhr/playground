def mine_sweeper(bombs, num_rows, num_cols):
    # Set the board
    field = [[0] * num_cols for row in range(num_rows)]
    def field_counters(row, col):
        for r in range(row - 1, row + 2):
            if not 0 <= r < num_rows: continue
            for c in range(col - 1, col + 2):
                if (0 <= c < num_cols
                    and field[r][c] != -1):
                    field[r][c] += 1
    # Set the bombs
    for row, col in bombs:
        field[row][col] = -1
        # Set the warning counter
        field_counters(row, col)
    return field


# NOTE: Feel free to use the following function for testing.
# It converts a 2-dimensional array (a list of lists) into
# an easy-to-read string format.
def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'


# NOTE: The following input values will be used for testing your solution.
result = mine_sweeper([[0, 2], [2, 0]], 3, 3)
print('\n', to_string(result))
# should return:
# [[0, 1, -1],
#  [1, 2, 1],
#  [-1, 1, 0]]

# result = mine_sweeper([[0, 0], [0, 1], [1, 2]], 3, 4)
# should return:
# [[-1, -1, 2, 1],
#  [2, 3, -1, 1],
#  [0, 1, 1, 1]]

# result = mine_sweeper([[1, 1], [1, 2], [2, 2], [4, 3]], 5, 5)
# should return:
# [[1, 2, 2, 1, 0],
#  [1, -1, -1, 2, 0],
#  [1, 3, -1, 2, 0],
#  [0, 1, 2, 2, 1],
#  [0, 0, 1, -1, 1]]
