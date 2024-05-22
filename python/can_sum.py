# -----------------------------------------------------------------------------
# Can Sum
#
# Write a funcion "can_cum(target_sum, numbers)", taht takes an integer
# which is the desired result, and an array of numbers as arguments.
#
# The function should return a boolean indicating whether or not it is
# posible to generate the target_sum using numbers from the array
#
# Constraints:
# - Only numbers in the array can be used
# - Numbers in the array can be used as many times as needed
# - Assume all input numbers are positive numbers.
# -----------------------------------------------------------------------------
import unittest

class TestCanSum(unittest.TestCase):
    def test_can_sum_tobe_true(self):
        self.assertEqual(True, implementation(7, [2, 3]))
        self.assertEqual(True, implementation(7, [5, 3, 4, 7]))
        self.assertEqual(True, implementation(8, [2, 3, 5]))

    def test_can_sum_tobe_false(self):
        self.assertEqual(False, implementation(7, [2, 4]))
        self.assertEqual(False, implementation(7, [14]))


def implementation(total: int, addends: list[int]):
    def fn(num: int, numbers: list[int], mem: dict[int, bool]={}):
        if num in mem: return mem[num]
        if num == 0: return True
        if num < 0: return False
        for n in numbers:
            reminder = num - n
            if num >= n and fn(reminder, numbers) == True:
                mem[num] = True
                return True
        mem[num] = False
        return False
    return fn(total, addends)


if __name__ == '__main__':
    unittest.main()
