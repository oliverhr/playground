const Node = require('../Node');

class BinaryTree {
  #root = null;

  constructor(value) {
    this.root = new Node(value);
  }

  get root() {
    return this.#root;
  }

  set root(node) {
    this.#root = node;
  }

  #nodeFactory(value) {
    if (typeof value !== 'number') throw new Error('WTF Bro!, Only numeric values are allowed.');

    if (value === this.root.value) throw new Error('Duplicated values not allowed.');

    return new Node(value);
  }

  add(value = null) {
    const node = this.#nodeFactory(value);
    const inner = (parent) => {
      const brach = (value < parent.value) ? 'left' : 'right';
      if (parent[brach] instanceof Node) {
        inner(parent[brach]);
      } else {
        parent[brach] = node;
      }
    };
    inner(this.#root);
  }
}

module.exports = BinaryTree;
