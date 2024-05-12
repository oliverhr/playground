// Valid anagram

const original = 'altisonancia'
const anagram  = 'nacionalista'

function isValidAnagram(original, anagram) {
  if (anagram.length !== original.length) return false;

  const cntO = new Map();
  const cntA = new Map();

  for (let i = 0; i < original.length; i++) {
    const co = original[i];
    const no = cntO.get(co) ?? 0;
    cntO.set(co, no + 1);

    const ca = anagram[i];
    const na = cntA.get(ca) ?? 0;
    cntA.set(ca, na + 1);
  }

  for (let [key, value] of cntO.entries()) {
    if (!cntA.has(key)) return false;
    if (cntA.get(key) !== value) return false;
  }

  return true;
}

const isValid = isValidAnagram(original, anagram)
console.log(isValid);
