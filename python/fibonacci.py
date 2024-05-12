'''
Dynamic programming
'''

def recursive(n: int) -> int:
    if n <= 1: return n
    return recursive(n - 1) + recursive(n - 2)


def dynamic(n: int) -> int:
    lookup: dict[int, int] = {}

    def fib(n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        if n in lookup: return lookup[n]

        lookup[n] = fib(n - 1) + fib(n - 2)
        return lookup[n]

    return fib(n)


# -----------------------------------------------------------------------------

def main() -> None:
    print(dynamic(610))
    print(recursive(610))


if __name__ == '__main__':
    main()

