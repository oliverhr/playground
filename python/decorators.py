def decorator(fn: callable) -> callable:
    def wrapper(*args, **kwargs):
        print('positional:', args)
        print('named:', kwargs)
        print('fn.__name__:', fn.__name__)
        fn(*args)
    return wrapper


@decorator
def decorated(ms: int) -> None:
    print('ms:', ms)


def main() -> None:
    decorated(10, just='for', fun='!')


if __name__ == '__main__':
    main()

