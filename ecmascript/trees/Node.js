class Node {
  #value = NaN;

  #left = null;

  #right = null;

  constructor(value) {
    this.value = value;
  }

  set value(val) {
    this.#value = val;
  }

  get value() { return this.#value; }

  set left(node) {
    if (!(node instanceof Node)) {
      throw new Error('The item must be a Node');
    }
    this.#left = node;
  }

  get left() {
    return this.#left;
  }

  set right(node) {
    if (!(node instanceof Node)) {
      throw new Error('The item must be a Node');
    }
    this.#right = node;
  }

  get right() {
    return this.#right;
  }

  hasChildren() {
    return (this.leaf !== null) && (this.right !== null);
  }

  isLeaf() {
    return (this.leaf === null) && (this.right === null);
  }
}

module.exports = Node;
