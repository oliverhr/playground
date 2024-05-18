

counter = 0

def fib(n, mem = {}):
    if n in mem: return mem[n]
    if (n <= 2): return 1
    mem[n] = fib(n-1) + fib(n-2)
    return mem[n]

if __name__ == '__main__':
    print(fib(6))
    print(fib(7))
    print(fib(8))
    print(fib(50))