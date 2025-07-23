from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        n = len(s)

        for i in range(n // 2):
            end = n - i - 1
            s[i], s[end] = s[end], s[i]