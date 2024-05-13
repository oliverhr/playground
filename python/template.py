# -----------------------------------------------------------------------------
# Title
#
# Description
#       details
#
# Additional instructions
#
#
# Contranints:
# - xyz
# -----------------------------------------------------------------------------

def implementation():
    return None


def test_expect_tobe_true():
    expected = True
    actual = implementation()
    assert expected == actual, \
           f'expected {expected} but {actual} was received.'


def test_expect_tobe_false():
    expected = False
    actual = implementation()
    assert expected == actual, \
           f'expected {expected} but {actual} was received.'


# leet code shit
class Solution:
    def isValid(self, s: str) -> bool:
        return implementation(s)

if __name__ == '__main__':
    test_expect_tobe_true()
    test_expect_tobe_false()

