import random


def linear(numbers, target):
    steps = 0
    # default return value "-1" if not found
    position = -1

    # iterate through every element in the array
    for index, number in enumerate(numbers):
        steps += 1
        # when first match occurs assign the index an break the loop
        if numbers[index] == target:
            position = index
            break
    return position, steps


def binaryFromEndsToMiddle(numbers, target):
    steps = 1
    size = len(numbers)
    # stablish the lower and upper bound
    left = 0
    right = size - 1

    # Check if the middle item is the searched number
    if size % 2 == 1 and numbers[size // 2] == target:
        return size // 2, steps

    # loop from the ends, up to the middle of the array
    # *---> * <---*
    while left < right:
        if numbers[left] == target: return left, steps
        if numbers[right] == target: return right, steps
        left += 1
        right -= 1
        steps += 1

    return -1, steps


def binaryFromMiddleToEnds(numbers, target):
    steps = 1
    size = len(numbers)
    right = size // 2
    left = right - 1

    if size % 2 == 1:
        if numbers[right] == target: return right, steps
        right += 1

    # loop from the middle to the beginning and the end for the array
    # <--- ** --->
    while left >= 0 and right < size:
        if numbers[left] == target: return left, steps
        if numbers[right] == target: return right, steps
        left, right = (left - 1, right + 1)
        steps += 1
    return -1, steps


def binary(numbers, target):
    numbers.sort()
    steps = 1

    # Set te initial index for the lower and the upper ends
    left = 0
    right = len(numbers) - 1

    print('size:', len(numbers))
    while left <= right:
        middle = (left + right) // 2

        # if middle point is the searched value return the index
        if target == numbers[middle]: return middle, steps

        # now we check what half to follow in the ordered collection
        if target < numbers[middle]:
            right = middle - 1 # continue to the right part
        else:
            left = middle + 1  # continue to the left part

        steps += 1


def search():
    # start = 1
    # limit = 101

    # arr = list(range(start, limit + 1))
    # random.shuffle(arr)

    # print('Array:', arr)

    # if len(arr) % 2 == 1:
    #     print(len(arr) // 2, ' = ', arr[len(arr) // 2], '\n')

    # num = int(input('Enter a number from {} to {}: '.format(start, limit)))
    # print('Size:', len(arr))
    # print('Target', num, '\n')
    # print('Index:', arr.index(num))
    # print('Linear:', linear(arr, num))
    # print('Binary')
    # print('FromEndsToMiddle:', binaryFromEndsToMiddle(arr, num))
    # print('FromMiddleToEnds:', binaryFromMiddleToEnds(arr, num))

    max = 128
    print('Binary:', binary(list(range(max)), int(input(f'Enter a number from {1} to {max-1}:'))))



def is_leap(year):
    if (year % 100 == 0):
        return year % 400 == 0
    else:
        return year % 4 == 0

def chess_board_boxes(number_of_grains):
    boxes_counter = 1
    placed_grains = 1

    while placed_grains < number_of_grains:
        placed_grains *= 2
        boxes_counter += 1

    return boxes_counter


if __name__ == '__main__':
    print(chess_board_boxes(32))

