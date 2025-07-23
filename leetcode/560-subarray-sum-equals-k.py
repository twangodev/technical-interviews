from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        cumulative = {0: 1}

        s = 0
        count = 0

        for n in nums:
            s+= n
            complement = s - k

            if complement in cumulative:
                count += cumulative[complement]

            cumulative[s] = cumulative.get(s, 0) + 1

        return count
