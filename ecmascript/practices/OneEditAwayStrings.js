/** ---------------------------------------------------------------------------
 * One Edit Away Strings
 *
 * Given two different strings return a boolean (true | false) if the
 * strings can be identical if a single valid edit is applied to one
 * of the strings, valid edits are: UPDATE | REMOVE | ADD a single
 * character, meaning that strings are One Edit Away to be identical.
 *
 * constraints:
 *   - All characters are lower case
 *   - BigO(N)
 --------------------------------------------------------------------------- */
/* eslint-disable array-bracket-spacing, no-multi-spaces */

const assert = require('node:assert');

const MAX_DIFF = 1;

function isOneAddOrRemoveAway(base, extra) {
  const [smaller, bigger] = (base.length > extra.length) ? [extra, base] : [base, extra];
  for (let i = 0, counter = 0; i < bigger.length; i++) {
    if (smaller[i] !== bigger[i + counter]) {
      counter++;
      if (counter > MAX_DIFF) return false;
    }
  }
  return true;
}

function isOneUpdateAway(base, extra) { // strings length is diff by one
  for (let i = 0, counter = 0; i < base.length; i++) {
    if (base[i] !== extra[i]) {
      counter++;
      if (counter > MAX_DIFF) return false;
    }
  }
  return true;
}

function isOneEditAway(base, extra) { // strings length are the same
  if (base === extra) return true;
  if (Math.abs(base.length - extra.length) > MAX_DIFF) return false;

  return (base.length === extra.length)
    ? isOneUpdateAway(base, extra)
    : isOneAddOrRemoveAway(base, extra);
}

// ----------------------------------------------------------------------------

function test([stringA, stringB, expected]) {
  const result = isOneEditAway(stringA, stringB);
  assert.strictEqual(result, expected, `${stringA} <=> ${stringB} : should return ${expected}.`);
}

const main = () => {
  [
    // same length
    ['a',       'a',      true],  // 1 equal then true
    ['abcdef',  'abqdef', true],  // 2
    ['abcdef',  'abccef', true],  // 3
    ['aaa',     'abc',    false], // 4 diff chars >= 2
    ['abc',     'bcc',    false], // 5 diff chars >= 2

    // different length
    ['abc',     'abcde',  false], // 6 length diff >= 2
    ['abcde',   'abc',    false], // 7 length diff >= 2

    // String1 has less chars
    ['bcde',    'abcde',  true],  // 10 rem e from the left
    ['abde',    'abcde',  true],  // 10 rem c in the middle
    ['abcd',    'abcde',  true],  // 10 rem e from the right

    // String1 has more chars
    ['abcdef',  'bcdef',  true],  // 8 add a to the left
    ['abcde',   'abce',   true],  // 9 add c in the middle
    ['abcdef',  'abcde',  true],  // 8 add f to the right

  ].forEach(test);
};

if (require.main === module) main();
