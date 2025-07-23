from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        solutions = {}

        for i in range(len(nums)):
            current = nums[i]
            complement = target - current

            if current in solutions:
                return [i, solutions[current]]

            solutions[complement] = i
