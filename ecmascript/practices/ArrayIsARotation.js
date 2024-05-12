/* ----------------------------------------------------------------------------
 *  Find if one array is a rotation of the other
 *
 *  constraints:
 *    - no duplicates in the passed arrays.
 *    - arrays has the same length
 --------------------------------------------------------------------------- */
const assert = require('node:assert');

function isRotation(base, rotated) {
  if (base.length !== rotated.length) return false;

  const size = base.length;
  const diff = rotated[0] - base[0];

  let pointerA;
  let pointerB;
  const movePointersToTheRight = () => { pointerA++; pointerB++; };

  // Initial position is over "base" array
  pointerA = 0;
  pointerB = size - diff;
  while (pointerB < size) { // pointerB is always the far right index
    if (base[pointerA] !== rotated[pointerB]) return false;
    movePointersToTheRight();
  }

  // Initial position is over "rotated" array
  pointerA = 0;
  pointerB = diff;
  while (pointerB < size) { // pointerB is always the far right index
    if (rotated[pointerA] !== base[pointerB]) return false;
    movePointersToTheRight();
  }

  return true;
}

// ----------------------------------------------------------------------------

let result = [];
const base = [1, 2, 3, 4, 5, 6, 7];

result = isRotation(base, [4, 5, 6, 7, 1, 2, 3]);
console.log('isRotation:', result);
assert.equal(result, true, 'should return True');

result = isRotation(base, [4, 5, 6, 7, 8, 1, 2, 3]);
console.log('isRotation:', result);
assert.equal(result, false, 'should return False');

result = isRotation(base, [4, 5, 6, 9, 1, 2, 3]);
console.log('isRotation:', result);
assert.equal(result, false, 'should return False');

result = isRotation(base, [4, 6, 5, 7, 1, 2, 3]);
console.log('isRotation:', result);
assert.equal(result, false, 'should return False');

result = isRotation(base, [4, 5, 6, 7, 0, 2, 3]);
console.log('isRotation:', result);
assert.equal(result, false, 'should return False');

result = isRotation(base, [7, 1, 2, 3, 4, 5, 6]);
console.log('isRotation:', result);
assert.equal(result, true, 'should return True');

result = isRotation(base, [1, 2, 3, 4, 5, 6, 7]);
console.log('isRotation:', result);
assert.equal(result, true, 'should return True');
