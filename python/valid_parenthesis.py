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


def implementation(string):
    if len(string) == 1: return False
    opens = {'(', '[', '{'}
    pairs = {')': '(', ']': '[', '}': '{'}\
    stack = list()
    for ch in string:
        if ch in opens:
            stack.append(ch)
            continue
        if not stack: return False
        if ch in pairs and stack[-1] != pairs.get(ch):
            return False
        stack.pop()
    return stack == []

if __name__ == '__main__':
    unittest.main()

