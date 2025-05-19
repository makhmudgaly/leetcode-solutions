from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counter = {0:0, 1:0, 2:0}
        insertIdx = 0

        for num in nums:
            counter[num] += 1
        
        for num in [0,1,2]:
            for j in range(counter[num]):
                nums[insertIdx] = num
                insertIdx += 1
        
        

        
        
        