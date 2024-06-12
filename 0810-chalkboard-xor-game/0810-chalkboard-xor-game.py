class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        x = 0
        for v in nums:
            x ^= v
        
        return x == 0 or len(nums) & 1 == 0