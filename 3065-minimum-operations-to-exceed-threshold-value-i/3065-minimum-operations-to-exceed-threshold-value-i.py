class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        c = 0
        for num in nums:
            c += num >=k
        
        return n - c