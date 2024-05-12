# -----------------------------------------------------------------------------
# Non repeated character
#
# Given a string, find the first non-repeating character in it
# and return its index.
#
# Constraints:
#   - The first unique element is the expected if multiple uniques exists
#   - All characters are lowercase
#   - If it does not exist, return -1.
#   - 1 <= s.length <= 10^5 (ten to the power of five)
# -----------------------------------------------------------------------------

def non_repeating(string: str) -> int:
  if len(string) == 0: return None

  mem: dict[str, dict[str, int]] = {}

  for idx, ch in enumerate(string):
    if ch in mem:
      mem[ch]['counter'] = mem.get(ch)['counter'] + 1
      mem[ch]['index'] = idx
    else:
      mem[ch] = {'counter': 1,'index': idx};

  for data in mem.values():
    if data['counter'] == 1: return data['index']

  return -1

# -----------------------------------------------------------------------------

def caller(string, expected):
  result = non_repeating(string);
  print(f'Non repeating character in "{string}" ' \
        + f'is {result}, expected is {expected}');

def main():
  caller('aabbcb', 4)
  caller('xxyz', 2)
  caller('abcab', 2)
  caller('abab', -1)
  caller('aabbbc', 5)
  caller('aabbdbc', 4)

if __name__ == '__main__':
  main()
