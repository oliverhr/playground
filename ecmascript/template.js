/** ---------------------------------------------------------------------------
 *  Title
 *
 *  constraints:
 *    - ...
 *    - ...
 --------------------------------------------------------------------------- */
/* eslint-disable array-bracket-spacing, no-multi-spaces */

const assert = require('node:assert');

function implementation({ base, param }) {
  console.log(base, param);
  return false;
}

// ----------------------------------------------------------------------------

function test() {
  const base = [];
  let result = [];

  result = implementation({ base, param: [] });

  console.log('text:', result);

  assert.strictEqual(result, true, 'should return True');
}


const main = () => {
  test();
};

if (require.main === module) main();

