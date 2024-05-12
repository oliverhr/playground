
arr = [4, 2, 7, 1, 3]

def selection_sort(arr: list[int]) -> list[int]:
    size: int = len(arr)

    for i in range(0, size):
        lowest = i
        for j in range(i + 1, size):
            if arr[j] < arr[lowest]:
                lowest = j
        if lowest != i:
            arr[i], arr[lowest] = arr[lowest], arr[i]
    return arr


def main():
    arr: list[int] = [4,2,7,1,3]
    res = selection_sort(arr)
    print(res)


if __name__ == '__main__':
    main()
