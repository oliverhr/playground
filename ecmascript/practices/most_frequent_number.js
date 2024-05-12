/*
  Find the most frequent numbers in collection of numbers
*/

function mostFrequent(array) {
  if (array.length === 0) return NaN;

  const mem = new Map();
  let frequent = {
    number: undefined,
    count: 0,
  };

  for (const number of array) {
    const count = mem.get(number) ? mem.get(number) + 1 : 1;
    mem.set(number, count);

    if (frequent.count < count) frequent = { number, count };
  }
  return frequent.number;
}


// should return 1.
const array1 = [1, 3, 1, 3, 2, 1];
console.log(`Expected: 1, result ${mostFrequent(array1)}`);

// should return 3.
const array2 = [3, 3, 1, 3, 2, 1];
console.log(`Expected: 3, result ${mostFrequent(array2)}`);

// should return null.
const array3 = [];
console.log(`Expected: NaN, result ${mostFrequent(array3)}`);

// should return 0.
const array4 = [0];
console.log(`Expected: 0, result ${mostFrequent(array4)}`);

// should return -1.
const array5 = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1];
console.log(`Expected: -1', result ${mostFrequent(array5)}`);
