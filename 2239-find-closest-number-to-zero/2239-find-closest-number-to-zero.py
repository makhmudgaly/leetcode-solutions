class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums = sorted(nums, key=lambda x: (abs(0-x), -x))
        return nums[0]
        