class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        n = len(word1)
        m = len(word2)

        i = 0
        j = 0

        result = []

        while i < n or j < m:

            if i < n:
                result.append(word1[i])
                i += 1

            if j < m:
                result.append(word2[j])
                j += 1

        return "".join(result)
