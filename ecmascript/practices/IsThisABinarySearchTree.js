class Node {
  #value = NaN;
  #left = null;
  #right = null;

  constructor(value, left = null, right = null) {
    this.#value = value;
    this.#left = left;
    this.#right = right;
  }

  get value() {
    return this.#value;
  }

  set left(node) {
    if (!(node instanceof Node)) throw Error('??????')
    this.#left = node;
  }

  set right(node) {
    if (!(node instanceof Node)) throw Error('??????')
    this.#right = node;
  }

  get left() {
    return this.#left;
  }

  get right() {
    return this.#right;
  }

  toString() {
    return `Node value: ${this.#value}`
      .concat(
        '\n', `Left child: ${this.#left ? this.#left.value : 'null'}`,
        '\n', `Right child: ${this.#right ? this.#right.value : 'null'}`
      );
  }
}


function isBinarySearchTree(node, min = null, max = null) {
  if (min !== null && node.value < min) return false;
  if (max !== null && node.value > max) return false;

  const leftIs = (node.left) ? isBinarySearchTree(node.left, min, node.value) : true;
  const rightIs = (node.right) ? isBinarySearchTree(node.right, node.value, max) : true;

  return leftIs && rightIs;
}


function create(hash, value) {
  const tree = { [value]: new Node(value) }

  for (const [left, right] of Object.values(hash)) {
    tree[left] = new Node(left);
    tree[right] = new Node(right);
  }

  for (const [key, [left, right]] of Object.entries(hash)) {
    tree[key].left = tree[left];
    tree[key].right = tree[right];
  }

  return tree[value];
}

// ----------------------------------------------------------------------------

function test0() {
  const hash = {
    0: [1, 2],
  }
  const root = create(hash, 0);

  console.log('-------------------------------------')
  console.log('Hash is a BST?', isBinarySearchTree(root));
}

function test1() {
  const hash = {
    0: [1, 2],
    1: [3, 4],
    2: [5, 6]
  }
  const root = create(hash, 0);

  console.log('-------------------------------------')
  console.log('Hash is a BST?', isBinarySearchTree(root));
}
function test1() {
  const hash = {
    0: [1, 2],
    1: [3, 4],
    2: [5, 6]
  }
  const root = create(hash, 0);

/*
  console.log('--------------- tree ----------------')
  console.log(root.value, root.left.value, root.right.value);
  console.log('-------------------------------------')
*/

  console.log('-------------------------------------')
  console.log('Hash is a BST?', isBinarySearchTree(root));
}

function test2() {
  const hash = {
    3: [1, 5],
    1: [0, 2],
    5: [4, 6],
  }
  const root = create(hash, 3);

/*
  console.log('--------------- tree ----------------')
  console.log(root.value, root.left.value, root.right.value);
  console.log('-------------------------------------')
*/

  console.log('-------------------------------------')
  console.log('Hash is a BST?', isBinarySearchTree(root));
}

test0();
//test1();
//test2();
