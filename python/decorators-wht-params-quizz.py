# ---------------------------------------------------------
# Why this code returns the error?:
#
#   TypeError: 'NoneType' object is not callable
#
# ---------------------------------------------------------


def concat(symbol: str) -> callable:
    def inner(fn):
        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs) + symbol
    return inner


@concat('!!')
def hello(name: str) -> str:
    return 'Hello' + name


print(hello('oliver'))

