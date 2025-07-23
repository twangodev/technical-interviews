from typing import List


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        buckets = {}

        for el in strs:
            counts = [0] * 26

            for c in el:
                normalized = ord(c) - ord("a") # Normalize to 0-25 range for 'a' to 'z'
                counts[normalized] += 1

            key = tuple(counts) # Can use bytes as it is also hashable, but you are limited to 256 as a maximum count

            if key not in buckets:
                buckets[key] = []

            buckets[key].append(el)

        return list(buckets.values())