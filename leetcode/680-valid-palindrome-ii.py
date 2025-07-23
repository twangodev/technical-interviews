def check(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        left = 0
        right = n - 1

        while left < right:
            if s[left] != s[right]:
                return check(s, left + 1, right) or check(s, left, right - 1)
            left += 1
            right -= 1

        return True
