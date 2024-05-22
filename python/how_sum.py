# -----------------------------------------------------------------------------
# How Sum
#
# Write a funcion "how_cum(target_sum, numbers)", taht takes an integer
# which is the desired result of the sum, and an array of numbers as arguments.
#
# The function should return an array containing any combination of elements
# that add up to exactly the target_sum. If there is no combination that adds
# up to the target_sum, then return None/Null.
#
# Constraints:
# - Only numbers in the array can be used
# - Numbers in the array can be used as many times as required, ie.:
#   + target: 8, array: [2,3,5], valid answers: [2,2,2,2]; [2,3,3]; [3,5];
# - Return any single combination, doesn't matter if there are many
# -----------------------------------------------------------------------------
import unittest

class TestHowSum(unittest.TestCase):
    def test_returned_array_sum_is_equal_to_target(self):
        self.assertEqual(expected:=0, sum(implementation(expected, [])))
        self.assertEqual(expected:=7, sum(implementation(expected, [5, 3, 4, 7])))
        self.assertEqual(expected:=8, sum(implementation(expected, [2, 3, 5])))

    def test_returns_none(self):
        self.assertEqual(None, implementation(7, [2, 4]))
        self.assertEqual(None, implementation(300, [7, 14]))


def implementation(target_sum: int, numbers: list[int]) -> list[int] | None:
    """
    Inner function to simplify and encapsulate the memoization
    """
    mem: dict[int, list] = {}
    def how_sum(target) -> list[int] | None:
        if target in mem: return mem[target]
        if target == 0: return []
        if target < 0: return None

        for num in numbers:
            remnant: int = target - num
            if (result := how_sum(remnant)) is not None:
                mem[target] = [ *result, num ]
                return mem[target]
        mem[target] = None
        return None
    return how_sum(target_sum)


if __name__ == '__main__':
    unittest.main()
