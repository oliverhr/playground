function gridTraveler(m, n) {
    const mem = new Map()
    const fn = (x, y) => {
        const key = `${x},${y}`

        if (mem.has(key)) return mem.get(key)
        if (x * y === 1) return 1
        if (x * y <= 0) return 0

        mem.set(key, fn(x-1, y) + fn(x, y-1))
        return mem.get(key)
    }
    return fn(m, n)
}

const grids = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1],
    [2, 3],
    [3, 3],
    [8, 8],
    [18, 18],
]

console.log('------------------------')
grids.forEach(([x, y]) => console.log(`${x}, ${y}: ${gridTraveler(x, y)}`))
