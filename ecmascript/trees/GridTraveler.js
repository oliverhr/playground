function gridTraveler(x, y) {
    if (x * y === 1) return 1
    if (x * y === 0) return 0
    return gridTraveler(x-1, y) + gridTraveler(x, y-1)
}

const grids = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1],
    [2, 3],
    [3, 3],
    [8, 8],
    // [18, 18],
]

grids.forEach(([x, y]) => console.log(`${x}, ${y}: ${gridTraveler(x, y)}`))
