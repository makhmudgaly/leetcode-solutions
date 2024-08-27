import heapq
class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        gcd = math.gcd(*numsDivide)
        heapq.heapify(nums)
        count = 0
        while nums:
            div = heapq.heappop(nums)
            if gcd % div == 0:
                return count
            count += 1
        
        return -1