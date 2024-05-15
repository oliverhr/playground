"""
Palindrome Partitioning

Given a string s, partition s such that every substring of the partition
is a palindrome. Return all possible palindrome partitioning of s.


----------------------------------
Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

----------------------------------
Example 2:
Input: s = "a"
Output: [["a"]]


Constraints:

* 1 <= s.length <= 16
* s contains only lowercase English letters
"""
import unittest


class TestPalindromePartitioning(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(partition('a'), [['a']])

    def test_case_2(self):
        self.assertEqual(partition('ab'), [['a', 'b']])

    def test_case_3(self):
        self.assertEqual(partition('aab'), [
            ['a','a','b'],
            ['aa','b']
        ])


# -----------------------------------------------------------------------------
def is_palindrome(string: str) -> bool:
    return len(string) and string == string[::-1]

def partition(string: str) -> list[list[str]]:
    def backtrack(index=0, path=[]):
        if index < length:
            for limit in range(index + 1, length + 1):
                subset = string[index:limit]
                if is_palindrome(subset):
                    path.append(subset)
                    backtrack(limit, path)
                    path.pop()
            return None

        partitions.append(path.copy())
        return None

    # -- Preamble
    length = len(string)
    partitions = []
    backtrack()
    return partitions


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
