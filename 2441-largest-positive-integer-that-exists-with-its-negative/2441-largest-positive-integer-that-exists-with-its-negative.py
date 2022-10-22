class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            d[i]=1
        
        ans = -1
        
        for num in nums:
            if num < 0:
                continue
            
            if num > ans and -num in d:
                ans = num
        
        return ans
        