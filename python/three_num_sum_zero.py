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
	def test_case_5(self):
		self.assertListEqual(implementation([-2,0,0,2,2]), [[-2,0,2]])

	def test_case_4(self):
		self.assertListEqual(implementation([0,0,0,0]), [[0,0,0]])

	def test_case_3(self):
		self.assertListEqual(implementation([0,0,0]), [[0,0,0]])

	def test_case_2(self):
		self.assertListEqual(implementation([0,1,1]), [])

	def test_case_1(self):
		self.assertListEqual(implementation([-1,0,1,2,-1,-4]), [
			[-1, -1, 2],
			[-1, 0, 1],
		])

# -----------------------------------------------------------------------------

def implementation(nums: list[int]) -> list[list[int]]:
	zero = 0
	nums.sort()
	output = []

	if nums[0] > 0: return output

	for index in range(len(nums) - 2):
		# after the first index (0) if current value
		# is the same as the previous skip aka continue
		if index > zero and nums[index] == nums[index-1]:
			continue

		# left pointer is next to current index
		left = index + 1
		# right is the last item in the list
		right = len(nums) - 1

		# index is increased each iteration
		# we need to move right and left pointers
		# we do this until they are the same

		while left != right:
			triplet = [nums[index], seen:=nums[left], nums[right]]
			summed = sum(triplet)

			# If not zero move only one pointer
			if summed < zero: left += 1; continue
			if summed > zero: right -= 1; continue

			# if zero append the triplet and move the
			# pointers unil skipping repeated values
			if summed == zero:
				output.append(triplet)
				# move pointer l-> to the next different value
				while left < right and nums[left] == seen:
					left += 1
	return output

# -----------------------------------------------------------------------------

if __name__ == '__main__':
	unittest.main()
