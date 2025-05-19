class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums = sorted(nums)
        
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        
        if nums[0] == nums[1] == nums[2]:
            return "equilateral"
        if nums[0] != nums[1] != nums[2]:
            return "scalene"
        
        return "isosceles"