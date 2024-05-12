def is_rotation(list1: list[int], list2: list[2]) -> bool:
    # if list length are differen is not a rotation
    if len(list1) != len(list2): return False

    size: int = len(list1)

    # get the first value of the first array
    key_value = list1[0]
    # Varaible to store the index for the key
    key_index = -1

    # Look on the second array for where the
    # initial value from the first key coincide
    for i in range(size):
        if list2[i] == key_value:
            key_index = i
            break

    # If the key remain with -1 means no concidence
    if key_index == -1: return False

    # Iteration with two moving pointers (i, j)
    for i in range(size):
        # this is the trick part, this operation
        # get the index for the second pointer
        j = (key_index + i) % size
        # print('(', key_index, '+', i, ') % ' , size, ' = ', j)

        # If there is a discrenpancy is not a rotation
        if list1[i] != list2[j]: return False

    return True

def main():
    result: bool
    baseArray: list[int] = [1, 2, 3, 4, 5, 6, 7]

    # should return true.
    result = is_rotation(baseArray, [4, 5, 6, 7, 1, 2, 3])
    print(result);

    # should return false.
    result = is_rotation(baseArray, [4, 5, 6, 7, 8, 1, 2, 3])
    print(result);

    # should return false.
    result = is_rotation(baseArray, [4, 5, 6, 9, 1, 2, 3])
    print(result);

    # should return false.
    result = is_rotation(baseArray, [4, 6, 5, 7, 1, 2, 3])
    print(result);

    # should return false.
    result = is_rotation(baseArray, [4, 5, 6, 7, 0, 2, 3])
    print(result);

    # should return true.
    result = is_rotation(baseArray, [1, 2, 3, 4, 5, 6, 7])
    print(result);

if __name__ == '__main__':
    main()
