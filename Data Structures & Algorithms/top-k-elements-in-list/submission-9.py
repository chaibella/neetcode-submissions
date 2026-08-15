class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vals = []
        for num, cnt in Counter(nums).items():
            heapq.heappush(vals, (-cnt, num))

        res = []
        for _ in range(k):
            res.append(heapq.heappop(vals)[1])
        
        return res