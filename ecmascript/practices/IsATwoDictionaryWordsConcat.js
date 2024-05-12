/** ---------------------------------------------------------------------------
 *  Write a function that given a string, determines,
 *  if it's a concatenation of two words, contained
 *  in a dictionary of words.
 *
 *  constraints:
 *    - the dictionary access is available as a function
 *    - analize the time complexity for the solution
 --------------------------------------------------------------------------- */
/* eslint-disable array-bracket-spacing, no-multi-spaces */

const assert = require('node:assert');

function inDict(word) {
  const list = [
    'car', 'foo', 'bar', 'baz' ,'abcd',
    'tree', 'news', 'geeks', 'paper', 'port',
    'qux', 'nut', 'sheet', 'dock',
  ];
  return list.includes(word);
}


function segmentString(input) {
  const mem = new Map();
  let counter = 0;

  const fn = (str) => {
    if (inDict(str)) return true;
    if (mem.has(str)) return false;

    const len = str.length;
    for (let i = 1; i < len; i++) {
      const prefix = str.slice(0, i);
      const sufix = str.slice(i, len);

      counter++;
      if (inDict(prefix) && fn(sufix)) return true;
    }
    mem.set(input, null);
    return false;
  }
  const result = fn(input);
  console.log(counter);
  console.log(Array.from(mem.keys()))
  return result;
}

function splitString(input) {
  let counter = 0;
  const fn = (str) => {
    if (inDict(str)) return true;

    const len = str.length;
    for (let i = 1; i < len; i++) {
      const prefix = str.slice(0, i);
      const sufix = str.slice(i, len);

      counter++;
      if (inDict(prefix) && fn(sufix)) return true;
    }
    return false;
  }
  const result = fn(input);
  console.log(counter)
  return result;
}


function devideString(input) {
  const len = input.length;
  let counter = 0;

  const fn = () => {
    for (let i = 1; i < len; i++) {
      const prefix = input.substring(0, i);
      const suffix = input.substring(i, len);

      counter++;
      if (inDict(prefix) && inDict(suffix)) return true;
    }
    return false;
  }
  const result = fn();
  console.log(counter);
  return result;
}

// ----------------------------------------------------------------------------

function testDevindeString() {
  const result = devideString('newspaper')
  assert.strictEqual(result, true, 'should return True');
}

function testSplitString() {
  let result = splitString('newspapertree');
  assert.strictEqual(result, true, 'should return True');
}

function testSegmentString() {
  let result = segmentString('newspapertreeport');
  assert.strictEqual(result, true, 'should return True');
}


const main = () => {
  //testDevindeString()
  //testSplitString();
  testSegmentString();
};

if (require.main === module) main();

