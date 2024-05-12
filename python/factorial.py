

def factorial(n: int) -> int:
    return n * factorial(n - 1) if n > 1 else 1


def main() -> None:
    print(factorial(3))
    print(factorial(5))


if __name__ == '__main__':
    main()


