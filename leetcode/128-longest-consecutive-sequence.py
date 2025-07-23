from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        answer = 0

        for n in nums:
            previous = n - 1

            if previous in nums:
                continue

            length = 1
            while n + length in nums:
                length += 1

            answer = max(answer, length)

        return answer