from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_count = Counter(nums)
        idx = 0
        for i in [0,1,2]:
            for j in range(num_count[i]):
                nums[idx] = i
                idx += 1
        
        
        