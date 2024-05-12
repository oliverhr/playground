
def search(arr: list[int], target: int) -> int:
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target: return mid

        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def main() -> None:
    array: list[int] = list(range(1, 50 + 1))
    target: int = 23
    print(f'Search for position of {target} in\n', array)
    index = search(array, 23)
    print(f'Index: {index} for value {array[index]}')


if __name__ == '__main__':
    main()

