class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        for i in range(len(nums)-2):
            for j in range(i,len(nums)-1):
                for k in range(j,len(nums)):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        count+=1
        
        return count
                        
        