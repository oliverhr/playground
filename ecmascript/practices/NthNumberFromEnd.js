/** ---------------------------------------------------------------------------
 *  Nth node from End
 *
 *  Implement a function that finds and returns the nth node
 *  in a linked list, counting from the end.
 *
 *  constraints:
 *    - If the given n is larger than the number of nodes
 *      in the list, return null / None.
 --------------------------------------------------------------------------- */
/* eslint-disable array-bracket-spacing, no-multi-spaces */
const assert = require('node:assert');

class Node {
  #value = NaN;
  #previous = null
  #next = null;

  constructor(value) {
    this.#value = value;
  }

  get value() {
    return this.#value;
  }

  get next() {
    return this.#next;
  }

  set next(node) {
    this.#next = node;
  }

  get previous() {
    return this.#previous;
  }

  set previous(node) {
    this.#previous = node;
  }
}

class LinkedList {
  #first = null;
  #last = null;
  #counter = 0;

  constructor(value) {
    const node = new Node(value);
    this.#first = node;
    this.#last = node;
    this.#counter++;
  }

  add(value) {
    const node = new Node(value);
    node.previous = this.#last;
    this.#last.next = node;
    this.#last = node;
    this.#counter++;
  }

  head() {
    return this.#first;
  }

  tail() {
    return this.#last;
  }

  nthFromStart(n) {
    if (n > this.#counter) return null;
    let i = 0;
    let node = this.#first
    while(i < n && node) {
      if (i + 1 == n) return node.value;
      node = node.next;
      i++;
    }
  }

  nthFromEnd(n) {
    if (n > this.#counter) return null;
    let i = 0;
    let node = this.#last;
    while(i < n && node) {
      if (i + 1 == n) return node.value;
      node = node.previous;
      i++;
    }
  }
}

function nthFromEnd(head, n) {
  let target = head;
  let control = head;

  for (let i = 0; i < n - 1; i++) {
    if (control.next === null) return null;
    control = control.next;
  }

  while (control.next !== null){
    control = control.next;
    target = target.next;
  }

  return target.value;
}

// ----------------------------------------------------------------------------

function test() {
  const list = new LinkedList(1);
  for (let i = list.head().value + 1; i <= 7; i++) {
    list.add(i);
  }
  console.log(`expected 7, result: ${list.nthFromEnd(1)}`);
  assert.strictEqual(7, list.nthFromEnd(1));

  console.log(`expected 1, result: ${list.nthFromEnd(7)}`);
  assert.strictEqual(1, list.nthFromEnd(7));

  console.log(`expected 5, result: ${list.nthFromEnd(3)}`);
  assert.strictEqual(5, list.nthFromEnd(3));

  console.log(`expected null, result: ${list.nthFromEnd(100)}`);
  assert.strictEqual(null, list.nthFromEnd(100));

  // --------------------------------------------------------------------------
  let value = nthFromEnd(list.head(), 3);
  console.log(`expected 5, result: ${value}`);

  value = nthFromEnd(list.head(), 8);
  console.log(`expected null, result: ${value}`);
}


const main = () => {
  test();
};

if (require.main === module) main();

