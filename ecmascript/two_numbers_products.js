
// BigO = O(n^2)
function twoNumberProducts(array) {
  const products = [];
  steps = 0;

  for (let i = 0; i < array.length - 1; i++) {
    for (let j = i + 1; j < array.length; j++) {
      steps++;
      products.push(array[i] * array[j]);
    }
  }
  console.log('Steps', steps);
  return products;
}


console.log(
  twoNumberProducts([1, 2, 3, 4, 5, 6, 7, 8])
);


/*
 * Because we are dealing with different
 * datasets, BigO = O(n *  m)
 */
function twoArraysProducts(first, second) {
  const products = [];
  let steps = 0;

  for (let i = 0; i < first.length; i++) {
    for (let j = 0; j < second.length; j++) {
      steps++;
      products.push(first[i] * second[j]);
    }
  }
  console.log('Steps', steps);
  return products;
}

console.log(
  twoArraysProducts([2, 3, 4], [5, 6, 7])
);
