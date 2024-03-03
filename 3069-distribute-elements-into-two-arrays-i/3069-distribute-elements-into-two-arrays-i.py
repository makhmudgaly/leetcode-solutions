class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        p1, p2 = [nums[0]], [nums[1]]
        
        for i in range(2, len(nums)):
            if p1[-1] > p2[-1]:
                p1.append(nums[i])
            else:
                p2.append(nums[i])
        
                
        return p1 + p2