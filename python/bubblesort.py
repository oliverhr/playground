
import random

# ------- UTILITIES -------

def get_array(size):
    '''
    Generate the array for the example
    '''
    array = list(range(1, size + 1))
    random.shuffle(array)
    return array

def swap(array, x, y):
    '''
    Swap the elements from the passed array
    '''
    array[x], array[y] = array[y], array[x]

# ------- IMPLEMENTATION -------

def bubble_sort(array):
    for idx, _ in enumerate(array):
        for nxt in range(idx + 1, len(array)):
            if array[idx] > array[nxt]:
                swap(array, idx, nxt)

def _bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                swap(array, i, j)


def __bubble_sort(array):
    unsorted_until_index = len(array) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            if array[i] > array[i+1]:
                swap(array, i, i+1)
                sorted = False
        unsorted_until_index -= 1


# ------- START -------

if __name__ == '__main__':
    array = get_array(10)
    print(array)
    bubble_sort(array)
    print(array)

