'''
count the Ones

This function acceptes an array of arrays, where the inner array,
contains 1s and 0s. The functon the returns how many 1s there are.
'''

# O(n)

def count_ones(collection: list[list[int]]) -> int:
    counter: int = 0
    steps: int = 0

    for array in collection:
        for number in array:
            steps += 1
            counter += 1 if number == 1 else 0
    print(f'Steps {steps}')
    return counter


def main() -> None:
    collection: list[list[int]] = [
            [0, 1, 0, 0, 1],
            [1, 0, 0, 0, 1],
    ]
    print(count_ones(collection))

    collection.append([1, 0, 1, 0, 0])
    print(count_ones(collection))

    collection.append([1, 0, 1, 0, 1])
    print(count_ones(collection))


if __name__ == '__main__':
    main()

