/* ----------------------------------------------------------------------------
 *  Non repeated character
 *
 *  Implement a function that takes a string and returns the
 *  first character that does not appear twice or more.
 *
 *  constraints:
 *    - The first unique element is the expected if multiple uniques exists
 *    - All characters are upper or lower case but not mixed
 *    - if there are non-repeating characters return an empty string
 --------------------------------------------------------------------------- */
const assert = require('node:assert');

function nonRepeating(string) {
  const mem = new Map();

  for (const ch of string) {
    mem.set(ch, (mem.get(ch) ?? 0) + 1);
  }

  for (const [char, counter] of mem) {
    if (counter === 1) return char;
  }

  return '';
}

// ----------------------------------------------------------------------------
function main() {
  let string = 'aabbcb';
  let result = nonRepeating(string);
  let expected = 'c';
  console.log(`Non repeating character in "${string}" is '${result}'`);
  assert.strictEqual(result, expected, `should return '${expected}'`);

  string = 'xxyz';
  result = nonRepeating(string);
  expected = 'y';
  console.log(`Non repeating character in "${string}" is '${result}'`);
  assert.strictEqual(result, expected, `should return '${expected}'`);

  string = 'abcab';
  result = nonRepeating(string);
  expected = 'c';
  console.log(`Non repeating character in "${string}" is '${result}'`);
  assert.strictEqual(result, expected, `should return '${expected}'`);

  string = 'abab';
  result = nonRepeating(string);
  expected = '';
  console.log(`Non repeating character in "${string}" is '${result}'`);
  assert.strictEqual(result, expected, `should return '${expected}'`);

  string = 'aabbbc';
  result = nonRepeating(string);
  expected = 'c';
  console.log(`Non repeating character in "${string}" is '${result}'`);
  assert.strictEqual(result, expected, `should return '${expected}'`);

  string = 'aabbdbc';
  result = nonRepeating(string);
  expected = 'd';
  console.log(`Non repeating character in "${string}" is '${result}'`);
  assert.strictEqual(result, expected, `should return '${expected}'`);
}

if (process.argv[1] === __filename) {
  main();
}
