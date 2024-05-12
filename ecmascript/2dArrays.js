// Rotate the contents of a vector.

const array =[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
]

const expected =[
  [7, 4, 1],
  [8, 5, 2],
  [9, 6, 3],
]

const numRows = 4
const numCols = 5

// ----------------------------------------------------------------------------
let matrix = []
console.log(matrix)

// DONT DONT DONT every row array is shallow copy
matrix = Array(numRows).fill(Array(numCols).fill(null))
matrix[0][0] = 0
console.log(matrix)

// ----------------------------------------------------------------------------
matrix = Array();
for (let r = 0; r < numRows; r++) {
  matrix.push([]);
  const row = matrix[r];
  for (let c = 0; c < numCols; c++) {
    const col = c+1
    row.push(col);
  }
}
console.log(matrix)

// ----------------------------------------------------------------------------
matrix = Array.from(Array(numRows), () => new Array(numCols).fill(0))
console.log(matrix)

// ----------------------------------------------------------------------------
matrix = Array(numRows)
for (let i = 0; i < matrix.length; i++) {
  matrix[i] = Array(numCols).fill(0)
}
console.log(matrix)

// ----------------------------------------------------------------------------
// Best approach when an initialized matrix is required
function ones(breadth, depth, content = null) {
  return Array.from(Array(breadth), () => new Array(depth).fill(content))
}

console.log('Matrix:', ones(numRows, numCols))

