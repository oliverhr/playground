/** ---------------------------------------------------------------------------
 *  Matrix clockwise rotation
 *
 *  With a given a two dimentional array ordered naturally [1, 2, 3]
 *  change its contents with a rotation to the right like 90 degree
 *  rotation.
 *  [1
 *   2
 *   3]
 *
 *  These means that in a matrix of 3 * 3, items should be changed
 *  in this way:
 *  - 1 from [0, 0], to [0, 2]
 *  - 2 from [0, 1], to [1, 2]
 *  - 3 from [0, 2], to [2, 2]
 *
 *  constraints:
 *    - expect a two dimensional array of x * x (square shape)
 *    - original numeric values are sorted
 --------------------------------------------------------------------------- */
/* eslint-disable array-bracket-spacing, no-multi-spaces */

const assert = require('node:assert');

function replace(matrix) {
  const rows = matrix.length
  const cols = matrix[0].length
  const size = matrix.length - 1

  const collection = Array.from(Array(rows), () => Array(cols))

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      collection[j][size-i] = matrix[i][j]
    }
  }

  return collection
}

function rotateIndexes(row, col, length) {
  const rowIndex = col;
  const colIndex = (length - 1) - row;
  return [rowIndex, colIndex]
}

function inplace(matrix) {
  if (matrix.length < 2) return;

  const CORNERS = 4
  const size = matrix.length

  const limitR = Math.ceil(size / 2);
  const limitC = Math.floor(size / 2);

  for (let r = 0; r < limitR; r++) {
    for (let c = 0; c < limitC; c++) {
      const mem = Array(CORNERS)
      let [x, y] = [r, c]

      for (let k = 0; k < CORNERS; k++) {
        mem[k] = matrix[x][y]; // semi if not intepreted as matrix[x][y][x,y]
        [x, y] = rotateIndexes(x, y, size)
      }

      for (let k = 0; k < CORNERS; k++) {
        const index = (k + 3) % CORNERS
        matrix[x][y] = mem[index] // Read about ASI (automatic semicolon insertion)
        ;[x, y] = rotateIndexes(x, y, size) // at developer.mozilla.org
      }
    }
  }

  return matrix;
}

// ----------------------------------------------------------------------------

function test3() {
  const original =[
    [ 1,  2,  3,  4,  5],
    [ 6,  7,  8,  9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
  ]
  const expected =[
    [ 21, 16, 11,  6, 1],
    [ 22, 17, 12,  7, 2],
    [ 23, 18, 13,  8, 3],
    [ 24, 19, 14,  9, 4],
    [ 25, 20, 15, 10, 5],
  ]
  assert.deepStrictEqual(replace(original), expected);
  assert.deepStrictEqual(inplace(original), expected);
}

function test2() {
  const original = [
    [ 1,  2,  3,  4],
    [ 5,  6,  7,  8],
    [ 9, 10, 11, 12],
    [13, 14, 15, 16]
  ]
  const expected = [
    [13,  9, 5, 1],
    [14, 10, 6, 2],
    [15, 11, 7, 3],
    [16, 12, 8, 4],
  ]
  assert.deepStrictEqual(replace(original), expected);
  assert.deepStrictEqual(inplace(original), expected);
}

function test1() {
  const original =[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
  ]
  const expected =[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3],
  ]
  assert.deepStrictEqual(replace(original), expected);
  assert.deepStrictEqual(inplace(original), expected);
}

function test0() {
  const original =[
    [1, 2],
    [3, 4],
  ]
  const expected =[
    [3, 1],
    [4, 2],
  ]

  assert.deepStrictEqual(replace(original), expected);
  assert.deepStrictEqual(inplace(original), expected);
}


const main = () => {
  test0()
  test1()
  test2()
  test3()
};

if (require.main === module) main();

