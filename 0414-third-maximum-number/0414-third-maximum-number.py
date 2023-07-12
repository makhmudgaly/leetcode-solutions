class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(set(nums), reverse=True)
        if len(nums) < 3:
            return nums[0]
        return nums[2]
        