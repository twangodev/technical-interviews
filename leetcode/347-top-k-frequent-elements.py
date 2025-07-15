class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}

        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        count_list = [(-freq, n) for n, freq in counts.items()]
        heapq.heapify(count_list)

        results = []
        for _ in range(k):
            results.append(heapq.heappop(count_list)[1])

        return results