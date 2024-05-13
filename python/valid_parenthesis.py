# -----------------------------------------------------------------------------
# Valid Prentheses
# - Given a string "s" containing just the characters:
#       '(', ')', '{', '}', '[' and ']'
#
# Determine if the input string has valid open/close brackets.
#
# An input is considered valid if:
#
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.
#
# Constraints:
#   - 1 <= s.length <= 10^4
#   - s consists of parenthesis only '()[]{}'
# -----------------------------------------------------------------------------
import unittest


class TestValidParentheses(unittest.TestCase):
    def test_expect_true(self):
        self.assertTrue(implementation('()'))
        self.assertTrue(implementation('(){}[]'))
        self.assertTrue(implementation('{([])}'))

    def test_expect_false(self):
        self.assertFalse(implementation('{'))
        self.assertFalse(implementation(']'))
        self.assertFalse(implementation('(]'))
        self.assertFalse(implementation('(('))
        self.assertFalse(implementation(']]'))
        self.assertFalse(implementation('){'))


# leet code shit
class Solution:
    def isValid(self, s: str) -> bool:
        return implementation(s)

def implementation(string):
    """
    Estratégia: vamos a iterar por la cadena de texto
    buscando por brackets de apertura, si se encuentra
    un bracket de cierre primero se regresa False.

    Como soporte se va a utilizar un stack para ir
    agregando los simbolos de apertura que se vayan
    encontrando, la interacción válida es:
    apertaura/cierre, es decir se puede espeerar
    varios elementos de apertura seguidos, pero si
    por cada item de apertura debe primero aparecer
    el cierre del último elemento abierto.
    """
    length = len(string)
    if not length or length % 2 != 0:
        return False

    chars = {'(': ')',
             '[': ']',
             '{': '}',}

    stack = list()
    for ch in string:
        if ch in chars:
            stack.append(chars.get(ch))
        elif not stack or ch != stack.pop():
            return False
    return stack == []


if __name__ == '__main__':
    unittest.main()

