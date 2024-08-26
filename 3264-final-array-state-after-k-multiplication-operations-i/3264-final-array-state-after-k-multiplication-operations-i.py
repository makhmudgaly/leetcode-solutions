class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n = len(nums)
        q = [(nums[i], i) for i in range(n)]
        heapq.heapify(q)
        
        while k > 0:
            val, idx = heapq.heappop(q)
            nums[idx] = val * multiplier
            heapq.heappush(q, (val * multiplier, idx))
            k -= 1
        
        return nums