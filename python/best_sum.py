# -----------------------------------------------------------------------------
# Best SUm
#
# Write a funcion "best_sum(target_sum, numbers)", that takes an integer
# which is the desired result of the sum, and an array of numbers as arguments.
#
# The function should return an array containing the shorthest combination of
# numbers that add up to exactly the target_sum.
#
# Constraints:
# - Only numbers in the array can be used
# - If there is any combinations tie, return any of the shortest combinations
# - Numbers in the array can be used as many times as required
# -----------------------------------------------------------------------------
import unittest

def implementation():
    return None


def test_expects_to_be_true():
    expected = True
    actual = implementation()
    assert expected == actual, \
           f'expected {expected} but {actual} was received.'


def test_expects_to_be_false():
    expected = False
    actual = implementation()
    assert expected == actual, \
           f'expected {expected} but {actual} was received.'

# leet code shit
class Solution:
    def isValid(self, s: str) -> bool:
        return implementation(s)

if __name__ == '__main__':
    test_expects_to_be_true()
    test_expects_to_be_false()

