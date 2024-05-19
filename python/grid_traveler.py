def grid_traveler(m, n):
    def fn(x, y, mem = {}):
        if x * y == 1: return 1
        if x * y <= 0: return 0
        if (id := f'{x},{y}') in mem: return mem[id]
        mem[id] = fn(x-1, y) + fn(x, y-1)
        return mem[id]
    return fn(m, n)


if __name__ == '__main__':
    grids = [
        (0, 0),
        (0, 1),
        (1, 0),
        (1, 1),
        (2, 3),
        (3, 3),
        (8, 8),
        (18, 18),
    ]
    for x, y in grids:
        print(f'{x},{y}: {grid_traveler(x, y)}')
