class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)

        candidates = [None] * 2
        candidate_data = [0] * 2 # Initially used to determine the candidate majority

        for el in nums:
            if candidates[0] == el:
                candidate_data[0] += 1
            elif candidates[1] == el:
                candidate_data[1] += 1
            elif candidate_data[0] == 0:
                candidates[0] = el
                candidate_data[0] = 1
            elif candidate_data[1] == 0:
                candidates[1] = el
                candidate_data[1] = 1
            else:
                candidate_data[0] -= 1
                candidate_data[1] -= 1

        candidate_data = [0] * 2 # Reset to count actual occurrences of candidates
        for el in nums:
            if el == candidates[0]:
                candidate_data[0] += 1
            elif el == candidates[1]:
                candidate_data[1] += 1

        results = []
        for i in range(2):
            if candidate_data[i] > n // 3:
                results.append(candidates[i])

        return results