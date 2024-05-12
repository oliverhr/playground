# Implement your function below.
def most_frequent(given_list):
    if len(given_list) == 0: return None

    mem = {}
    max_item = { "number": None, "count": 0 }

    for item in given_list:
        mem[item] = mem.get(item, 0) + 1
        if max_item["count"] < mem[item]:
            max_item["number"] = item
            max_item["count"] = mem[item]
    return max_item["number"]

# NOTE: The following input values will be used for testing your solution.

# most_frequent(list1) should return 1
list1 = [1, 3, 1, 3, 2, 1]
print(most_frequent(list1))

# most_frequent(list2) should return 3
list2 = [3, 3, 1, 3, 2, 1]
print(most_frequent(list2))

# most_frequent(list3) should return None
list3 = []
print(most_frequent(list3))

# most_frequent(list4) should return 0
list4 = [0]
print(most_frequent(list4))

# most_frequent(list5) should return -1
list5 = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]
print(most_frequent(list5))
