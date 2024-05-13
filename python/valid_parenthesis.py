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
# Contranints:
# 1 <= s.length <= 10^4
# s consists of parenthesis only '()[]{}'
# -----------------------------------------------------------------------------
import unittest

class TestValidParentheses(unittest.TestCase):
    def test_expect_tobe_true(self):
        self.assertTrue(implementation())

    def test_expect_tobe_false(self):
        self.assertFalse(implementation())

# leet code shit
class Solution:
    def isValid(self, s: str) -> bool:
        return implementation(s)


def implementation():
    return None


if __name__ == '__main__':
    unittest.main()

