// Find two integers that multiply to 20
const searched = 20;
const numbers = [2, 2, 4, 1, 6, 5, 40, -1]; // se espera: [4, 5]


function findTwoNumbersProductV1(target, array) {
  let answer = [];
  for (let i = 0; i < array.length - 1; i++) {
    for (let j = i + 1; j < array.length; j += 1) {
      if ((array[i] * array[j]) === target) answer = [array[i], array[j]];
    }
  }

  return answer;
}
console.log('findTwoNumbersProductV1', findTwoNumbersProductV1(searched, numbers));


function findTwoNumbersProductV2(target, array) {
  const mem = new Set();

  for (let i = 0; i < array.length - 1; i += 1) {
    const current = array[i];
    if (!mem.has(current)) {
      for (let j = i + 1; j < array.length; j += 1) {
        const product = array[i] * array[j];
        if (product === target) return [current, array[j]];
      }
      mem.add(current);
    }
  }

  return [];
}
console.log('findTwoNumbersProductV2', findTwoNumbersProductV2(searched, numbers));


function findTwoNumbersProductV3(target, array) {
  const number = new Set();

  for (const currentItem of array) {
    const seen = target / currentItem;
    if (number.has(seen)) return [seen, currentItem];
    number.add(currentItem);
  }

  return [];
}
console.log('findTwoNumbersProductV3', findTwoNumbersProductV3(searched, numbers));
