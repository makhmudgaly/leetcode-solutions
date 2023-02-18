class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        nums = set(nums)
        
        power = 0
        
        while power != 32:
            if 2 ** power not in nums:
                return 2 ** power
            power+=1
        