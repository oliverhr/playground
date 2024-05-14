import unittest

class TestValidParentheses(unittest.TestCase):
    def test_expect_true(self):
        self.assertEqual([4, 3, 2, 2], plus_one([4, 3, 2, 1]))
        self.assertEqual([1, 0], plus_one([9]))
        self.assertEqual([2, 0], plus_one([1, 9]))
        self.assertEqual([5, 0, 0], plus_one([4, 9, 9]))


def plus_one(digits):
    carry = 1 # nomber to add
    # start from the last index, meaning
    # from the most right number
    for (idx, curr) in reversed(list(enumerate(digits))):
        carry += curr # add to the last index
        digits[idx] = carry % 10 # ten or th number
        carry = carry // 10 # if was more than then keep the carry
        if carry == 0: return digits
    return [1] + [0] * len(digits)


if __name__ == '__main__':
    unittest.main()
