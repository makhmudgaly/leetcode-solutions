class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 1
        right = len(nums) - 1
        
        while left <= right:
            nums[0]^=nums[left]
            nums[0]^=nums[right]
            left += 1
            right -= 1
            
        
        return nums[0]