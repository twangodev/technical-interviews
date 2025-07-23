from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        n = len(nums)

        for i in range(n):
            el = nums[i]

            if el <= 0 or el > n:
                nums[i] = n + 1

        for i in range(n):
            el = abs(nums[i])
            if 1 <= el <= n:
                target = el - 1
                nums[target] = -abs(nums[target])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1
