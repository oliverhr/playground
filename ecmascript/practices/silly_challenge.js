const println = (str) => process.stdout.write(`${str}\n`);

const array = [
  0, 1, 0, 1, 0,
  1, 0, 0, 1, 1,
  0,
];

function sort(arr) {
  const ones = arr.join('').replaceAll('0', '').length;
  const zeros = arr.length - ones;

  return [
    ...Array(zeros).fill(0),
    ...Array(ones).fill(1),
  ];
}

println(sort(array));
println('-'.repeat(40));

function onezero(arr) {
  return [
    ...arr.filter((i) => Boolean(!i)), // !!!i
    ...arr.filter((i) => Boolean(i)), // !!i
  ];
}
println(onezero(array));
println('-'.repeat(40));

println([...array.filter((i) => (i ? 0 : 1)), ...array.filter((i) => (i ? 1 : 0))]);
println('-'.repeat(40));

println([...array.filter((i) => (!i || 0)), ...array.filter((i) => (0 || i))]);
