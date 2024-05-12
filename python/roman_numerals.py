'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol    Value
  I        1
  V        5
  X        10
  L        50
  C        100
  D        500
  M        1000

For example, 2 is written as II in Roman numeral, just two ones added together.
12 is written as XII, which is simply X + II. The number 27 is written as XXVII,
which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However,
the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four. The same principle
applies to the number nine, which is written as IX.

There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.


Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


Constraints:
1) 1 <= s.length <= 15
2) s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
3) It is guaranteed that s is a valid roman numeral in the range [1, 3999].
   from I to MMMCMXCIX
'''

symbols = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def roman_to_int(roman: str) -> int:
    end = len(roman) - 1
    res = 0

    for idx, rmn in enumerate(roman):
        num = symbols[rmn]
        res += -num if (idx < end and symbols[roman[idx + 1]] > num) else num

        # if idx != end:                          # - Si no estamos en el ultimo elemento
        #     nxt = symbols[roman[idx + 1]]       # obtengamos el valor del siguiente item
        #     if nxt > num:                       # Si es mayor que el numero actual
        #         res -= num                      # restamos
        # else:                                   # - Si no estamos al final
        #     res += num                          # sumamos

        print(idx, rmn, num, res)

    return res



if __name__ == '__main__':
    print(f'Res: {roman_to_int('IV')}')

