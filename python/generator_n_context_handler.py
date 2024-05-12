'''
Generators

Generadores "YIELD", es una forma de controlar las iteraciones

En este ejemplo se usa el context handler "with" y "open" para
trabajar con archivos de texto que pueden resultar en un uso
intensivo de memoria en caso que este archivo contenga una
vasta cantidad de lines texto.
'''


def bad(filename: str) -> None:
    lines = open(filename).readlines()
    for line in lines:
        if len(line.strip()):
            print(line)


def good(filename: str) -> None:
    with open(filename) as file:
        for line in file:
            if line.strip():
                print(line)


def better(filename: str) -> None:
    def handler(line: str) -> None:
        if line.strip(): print(line)

    def gen():
        with open(filename) as file:
            for line in file:
                yield handler(line)

    for line in gen():
        pass


def main() -> None:
    path: str = './palindrome_checker.py'
    # bad(path)
    # good(path)
    better(path)


if __name__ == '__main__':
    main()

