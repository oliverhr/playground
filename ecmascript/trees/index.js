const BinarySearchTree = require('./SearchTree/BinarySearchTree');
const Node = require('./Node');

// ----------------------------------------------------------------------------
const println = (str = '') => process.stdout.write(`${str}\n`);
const printtab = (str = '') => process.stdout.write(`${str}\t`);
// ----------------------------------------------------------------------------

const Order = Object.freeze({
  Pre: Symbol('pre'),
  In: Symbol('in'),
  Post: Symbol('post'),
});

function traverse(node, order = Order.In) {
  if (node === null) return;

  const print = () => process.stdout.write(`${node.value} `);

  if (order === Order.Pre) print();
  traverse(node.left, order);
  if (order === Order.In) print();
  traverse(node.right, order);
  if (order === Order.Post) print();
}

module.exports = () => {
  const bst = new BinarySearchTree(50);
  const items = [25, 75, 10, 33, 56, 89, 4, 11, 30, 40, 52, 61, 82, 95];
  items.forEach((item) => bst.add(item));

  println('-'.repeat(80));

  printtab('Order.Pre:');
  traverse(bst.root, Order.Pre);

  printtab('\nOrder.In:');
  traverse(bst.root, Order.In);

  printtab('\nOrder.Post:');
  traverse(bst.root, Order.Post);
  println();

  println('-'.repeat(80));
  const node = new Node(99);
  println(node.isLeaf());

  node.left = new Node(30);
  println(node.isLeaf());
  println(node.left.value);
  println((node.right && node.left));
};
