class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        for idx in range(1, len(nums)):
            nums[0] |= nums[idx]
        
        return nums[0]
            
        