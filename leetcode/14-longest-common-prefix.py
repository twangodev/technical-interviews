from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = strs[0]

        for i in range(1, len(strs)):
            current = strs[i]

            up_to = 0

            for j in range(min(len(prefix), len(current))):
                if prefix[j] != current[j]:
                    break
                up_to += 1

            prefix = prefix[:up_to]

        return prefix