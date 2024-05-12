# -----------------------------------------------------------------------------
#  Non repeated character
#
#  Implement a function that takes a string and returns the
#  first character that does not appear twice or more.
#
#  constraints:
#    - The first unique element is the expected if multiple uniques exists
#    - All characters are upper or lower case but not mixed
#    - if there are non-repeating characters return an empty string
# -----------------------------------------------------------------------------

def non_repeating(string: str) -> str | None:
  if len(string) == 0: return None

  mem: dict[str, int] = {}

  for ch in string:
    mem[ch] = mem.get(ch, 0) + 1

  for char, counter in mem.items():
    if counter == 1: return char

  return None


# -----------------------------------------------------------------------------

def caller(string, expected):
  result = non_repeating(string);
  print(f'Non repeating character in "{string}" ' \
        + f'is {result}, expected is {expected}');


def main():
  caller('aabbcb', 'c')
  caller('xxyz', 'y')
  caller('abcab', 'c')
  caller('abab', None)
  caller('aabbbc', 'c')
  caller('aabbdbc', 'd')

if __name__ == '__main__':
  main()
