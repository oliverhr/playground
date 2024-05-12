def countdown(low: int, high: int) -> None:
    if low > high: return None
    print(high)
    countdown(low, high - 1)


def to_zero(n):
    return countdown(0, n)


def doubles(array: list[int], index: int = 0) -> None:
    if index >= len(array): return None
    array[index] *= 2
    doubles(array, index + 1)


def alreves(cadena):
    # print(cadena)
    if len(cadena) == 1: return cadena[0]
    return alreves(cadena[1:]) + cadena[0]


def main() -> None:
    # tozero(10)

    # array: list[int] = [1, 2, 3, 4]
    # print(f'Before: {array}')
    # doubles(array)
    # print(f'After: {array}')

    words: list[str] = [
        'revilo',
        'ogaleicrum',
        'perro',
    ]
    for word in words:
        print(word, alreves(word))


if __name__ == '__main__':
    main()

