'''
100-Sum Array
extemes added sum a hundred?
'''

def one_hundred_sum(array: list[int]) -> bool:
    ileft: int = 0
    iright: int = len(array) - 1

    while ileft < len(array) / 2:
        summ: int = array[ileft] + array[iright]
        if summ == 100: return True
        ileft += 1
        iright -= 1
    return False


def main() -> None:
    array: list[int] = [20, 20, 15, 85, 35, 90]
    res: bool = one_hundred_sum(array)
    print(f'Sum 100?: {res}')


if __name__ == '__main__':
    main()

