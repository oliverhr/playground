'''
From a passed array of integers return the mean average of all its even numbers

Indicate the BigO category for this algorithm.
'''

def average_of_even_nums(numbers: [int]) -> float:
    total: float = 0.0
    counter: int = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
            counter += 1
    return total / counter


def main():
    arr: list[int] = [3, 4, 7, 1, 2]
    res: float = average_of_even_nums(arr)
    print(res)


if __name__ == '__main__':
    main()

