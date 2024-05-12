'''
Dynamic programming
'''


def fun(nums: list[int]) -> int:
    """
    Minimum possible sum
    """
    res: int = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            print(i, j, nums[i:j])

    return res


def main() -> None:
    nums: list[int] = [-7, 3, 4, -2, -3, 1, -3]
    print(f'Result: {fun(nums)}')


if __name__ == '__main__':
    main()
