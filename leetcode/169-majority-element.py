class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        majority = None
        count = 0

        for i in nums:
            if count == 0:
                majority = i

            count += 1 if i == majority else -1

            if count > len(nums) // 2:
                return i

        return majority