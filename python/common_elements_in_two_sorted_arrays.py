from itertools import zip_longest

# Implement your function below.
def common_elements(a, b):
    mem = {}
    for itemA, itemB in zip_longest(a, b):
        if itemA is not None: mem[itemA] = mem.get(itemA, -1) + 1
        if itemB is not None: mem[itemB] = mem.get(itemB, -1) + 1
    return [key for key, value in mem.items() if value > 0]

# NOTE: The following input values will be used for testing your solution.

# should return [1, 4, 9] (a list).
print(common_elements([1, 3, 4, 6, 7, 9],
                      [1, 2, 4, 5, 9, 10]))

# should return [1, 2, 9, 10, 12] (a list).
print(common_elements([1, 2, 9, 10, 11, 12],
                      [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15]))


# should return [1, 2, 4, 5] (a list).
print(common_elements([0, 1, 2, 3, 4, 5],
                      [1, 2, 4, 5, 9, 10]))

# should return [] (an empty list).
print(common_elements([0, 1, 2, 3, 4,   5],
                      [6, 7, 8, 9, 10, 11]))
