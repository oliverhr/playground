def rotate(matrix, n=0):
    rows = len(matrix)
    cols = len(matrix[0])
    size = len(matrix) - 1
    collection = [[None] * cols for row in range(rows)]
    for i in range(rows):
        for j in range(cols):
            collection[j][size-i] = matrix[i][j]
    return collection

import unittest
class TestMatrixRotation(unittest.TestCase):
    def test_one(self):
        original = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]
        # rotate(a1, 3) should return:
        expected = [[7, 4, 1],
                    [8, 5, 2],
                    [9, 6, 3]]
        rotated = rotate(original)
        self.assertListEqual(rotated, expected)


    def test_two(self):
        original = [[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 16]]
        # rotate(a2, 4) should return:
        expected =[[13, 9, 5, 1],
                   [14, 10, 6, 2],
                   [15, 11, 7, 3],
                   [16, 12, 8, 4]]
        rotated = rotate(original)
        rotated[1][1] = 0
        self.assertListEqual(rotated, expected)


if __name__ == '__main__':
    unittest.main()
