import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[^a-z0-9]", "", s.lower())
        print(s)

        n = len(s)

        half = n // 2
        for i in range(half):
            j = n - i - 1
            if s[i] != s[j]:
                return False

        return True