/** ---------------------------------------------------------------------------
 *  Mine Sweeper
 *
 *  Implement a program that assigns correct numbers in file of mineswapper,
 *  which is represented as a 2 dimensional array.
 *
 *  constraints:
 *    - Array of arrays
 *    - Return a 2d array
 *
 *  Cell information or mark:
 *    - (0) represents that there are no surrounding bombs
 *    - (-1) represents that there is a bomb in the location
 *    - (1..8) represents the surrounding cells with a bomb
 *             4 for each adjacent cell for side
 *             4 for each diagonal adjacent cell
 *
 *  Arguments:
 *    - Bombs: a tuple of pairs with the bombs locations (assume no duplicates)
 *    - rows: The number of rows for the field
 *    - cols: The number of columns for the field
 --------------------------------------------------------------------------- */
/* eslint-disable array-bracket-spacing, no-multi-spaces */

const assert = require('node:assert');

const REVEALED = -2;

class MineSweeper {
  #board = [];

  #bombs = [];

  #rows = 0;

  #cols = 0;

  constructor(rows = 0, cols = 0, bombs = null) {
    this.#rows = rows;
    this.#cols = cols;

    this.#boardFactory();

    if (bombs !== null && Array.isArray(bombs) && bombs.length >= 1) {
      this.setBombs(bombs);
    }
  }

  static get REVEALED() {
    return REVEALED;
  }

  get board() {
    return this.#board;
  }

  #boardFactory() {
    for (let i = 0; i < this.#rows; i++) {
      const row = [];
      for (let j = 0; j < this.#cols; j++) {
        row.push(0);
      }
      this.#board.push(row);
    }
  }

  setBombs(bombs = []) {
    if (this.#bombs.length !== 0) return;
    this.#bombs = bombs;

    for (const coord of bombs) {
      this.#placeMine(coord);
      this.#surroundingCellsWarning(coord);
    }
  }

  #placeMine([row, col]) {
    this.#board[row][col] = -1;
  }

  #surroundingCellsWarning([row, col]) {
    const rows = [row - 1, row, row + 1];
    const cols = [col - 1, col, col + 1];

    for (const r of rows) {
      if (r >= 0 && r < this.#rows) {     // only rows not out index
        for (const c of cols) {
          if ((c >= 0 && c < this.#cols)  // valid not out of index
            && (this.#board[r][c] !== -1) // cells with no bombs
          ) this.#board[r][c]++;
        }
      }
    }
  }

  #iterablesRowsCols(row, col) {
    const rows = [row - 1, row, row + 1];
    const cols = [col - 1, col, col + 1];

    return [rows, cols];
  }

  *#cellIterator(center) {
    yield center - 1;
    yield center;
    yield center + 1;
  }

  click([row, col]) {
    if (this.#board[row][col] === 0) this.#depthFirstReveal(row, col);
  }

  #depthFirstReveal(row, col) {
    const [rows, cols] = this.#iterablesRowsCols(row, col);
    for (const r of rows) {
      if (r >= 0 && r < this.#rows) {
        for (const c of cols) {
          if ((c >= 0 && c < this.#cols) && this.#board[r][c] === 0) {
            this.#board[r][c] = REVEALED;
            this.#depthFirstReveal(r, c);
          }
        }
      }
    }
  }

  touch([row, col]) {
    if (this.#board[row][col] !== 0) return;
    this.#board[row][col] = REVEALED;
    this.#breadthFirstReveal(row, col);
  }

  #breadthFirstReveal(row, col) {
    const queue = [[row, col]];
    while (queue.length) {
      const [row, col] = queue.shift();

      for (const r of this.#cellIterator(row)) {
        if (r >= 0 && r < this.#rows) {
          for (const c of this.#cellIterator(col)) {
            if ((c >= 0 && c < this.#cols) && this.#board[r][c] === 0) {
              this.#board[r][c] = REVEALED;
              queue.push(([r, c]));
            }
          }
        }
      }
    }
  }

  display() {
    const lines = (this.#cols ** 2) + this.#cols;
    console.log(`\n${'-'.repeat(lines)}`);
    for (let r = 0; r < this.#rows; r++) {
      for (let c = 0; c < this.#cols; c++) {
        process.stdout.write(`${this.#board[r][c]}`.padStart(3));
      }
      console.log('');
    }
    console.log(`${'-'.repeat(lines)}\n`);
  }
}

// ----------------------------------------------------------------------------

function test1() {
  const bombs = [[0, 2], [2, 0]];
  const rows = 3;
  const cols = 3;

  const game = new MineSweeper(rows, cols);
  // game.display();
  game.setBombs(bombs);
  // game.display();

  const expected = [
    [  0, 1, -1],
    [  1, 2,  1],
    [ -1, 1,  0],
  ];
  assert.deepStrictEqual(game.board, expected);
}

function test2() {
  const bombs = [[0, 0], [0, 1], [1, 2]];
  const rows = 3;
  const cols = 4;

  const game = new MineSweeper(rows, cols);
  game.setBombs(bombs);

  const expected = [
    [-1, -1,  2, 1],
    [ 2,  3, -1, 1],
    [ 0,  1,  1, 1],
  ];
  assert.deepStrictEqual(game.board, expected);
}

function test3() {
  const bombs = [[1, 1], [1, 2], [2, 2], [4, 3]];
  const rows = 5;
  const cols = 5;

  const game = new MineSweeper(rows, cols, bombs);

  const expected = [
    [1,  2,  2,  1, 0],
    [1, -1, -1,  2, 0],
    [1,  3, -1,  2, 0],
    [0,  1,  2,  2, 1],
    [0,  0,  1, -1, 1],
  ];

  assert.deepStrictEqual(game.board, expected);
}

function test4() {
  const bombs = [[2, 2]];
  const rows = 3;
  const cols = 5;

  const game = new MineSweeper(rows, cols, bombs);

  const expected = [
    [0, 0,  0, 0, 0],
    [0, 1,  1, 1, 0],
    [0, 1, -1, 1, 0],
  ];
  assert.deepStrictEqual(game.board, expected);

  game.click([2, 2]);
  const expectedAfterClick1 = [
    [0, 0,  0, 0, 0],
    [0, 1,  1, 1, 0],
    [0, 1, -1, 1, 0],
  ];
  assert.deepStrictEqual(game.board, expectedAfterClick1);

  game.click([1, 4]);
  const expectedAfterClick2 = [
    [-2, -2, -2, -2, -2],
    [-2,  1,  1,  1, -2],
    [-2,  1, -1,  1, -2],
  ];
  assert.deepStrictEqual(game.board, expectedAfterClick2);
}

function test5() {
  const bombs = [[0, 0], [3, 3]];
  const rows = 4;
  const cols = 4;

  const game = new MineSweeper(rows, cols, bombs);

  const expected = [
    [-1, 1, 0,  0],
    [ 1, 1, 0,  0],
    [ 0, 0, 1,  1],
    [ 0, 0, 1, -1],
  ];
  assert.deepStrictEqual(game.board, expected);

  game.click([0, 1]);
  const expectedAfterClick1 = [
    [-1, 1, 0,  0],
    [ 1, 1, 0,  0],
    [ 0, 0, 1,  1],
    [ 0, 0, 1, -1],
  ];
  assert.deepStrictEqual(game.board, expectedAfterClick1);

  game.click([1, 3]);
  const expectedAfterClick2 = [
    [-1,  1, -2, -2],
    [ 1,  1, -2, -2],
    [-2, -2,  1,  1],
    [-2, -2,  1, -1],
  ];
  assert.deepStrictEqual(game.board, expectedAfterClick2);
}

function test6() {
  const bombs = [[0, 0], [3, 3]];
  const rows = 4;
  const cols = 4;

  const game = new MineSweeper(rows, cols, bombs);

  const expected = [
    [-1, 1, 0,  0],
    [ 1, 1, 0,  0],
    [ 0, 0, 1,  1],
    [ 0, 0, 1, -1],
  ];
  assert.deepStrictEqual(game.board, expected);

  game.touch([0, 1]);
  const expectedAfterClick1 = [
    [-1, 1, 0,  0],
    [ 1, 1, 0,  0],
    [ 0, 0, 1,  1],
    [ 0, 0, 1, -1],
  ];
  assert.deepStrictEqual(game.board, expectedAfterClick1);

  game.touch([1, 3]);
  const expectedAfterClick2 = [
    [-1,  1, -2, -2],
    [ 1,  1, -2, -2],
    [-2, -2,  1,  1],
    [-2, -2,  1, -1],
  ];
  assert.deepStrictEqual(game.board, expectedAfterClick2);
}

const main = () => {
  // test1();
  // test2();
  // test3();
  // test4();
  test5();
  test6();
};

if (require.main === module) main();

module.exports = function mineSweeper(bombs = [], rows = 0, cols = 0) {
  const game = new MineSweeper(rows, cols);
  game.setBombs(bombs);
  return game.board;
};

