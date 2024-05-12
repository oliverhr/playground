'''
Insertion sort

algorithm implementation in python
O(n^2)
'''

def sort(numbers: list[int]) -> None:
    for i in range(1, len(numbers)):
        current = numbers[i]
        left = i
        for right in reversed(range(i)):
            if numbers[right] < current:
                break
            swap(numbers, left, right)
            left -= 1


def insertion_sort(items: list[int]) -> None:
    for i in range(1, len(items)):
        j: int = i
        while j > 0 and items[j-1] > items[j]:
            swap(items, j-1, j)
            j -= 1


def swap(arr: list[int], left: int, right: int) -> None:
    arr[left], arr[right] = arr[right], arr[left]


def main():
    arr: list[int] = [4, 2, 7, 1, 3]
    print(f'Original array: {arr}')

    sort(arr)
    print(f'Sorted array: {arr}')

    insertion_sort(arr)
    print(f'Sorted array: {arr}')


if __name__ == '__main__':
    main()

