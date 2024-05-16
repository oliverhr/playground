"""
3Sum

Description 
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets. 

Example 1:
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [ [-1, -1, 2], [-1 ,0 ,1] ]

Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0, 1 , 1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0, 0, 0]
Output: [ [0, 0, 0] ]
Explanation: The only possible triplet sums up

Contraints:
* 3 <= nums.length <= 3000
* -105 <= nums[i] <= 105
"""
import unittest


class TestThreeSumNumZero(unittest.TestCase):
	def test_case_1(self):
		self.assertListEqual(implementation([-1,0,1,2,-1,-4]), [
			[-1, -1, 2],
			[-1, 0, 1],
		])

	def test_case_2(self):
		self.assertListEqual(implementation([0,1,1]), [])

	def test_case_3(self):
		self.assertListEqual(implementation([0,0,0]), [[0,0,0]])

	def test_case_4(self):
		self.assertListEqual(implementation([0,0,0,0]), [[0,0,0]])

# -----------------------------------------------------------------------------

def implementation(nums: list[int]) -> list[list[int]]:
	zero = 0;
	output = []
	nums.sort()

	if nums[0] > 0: return output
	for i in range(len(nums) - 2):
		if i > 0 and nums[i - 1] == nums[i]: continue

		left = i + 1
		right = len(nums) - 1

		target = 0 - nums[i]

		while (left < right):
			if (calc := nums[left] + nums[right]) == target:
				triplet = [nums[i], nums[left], nums[right]]
				output.append(triplet)
				left += 1
				right -= 1
			elif calc < target:
				left += 1
			else:
				right -= 1

	return  output

# -----------------------------------------------------------------------------

if __name__ == '__main__':
	unittest.main()
	# arr = implementation([-1,0,1,2,-1,-4])
	# print(arr)
