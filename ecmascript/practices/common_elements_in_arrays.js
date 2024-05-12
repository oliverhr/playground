/*
  Find the common elements in two sorted arrays
*/
const assert = require('node:assert');

function commonElements(a, b) {
  const mem = {};

  const length = Math.max(a.length, b.length);
  for (let i = 0; i < length; i++) {
    const itemA = a[i];
    const itemB = b[i];

    if (itemA) {
      mem[itemA] = mem[itemA] === undefined ? 0 : mem[itemA] + 1;
    }

    if (itemB) {
      mem[itemB] = mem[itemB] === undefined ? 0 : mem[itemB] + 1;
    }
  }

  const elements = [];

  Object.entries(mem)
    .forEach(([key, value]) => {
      if (value) elements.push(parseInt(key, 10));
    });

  return elements;
}


let result;

// should return [1, 4, 9]
result = commonElements(
  [1, 3, 4, 6, 7, 9],
  [1, 2, 4, 5, 9, 10],
);
console.log(result);
assert.deepStrictEqual(result, [1, 4, 9]);

// should return [1, 2, 9, 10, 12].
result = commonElements(
  [1, 2, 9, 10, 11, 12],
  [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15],
);
console.log(result);
assert.deepStrictEqual(result, [1, 2, 9, 10, 12]);

// should return [1, 2, 4, 5].
result = commonElements(
  [0, 1, 2, 3, 4, 5],
  [1, 2, 4, 5, 9, 10],
);
console.log(result);
assert.deepStrictEqual(result, [1, 2, 4, 5]);

// should return [] (an empty list).
result = commonElements(
  [0, 1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10, 11],
);
console.log(result);
assert.deepStrictEqual(result, []);
