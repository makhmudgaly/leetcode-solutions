class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        n = len(nums)
        avg = max(nums)
        nums.sort()
        i = 0
        j = n - 1
        while i < j:
            avg = min(avg, (nums[i] + nums[j])/2)
            i += 1
            j -= 1
        
        return avg