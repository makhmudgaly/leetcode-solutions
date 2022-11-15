class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        avg_set = set()
        nums = sorted(nums)
        
        while len(nums) != 0:
            avg_set.add((nums[0] + nums[-1]) / 2)
            del nums[0]
            del nums[-1]
        
        return len(avg_set)
            