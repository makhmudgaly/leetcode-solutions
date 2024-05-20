class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        old_parity = nums[0] & 1
        for i in range(1,len(nums)):
            curr_parity = nums[i] & 1
            if old_parity == curr_parity:
                return False
            old_parity = curr_parity
        
        return True