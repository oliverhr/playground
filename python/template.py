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

