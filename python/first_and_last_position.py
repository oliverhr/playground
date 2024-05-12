# ---------------------------------------------------------
# Given a sorted array of integers "arr" and an integer
# target, find teh index of the first and last position
# of "target" in arr.
#
# If target can't be found in arr, return [-1, -1]
# ---------------------------------------------------------

def linear(arr: list[int], target: int) -> list[int]:
    position: list[int] = [-1, -1]
    for i, item in enumerate(arr):
        if item != target: continue
        if position[0] == -1: position[0] = i
        else: position[1] = i
    return position


def binary(arr: list[int], target: int) -> list[int]:
    position: list[int] = [-1, -1]

    left = 0
    right = len(arr) - 1

    while -1 in position:
        if position[0] == -1 and arr[left] == target:
            position[0] = left
        else:
            left += 1

        if position[1] == -1 and arr[right] == target:
            position[1] = right
        else:
            right -= 1

    return position


def main() -> None:
    arr: list[int] = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]
    target = 5

    res_lin: list[int] = linear(arr, target)
    print(res_lin)

    res_bin: list[int] = binary(arr, target)
    print(res_bin)


if __name__ == '__main__':
    main()

